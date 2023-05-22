import dash
from dash import html

#creamos nuestra aplicacion

app = dash.Dash()
app.layout = html.Div("Mi primera aplicación Dash")

if __name__ == "__main__":
    app.run_server(debug=True)