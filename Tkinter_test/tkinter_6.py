from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
import pandas as pd

ventana = tk.Tk()
ventana.title("Embendding in Tk")
df = pd.DataFrame({"x":[0,1,2,3,4], "y": [10,15,5,25,30]})

figura = Figure(figsize=(6, 4))
figura.add_subplot(111).plot(df.y)

canvas = FigureCanvasTkAgg(figura, ventana)
canvas.draw()
canvas.get_tk_widget().pack()

toolbar = NavigationToolbar2Tk(canvas, ventana)
toolbar.update()
canvas.get_tk_widget().pack()

tk.mainloop()