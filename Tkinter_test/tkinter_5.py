import tkinter as tk

ventana = tk.Tk()

def funcion_usuarios():
    print("Nombre: ", e1.get(), "- Apellido:", e2.get())
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

tk.Label(ventana, text="Ingrese Nombre y Apellido").grid(row=1, column=0)
tk.Label(ventana, text=" Nombre ").grid(row=2, column=0)
tk.Label(ventana, text=" Apellido").grid(row=3, column=0)


e1 = tk.Entry(ventana)
e1.insert(0, "")
e1.grid(row=2, column=1)

e2 = tk.Entry(ventana)
e2.insert(0, "")
e2.grid(row=3, column=1)

tk.Button(ventana, text="Mostrar",
          fg="white", bg="blue", command=funcion_usuarios).grid(row=4, column=0)

ventana.mainloop()