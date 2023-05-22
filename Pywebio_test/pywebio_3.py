from optparse import Values
from pywebio.input import *
from pywebio.output import *

textarea('Text Area',
         rows=3,
         placeholder='Escriba su texto aquí...')

textarea('Code Edit',
         code={
               'mode': "python",
               'theme': "dracula",
               },
         value='import pandas as pd\n# Escriba código en Python')
