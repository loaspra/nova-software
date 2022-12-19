"""
Script que muestra las peticiones mandadas por el proceso en la interfaz
"""

# visit http://127.0.0.1:8050/ in your web browser.
import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import json
import redis
import os
import pandas as pd

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


# layout de la aplicacion
def serve_layout():
    return html.Div(
    className="container scalable",
    children=
    [
        html.Div(
            id="banner",
            className="banner",
            children=[
                html.H1("Redis, Celery, and Periodic Updates"),
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
                        dcc.Graph(id="graph"),
                    ]
                ),
                html.Div(
                    id="middle-row",
                    className="row",
                    children=[
                        # dcc.Interval(interval=2 * 1000, id="interval"),
                        dcc.Graph(id="graph2"),
                    ]
                ),
                html.Div(
                    id="bottom-row",
                    className="row",
                    children=[
                        # dcc.Interval(interval=2 * 1000, id="interval"),
                        dcc.Graph(id="graph3"),
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

@app.callback(
    Output("graph", "figure"),
    [Input("interval", "n_intervals")],
)
def update_graph(_):
    df = get_dataframe()
    return {
        "data": [{"x": df["time"], "y": df["value"], "type": "bar"}],
        "layout": {"title": "Test"},
    }

@app.callback(
    Output("graph2", "figure"),
    [Input("interval", "n_intervals")],
)
def update_graph2(_):
    df = get_dataframe()
    return {
        "data": [{"x": df["time"], "y": df["value"], "type": "bar"}],
        "layout": {"title": "Test"},
    }

@app.callback(
    Output("graph3", "figure"),
    [Input("interval", "n_intervals")],
)
def update_graph(_):
    df = get_dataframe()
    return {
        "data": [{"x": df["time"], "y": df["value"], "type": "bar"}],
        "layout": {"title": "Test"},
    }

@app.callback(
    Output("status", "children"),
    [Input("interval", "n_intervals")],
)
def update_status(_):
    data_last_updated = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["DATE_UPDATED"]
    ).decode("utf-8")
    return "Data last updated at {}".format(data_last_updated)


if __name__ == "__main__":
    app.run_server(debug=True)