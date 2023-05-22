from pywebio.input import *
from pywebio.output import *

with put_collapse('Despliega el menú con 4 opciones:'):
      for i in range(1, 5, 1):
            put_text("Opcion: ", i)