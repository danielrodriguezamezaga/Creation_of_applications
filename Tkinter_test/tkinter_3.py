import tkinter as tk

ventana = tk.Tk()

ventana.title("Botón contador de clicks")
ventana.resizable(0, 0)
ventana.geometry("500x500")

click = 0
def funcion_click():
    global click
    click +=1
    print("Se han pulsado:", click, " veces")

button = tk.Button(ventana, text="Haga click", fg="white", bg="green", 
                   width=10, height=5, command=funcion_click)
button.pack()

ventana.mainloop()