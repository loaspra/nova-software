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


def serve_layout():
    return html.Div(
        [
            dcc.Interval(interval=2 * 1000, id="interval"),
            html.H1("Redis, Celery, and Periodic Updates"),
            html.Div(id="status"),
            dcc.Graph(id="graph"),
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


@app.callback(
    Output("graph", "figure"),
    [Input("dropdown", "value"), Input("interval", "n_intervals")],
)
def update_graph(value, _):
    df = get_dataframe()

    return {
        "data": [{"x": df["time"], "y": df["value"], "type": "bar"}],
        "layout": {"title": value},
    }


@app.callback(
    Output("status", "children"),
    [Input("dropdown", "value"), Input("interval", "n_intervals")],
)
def update_status(value, _):
    data_last_updated = redis_instance.hget(
        tasks.REDIS_HASH_NAME, tasks.REDIS_KEYS["DATE_UPDATED"]
    ).decode("utf-8")
    return "Data last updated at {}".format(data_last_updated)


if __name__ == "__main__":
    app.run_server(debug=True)