from pywebio.input import *
from pywebio.output import *


# radio
radio("Selecciona un framework GUI <radio button> :",
      options=["PyQT", "Tkinter"])

# checkbox
checkbox("¿Conoces el Framework Dash?",
         options=["SI", "NO"])

# select
select("Selecciona un Framework <select> :",
       ["Django", "Streamlit", "PyWebIO"])