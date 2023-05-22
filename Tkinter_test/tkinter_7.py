import tkinter as tk

ventana = tk.Tk()

ventana.title("destroy")
ventana.resizable(0,0)
ventana.geometry("500x500")

def _quit():
    ventana.quit()
    ventana.destroy()
    
button = tk.Button(ventana, text="Quit", command=_quit)
button.pack(side=tk.BOTTOM)

tk.mainloop()