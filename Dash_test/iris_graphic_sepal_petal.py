import dash
from dash import dcc
from dash import html
import plotly.express as px

df = px.data.iris()

figura = px.scatter(df, x="sepal_length", y="sepal_width", color="species")
figura2 = px.scatter(df, x="petal_length", y="petal_width", color="species")

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children="Gráfica del Iris Dataset para el Sépalo (Largo-Ancho)"),
    dcc.Graph(figure=figura),
    html.H1(children="Gráfica del Iris Dataset para el Pétalo (Largo-Ancho)"),
    dcc.Graph(figure=figura2)])

if __name__ == "__main__":
    app.run_server(debug=True)
