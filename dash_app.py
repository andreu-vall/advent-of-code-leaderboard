from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from plots import generate_figures


app = Dash()
app.title = 'AoC Leaderboard'
server = app.server

app.layout = html.Div([

    html.H1('Advent of Code Leaderboard'),

    html.P('Real time interactive plots from Advent of Code'),

    dcc.Dropdown(id='select_year',
                 options=[
                     {'label': '2020', 'value': 2020},
                     {'label': '2021', 'value': 2021}],
                 value=2021
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
def update_graph(year):
    return generate_figures(year)


if __name__ == '__main__':
    app.run_server()
