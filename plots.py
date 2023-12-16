from datetime import datetime
import plotly.express as px
import pandas as pd
import data


def generate_figures(version):
    year = {1: 2020, 2: 2021, 3: 2022, 4: 2022, 5: 2023}[version]
    user = {1: 1066392, 2: 1075819, 3: 1075819, 4: 1621551, 5: 1075819}[version]
    df, acc_times = data.get_data(year, user)
    n_days = int(df.columns[-2].split('.')[0])
    figure1 = generate_figure1(df, year, n_days)
    figure2 = generate_figure2(df, year, n_days)
    figure3 = generate_figure3(acc_times, year, n_days)
    return figure1, figure2, figure3


def generate_figure1(df, year, n_days):

    too_far = datetime.strptime(f'2/12/{year} 06', '%d/%m/%Y %H')

    times_data = []
    for _, row in df.iterrows():
        for day in range(1, n_days + 1):
            if f'{day}.1' in row:
                date = row[f'{day}.1']
                if not pd.isnull(date):
                    time = date - pd.Timedelta(day - 1, unit='d')
                    if time < too_far:
                        times_data.append({'name': row['name'], 'day': day, 'time': time})

    times = pd.DataFrame(times_data)

    fig = px.line(times, x='day', y='time', line_group='name', color='name', markers=True,
                  title='Hour when Part One Solved', template="simple_white", height=650)
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    fig.update_yaxes(tickformat='%H:%M')
    fig.update_xaxes(dtick=1)
    return fig


def generate_figure2(df, year, n_days):
    base = datetime.strptime(f'1/12/{year}', '%d/%m/%Y')

    times_data = []
    for _, row in df.iterrows():
        for day in range(1, n_days + 1):
            if f'{day}.2' in row:
                time = row[f'{day}.2']
                if not pd.isnull(time):
                    times_data.append({'name': row['name'], 'day': day, 'time': time + base})

    times = pd.DataFrame(times_data)

    fig = px.line(times, x='day', y='time', line_group='name', color='name', markers=True,
                  title='Second Part Spent Time', template="simple_white", height=650)
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    fig.update_yaxes(tickformat='%H:%M:%S')
    fig.update_xaxes(dtick=1)
    return fig


def generate_figure3(acc_times, year, n_days):
    base = datetime.strptime(f'1/12/{year}', '%d/%m/%Y')

    times_data = []
    for _, row in acc_times.iterrows():
        for day in range(1, n_days + 1):
            if str(day) in row:
                time = row[str(day)]
                if not pd.isnull(time):
                    times_data.append({'name': row['name'], 'day': day, 'time': time + base})

    times = pd.DataFrame(times_data)

    fig = px.line(times, x='day', y='time', line_group='name', color='name', markers=True,
                  title='Accumulated Second Part Spent Time', template="simple_white", height=650)
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    fig.update_yaxes(tickformat='%H:%M')
    fig.update_xaxes(dtick=1)
    return fig
