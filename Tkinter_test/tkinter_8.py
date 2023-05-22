import tkinter as tk

ventana = tk.Tk()

ventana.title("ubicacioón en la pantalla")
ventana.geometry("500x500")

ventana.resizable(0,0)

tk.Label(ventana, text="label 1", fg="white").place(x=20, y=20)
tk.Label(ventana, text="label 2", fg="blue").place(x=200, y=200)
tk.Label(ventana, text="label 3", fg="green").place(x=400, y=400)

tk.Label(ventana, text="label 4", fg="white").place(x=2000, y=2000)

tk.mainloop()