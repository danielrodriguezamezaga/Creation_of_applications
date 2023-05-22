from pywebio.input import *
from pywebio.output import *

# text Output
put_text("Con put_text realizamos salida de texto")

# table Output
put_table([
      ["Empresa", "Cotización (€)"],
      ["x", "10"],
      ["y", "0.5"],
      ["z", "8.1"],
])

# Markdown
put_markdown("~~Mensaje tachado~~")

# markdown 2
put_markdown("**Mensaje en negrita**")