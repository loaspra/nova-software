"""
servidor-web.py

Script que muestra las peticiones mandadas por el proceso en la interfaz

El trabajo para ahora (25 octubre) es desde la linea 
"""
# para ver la interfaz:
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

"""
Codigo de ejemplo
"""
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# figura (grafico de barras)
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

"""
la distribucion de la interfaz se lleva a cabo usando componentes HTML
  como divs, las graficas se manejan con la libreria Dash.dcc (dash core 
  components: https://dash.plotly.com/dash-core-components/graph)
"""
app.layout = html.Div(children=[
    # header de la app
    html.H1(children='Hello Dash'),
    # subtitulo
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    # grafico
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)