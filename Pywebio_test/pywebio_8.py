from pywebio.input import *
from pywebio.output import *
import pywebio

def funcion_click(valor_boton):
      if valor_boton == "Java" or valor_boton == "C++":
            put_text(valor_boton, ": es un buen Lenguaje de Programacion")
      else:
            #python
            put_text(valor_boton, ": es absolutamente impresionante!")

put_buttons(['Python', 'C++', 'Java'], onclick=funcion_click)

pywebio.session.hold()