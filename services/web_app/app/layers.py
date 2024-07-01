from dash_extensions.javascript import arrow_function, assign
import dash_leaflet.express as dlx
import dash_leaflet as dl
from dash import html, dcc

classes = [1, 2, 3, 4, 5, 6, 7, 8]
colorscale = [
    '#FFEDA0',
    '#FED976',
    '#FEB24C',
    '#FD8D3C',
    '#FC4E2A',
    '#E31A1C',
    '#BD0026',
    '#800026'
]
ctg = [
    "{}%".format(cls)
    for i, cls in enumerate(classes[:-1])
] + [
    '{}%'.format(classes[-1])
]
style = {
    'weight': 2,
    'opacity': 1,
    'color': 'white',
    'dashArray': 3,
    'fillOpacity': 0.7,
}
style_handle = assign("""function(feature, context){
    const {classes, colorscale, style, colorprop, data} = context.hideout;
    const departement = feature.properties['code'];

    const value = data[departement]['taux_par_pop'] * 100;                   

    for (let i = 0; i < classes.length; i++) {
        if (value > classes[i]) {
            style.fillColor = colorscale[i];
        }
    }
    return style;
}""")

def get_info(feature=None, json_data=None, year=2016):
    header = [html.H4('Statistiques du crime en ' + str(year))]
    if not feature:
        return header + [html.P(
            'Survolez un département pour afficher les statistiques'
        )]

    crimes = []
    for i, (key, faits) in enumerate(
        json_data[str(year)] \
            [feature['properties']['code']] \
            ['crimes'] \
            .items()
    ):
        crimes += [faits, ' ', key, html.Br()]

    return header + [
        html.B(
            feature['properties']['code'] + \
                '. ' + \
                feature['properties']['nom']
        ),
        html.Br()
    ] + [html.Pre(children=crimes)]

def get_hideout(data, year='2016'):
    return {
        'colorscale': colorscale,
        'classes': classes,
        'style': style,
        'data': data[year],
    }

def get_layers(data):
    # Colorbar widget
    colorbar = dlx.categorical_colorbar(
        categories=ctg,
        colorscale=colorscale,
        width=300,
        height=30,
        position='bottomleft',
    )

    # Map widget
    geojson = dl.GeoJSON(
        url="/assets/departements.json",
        style=style_handle,
        zoomToBounds=True,
        zoomToBoundsOnClick=True,
        hoverStyle=arrow_function({
            'weight':5,
            'color': '#666',
            'dashArray': ''
        }),
        hideout=get_hideout(data=data),
        id='geojson',
    )

    info = html.Div(
        children=get_info(),
        id='info',
        className='info',
        style={
            'position': 'absolute',
            'top': '10px',
            'right': '10px',
            'z-index': '1000',
        }
    )



    annees = [int(i) for i in data]
    slider = dcc.Slider(
        min(annees),
        max(annees),
        1,
        value=min(annees),
        id='slider',
        className='slider_annee',
        marks={i: str(i) for i in annees},
    )

    return colorbar, geojson, info, slider
