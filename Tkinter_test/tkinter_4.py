from ssl import VerifyMode
import tkinter as tk

ventana = tk.Tk()

ventana.title("Checkbutton y label")
ventana.resizable(0,0)
ventana.geometry("500x500")


def funcion_opcion():
    print("Variable 1:", v1.get(), "- Variable 2", v2.get(), "- Variable 3:", v3.get())
    
tk.Label(ventana, text="Elija la opción que desee")

v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.IntVar()
tk.Checkbutton(ventana, text="Opcion 1", variable=v1).grid(row=0, column=0)
tk.Checkbutton(ventana, text="Opcion 2", variable=v2).grid(row=0, column=1)
tk.Checkbutton(ventana, text="Opcion 3", variable=v3).grid(row=0, column=2)

tk.Button(ventana,text="Mostrar las opciones elegidas",
          fg="white", bg="blue", command=funcion_opcion).grid(row=0, column=3)

ventana.mainloop()