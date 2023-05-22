import dash
from dash import dcc
from dash import html
import plotly.express as px
import  quandl

df1 = quandl.get("WIKI/GOOGL.4", start_date="2015-1-1", end_date="2018-12-31")
df2 = quandl.get("WIKI/MSFT.4", start_date="2015-1-1", end_date="2018-12-31")

figura = px.line(df1, title="Cotizacion de Google: Enero 2015 - Diciembre 2018")
figura2 = px.line(df2, title="Cotizacion de Microsoft: Enero 2015 - Diciembre 2018")

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children="APLICACIÓN CON DASH PARA MERCADOS FINANCIEROS GOOGLE"),
    dcc.Graph(figure=figura),
    html.H1(children="APLICACIÓN CON DASH PARA MERCADOS FINANCIEROS MICROSOFT"),
    dcc.Graph(figure=figura2)])

if __name__ == "__main__":
    app.run_server(debug=True)
