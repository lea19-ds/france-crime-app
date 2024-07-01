"""Module launching a web app showing crime stats"""

from dash_extensions.javascript import arrow_function, assign
from dash import Dash, Output, Input, html, dcc
import dash_leaflet as dl
import json
import sys

from layers import get_layers, get_info, get_hideout

if len(sys.argv) < 2:
    print('Usage: python app.py data.json')
    exit(1)

json_file = sys.argv[1]
json_data = json.loads(open(json_file, 'r').read())

colorbar, geojson, info, slider = get_layers(json_data)

app = Dash(prevent_initial_callbacks=True)
app.layout = html.Div(children=[
    html.Div(children=[
        html.H3('Taux de criminalité par habitant', style={
            'margin-left': '20px',
            'flex': '1',
            'font-family':'Arial, Helvetica, sans-serif'
        }),
        html.Div(children=[slider], style={'flex': '4'}),
    ], style={
        'height': '5vh',
        'display': 'flex',
        'justify-content': 'space-evenly',
        'align-items': 'center'
    }),
    dl.Map(children=[
        dl.TileLayer(),
        geojson,
        colorbar,
        info,
    ], style={'height': '95vh'}, center=[46, 2], zoom=6),
    dcc.Store(id='selected_year')
])

@app.callback(
    Output('info', 'children'),
    Input('geojson', 'hoverData'),
    Input('selected_year', 'data')
)
def info_hover(feature, year):
    if year is None:
        year = '2016'
    return get_info(feature, json_data, year)

@app.callback(
    Output('geojson', 'hideout'),
    Input('selected_year', 'data')
)
def update_hideout(value):
    if value is None:
        value = '2016'
    return get_hideout(json_data, str(value))

@app.callback(
    Output('selected_year', 'data'),
    Input('slider', 'value')
)
def update_year(value):
    return value

if __name__=='__main__':
    app.run_server(host='0.0.0.0')
