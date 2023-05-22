from pywebio.input import *
from pywebio.output import *

# es posible usar style() para hacer una salida customizada

style(put_text('Texto emn Azul'), 'color: blue')

put_table([
    [style(put_text('Texto en negro'), 'color: black'),
     style(put_text('Textp en rojo'), 'color: red')],
    
    [style(put_text('Texto en naranja'), 'color: orange'),
     style(put_text('Textp en verde'), 'color: green')],
])