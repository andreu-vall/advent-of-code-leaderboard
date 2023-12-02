from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from plots import generate_figures
from dash_bootstrap_templates import load_figure_template


app = Dash()
app.title = 'AoC Leaderboard'
server = app.server

#load_figure_template('plotly_dark')

app.layout = html.Div([

    html.H1('Advent of Code Leaderboard'),

    html.P(
        ['Real time interactive plots from Advent of Code. You can check out the code at ',
        html.A("GitHub", href = "https://github.com/andreu-vall/advent-of-code-leaderboard")]),

    dcc.Dropdown(id='select_year',
                 options=[
                     {'label': '2020', 'value': 1},
                     {'label': '2021', 'value': 2},
                     {'label': '2022 Doble', 'value': 3},
                     {'label': '2022 GDSC', 'value': 4},
                     {'label': '2023', 'value': 5}],
                 value=5
                 ),

    dcc.Graph(id='first_graph'),
    dcc.Graph(id='second_graph'),
    dcc.Graph(id='third_graph')
])


@app.callback(
    [Output(component_id='first_graph', component_property='figure'),
     Output(component_id='second_graph', component_property='figure'),
     Output(component_id='third_graph', component_property='figure')],
    [Input(component_id='select_year', component_property='value')]
)
def update_graph(version):
    return generate_figures(version)


if __name__ == '__main__':
    app.run_server()
