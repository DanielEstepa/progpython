import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.seleccion.set(2)
        self.radio1=tk.Radiobutton(self.ventana1,text="usuario", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=0)
        self.radio2=tk.Radiobutton(self.ventana1,text="contraseña", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="Mostrar seleccionado", command=self.mostrarseleccionado)
        self.boton1.grid(column=0, row=2)
        self.label1=tk.Label(self.ventana1,text="opcion seleccionada")
        self.label1.grid(column=0, row=3)

        self.boton1=tk.Button(self.ventana1,text="Acceso", command=self.acceder)
        self.boton1.grid(columna=0, row=2)
        self.label2=tk.Label(self.ventana1, text="")
        self.label2.grid(columna=0, row=3)
        self.ventana1.mainloop()

    def acceder(self):
        valor=self.dato.get()
        valor1=self.dato1-get()
        if valor=="Juan" and valor1=="abc123"
            self.label3.configure(text="correcto")
        else:
            self.label3.configure(text="Incorrecto")

aplicacion1=Aplicacion()
  
