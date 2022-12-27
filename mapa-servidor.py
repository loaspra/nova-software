import dash
from dash import dcc, html
import pandas as pd
import numpy as np

from dash.dependencies import Input, Output
from plotly import graph_objs as go
from plotly.graph_objs import *
from datetime import datetime as dt
from collections import deque
import time,random
from multiprocessing import Process

global ref, trayectory

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
)
app.title = "Nova Map"
server = app.server

# Plotly nova token
mapbox_access_token = "pk.eyJ1IjoibWFudTMwIiwiYSI6ImNsYWJnOXQweTAwNGMzdnA3dW5kdWN3bmgifQ.U65wFy0SVIWlRtqbbofR3g"

list_of_locations = {
    "Chipoco": {"lat": -12.138162, "lon": -77.023454},
    "UTEC": {"lat": -12.135117, "lon": -77.022180},
    "Las Palmas": {"lat": -12.161567, "lon": -76.999232},
}

ref = list_of_locations["Chipoco"]
trayectory = [[ref["lat"], ref["lon"]]]


####################################################################3
app.layout = html.Div(
    children=[
        dcc.Graph(id="map-graph", animate = True),
        dcc.Interval(
            id = 'graph-update',
            interval = 500,
            ),
    ]
)
######################################################################
@app.callback(Output("map-graph", "figure"),
              [Input("graph-update", "n_intervals")])

def update_graph(input_data):
    global ref, trayectory
    ref["lat"] += random.randint(-10,10)*0.0001
    ref["lon"] += random.randint(-10,10)*0.0001
    trayectory.append([ref["lat"], ref["lon"]])
    array = np.array(trayectory)
    x = list(array[:,0])
    y = list(array[:,1])
                
    return go.Figure(
        data=[
            # Data for all rides based on date and time
            Scattermapbox(
                lat= x,
                lon= y,
                mode="markers",
                hoverinfo="lat+lon+text",
               
            ),
            # Plot of important locations on the map
            Scattermapbox(
                lat=[list_of_locations[i]["lat"] for i in list_of_locations],
                lon=[list_of_locations[i]["lon"] for i in list_of_locations],
                mode="markers",
                hoverinfo="text",
                text=[i for i in list_of_locations],
                marker=dict(size=8, color="#ffa0a0"),
            ),
        ],
        layout=Layout(
            autosize=True,
            margin=go.layout.Margin(l=0, r=35, t=0, b=0),
            showlegend=False,
            mapbox=dict(
                accesstoken=mapbox_access_token,
                center=dict(lat=ref["lat"], lon=ref["lon"]),  # 40.7272  # -73.991251
                style="dark",
                bearing=0,
                zoom=15,
            ),
            updatemenus=[
                dict(
                    buttons=(
                        [
                            dict(
                                args=[
                                    {
                                        "mapbox.zoom": 15,
                                        "mapbox.center.lon": str(ref["lon"]),
                                        "mapbox.center.lat": str(ref["lat"]),
                                        "mapbox.bearing": 0,
                                        "mapbox.style": "dark",
                                    }
                                ],
                                label="Update",
                                method="restyle",
                            )
                        ]
                    ),
                    direction="left",
                    pad={"r": 0, "t": 0, "b": 0, "l": 0},
                    showactive=False,
                    type="buttons",
                    x=0.45,
                    y=0.02,
                    xanchor="left",
                    yanchor="bottom",
                    bgcolor="#323130",
                    borderwidth=1,
                    bordercolor="#6d6d6d",
                    font=dict(color="#FFFFFF"),
                )
            ],
        ),
    )

if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=False)
    

