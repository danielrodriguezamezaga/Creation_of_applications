from pywebio.input import *
from pywebio.output import *

# ventana emergente 2
popup("Título de la ventana emergente",
      [
            put_html("<h1>Contenido en H1</h1>"),
            put_html("<h2>Contenido en H2</h2>"),
            put_html("<h3>Contenido en H3</h3>"),
            put_html("<h4>Contenido en H4</h4>"),
            put_html("<h5>Contenido en H5</h5>"),
            put_html("<h6>Contenido en H6</h6>")
      ])