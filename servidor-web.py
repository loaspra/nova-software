"""
Script que muestra las peticiones mandadas por el proceso en la interfaz

Para el mapa
https://plotly.com/python/scattermapbox/

"""

# visit http://127.0.0.1:8050/ in your web browser.
import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import json
import redis
import pandas as pd
from datetime import datetime

import plotly.express as px

import plotly.graph_objs as go

# este es el script que inserta datos artificiales a redis
import tasks

app = dash.Dash("cansat-ui")
server = app.server

# initialize the data when the app starts
tasks.update_data()

# connect with redis-server
# en mi caso, el server esta corriendo en WSL

REDIS_URL = "redis://127.0.0.1:6379"
redis_instance = redis.StrictRedis.from_url(REDIS_URL)


"""
Layout the la aplicacion web
"""
def serve_layout():
    return html.Div(
    className="container scalable",
    children=
    [
        html.Div(
            id="banner",
            className="banner",
            children=[
                html.H1("Historico de datos recolectados"),
                html.Div(id="status"),
            ]
        ),
        dcc.Interval(interval=2 * 1000, id="interval"),
        html.Div(
            className="app_main_content",
            children=[
                html.Div(
                    id="top-row",
                    className="row",
                    children=[
                        html.Div(id="temperatura graph",
                                className="six columns",
                                children=[
                                        dcc.Graph(id="graph_temperatura", style={'width': '90vh', 'height': '45vh'})
                                    ]
                                ),
                                html.Div(id="pressure graph",
                                className="six columns",
                                children=[
                                        dcc.Graph(id="graph_pressure", style={'width': '90vh', 'height': '45vh'})
                                    ]
                                )]),
                        # dcc.Graph(id='my-graph',style={'width': '90vh', 'height': '90vh'})
                html.Div(
                    id="bottom-row",
                    className="row",
                    children=[
                        # dcc.Interval(interval=2 * 1000, id="interval"),
                        dcc.Graph(id="graph_humidity", style={'height': '45vh'}),
                    ]
                ),
            ]
        )
    ]
)


app.layout = serve_layout


def get_dataframe():
    """Retrieve the dataframe from Redis
    This dataframe is periodically updated through the redis task
    """
    jsonified_df = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["DATASET"]
    ).decode("utf-8")
    df = pd.DataFrame(json.loads(jsonified_df))
    return df


# Actualizar los datos de los graficos 
# Pressure 
@app.callback(
    Output("graph_pressure", "figure"),
    [Input("interval", "n_intervals")],
)
def update_graph_pressure(_):
    df = get_dataframe()
    fig = px.bar(df, x=df.index, y="temperatura", barmode="group")
    fig.update_layout(
        margin=dict(l=5, r=15, t=10, b=10),
    )
    return fig

# temperatura
@app.callback(
    Output("graph_temperatura", "figure"),
    [Input("interval", "n_intervals")],
)
def update_graph_temperatura(_):
    df = get_dataframe()
    fig = px.bar(df, x=df.index, y="temperatura", barmode="group")
    fig.update_layout(
        margin=dict(l=5, r=15, t=10, b=10),
    )
    return fig

# Humidity
@app.callback(
    Output("graph_humidity", "figure"),
    [Input("interval", "n_intervals")],
)
def update_graph_humidity(_):
    df = get_dataframe()
    fig = px.bar(df, x=df.index, y="temperatura", barmode="group")
    fig.update_layout(
        margin=dict(l=5, r=15, t=10, b=10),
    )
    return fig

# Status (not touch)
@app.callback(
    Output("status", "children"),
    [Input("interval", "n_intervals")],
)
def update_status(_):
    return "Last update at {}".format(datetime.now())


if __name__ == "__main__":
    app.run_server(debug=True)