from pywebio.input import *
from pywebio.output import *

put_row([
    put_column([
        put_code('ELEMENTO DE LA FILA 1 COLUMNA 1'), None,
        put_row([
            put_code('Fila añadida 2 - Texto 1'), None,
            put_code('Fila añadida 2 - Texto 2'), None,
            put_code('Fila añadida 2 - Texto 3'),
        ])
    ])
])
put_row([
    put_column([
        put_code('ELEMENTO DE FILA 3 COLUMNA 1'), None,
        put_row([
            put_code('Fila añadida 4 - Texto 1'), None,
            put_code('Fila añadida 4 - Texto 2'), None,
            put_code('Fila añadida 4 - Texto 3'),
        ])
    ])
])
