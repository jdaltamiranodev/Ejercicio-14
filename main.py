import tkinter

window = tkinter.Tk()

def salir(event):
    window.quit()

def refrescar(event):
    for widget in window.winfo_children():
        if isinstance(widget, tkinter.Radiobutton):
            selected.set(None)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

selected = tkinter.StringVar()
r1 = tkinter.Radiobutton(window, text='Facil', value=1, variable=selected)
r2 = tkinter.Radiobutton(window, text='Medio', value=2, variable=selected)
r3 = tkinter.Radiobutton(window, text='Dificil', value=3, variable=selected)
selected.set(0)

r1.grid(column=0, row=1, pady=15, padx=15)
r2.grid(column=1, row=1, pady=15, padx=15)
r3.grid(column=2, row=1, pady=15, padx=15)

boton = tkinter.Button(window, text='Refrescar')#, command=lambda: refrescar())
boton.grid(column=1, row=2, sticky=tkinter.E, padx=10, pady=10)
boton.bind('<Button-1>', refrescar)

botonSalir = tkinter.Button(window, text='Salir')
botonSalir.grid(column=2, row=2, sticky=tkinter.E, padx=15, pady=15)
botonSalir.bind('<Button-1>', salir)

window.mainloop()