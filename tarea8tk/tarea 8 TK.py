import tkinter as tk
from tkinter import ttk

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.label0=ttk.Label(self.ventana1, text="Nombre")
        self.label0.grid(column=0,row=0)
        self.opcion=tk.StringVar()
        self.entry1=tk.entry(self.ventana1,width=20,textvariable=self,dato1)
        self.entry1.grid(column=1,row=0)
        self.label1.ttk.label(self.ventana1,text="Seleccione un pais")
        self.label1.grid(column=1,row=1)
        self.opcion=tk.StraingVaR()
        paises=("Francia","España","Alemania","Italia","Grecia","Holanda")
        self.combobox1=ttk.Combobox(self.ventana1, 
            width=10, 
            textvariable=self.opcion, 
            values=diassemana)
        self.combobox1.current(0)
        self.combobox1.grid(column=1, row=2)
        self.boton1=tk.Button(self.ventana1, text="visualizar", command=self.recuperar)
        self.label2.grid(column=1, row=3)
        self.label2=ttk.Label(self.ventana1, text="valores")
        self.label2.grid(column=0, row=4)
        self.ventana1.mainloop()

    def recuperar(self):
        self.label2.configure(text="Valores:"*self.dato1.get()+"-"+self.opcion.get())

aplicacion1=Aplicacion()
