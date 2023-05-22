from pywebio.input import *
from pywebio.output import *
import plotly.express as px

style(put_text('Petal and sepal charts IrisDatasheet'), 'color: blue')


df = px.data.iris()
put_text("Width and length of sepal chart")
fig = px.scatter(df, x="sepal_length", y="sepal_width", 
                    color="species")
html = fig.to_html(include_plotlyjs="require", full_html=False)
put_html(html)

put_text("Width and length of petal char")
fig2 = px.scatter(df, x="petal_length", y="petal_width", 
                     color="species")
html = fig2.to_html(include_plotlyjs="require", full_html=False)
put_html(html)
