import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.dato=""
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="")
        self.label1.grid(columna=0,row=0)

        self.boton1=tk.Button(self.ventana1.text="1",command=self.ingresar1)
        self.boton1.grid(columna=1,row=1)

        self.boton2=tk.Button(self.ventana1.text="2",command=self.ingresar2)
        self.boton2.grid(columna=1,row=1)

        self.boton3=tk.Button(self.ventana1.text="3",command=self.ingresar3)
        self.boton3.grid(columna=2,row=1)

        self.boton4=tk.Button(self.ventana1.text="4",command=self.ingresar4)
        self.boton4.grid(columna=3,row=1)

        self.boton5=tk.Button(self.ventana1.text="5",command=self.ingresar5)
        self.boton5.grid(columna=4,row=1)
        
        self.ventana1.mainloop()

    def ingresar1(self):
        self.dato=self.dato+"-"+self.get()
        self.label1.configure(text=self.dato)
    def ingresar2(self):
        self.dato=self.dato+"-"+self.get()
        self.label1.configure(text=self.dato)
    def ingresar3(self):
        self.dato=self.dato+"-"+self.get()
        self.label1.configure(text=self.dato)
    def ingresar4(self):
        self.dato=self.dato+"-"+self.get()
        self.label1.configure(text=self.dato)
    def ingresar5(self):
        self.dato=self.dato+"-"+self.get()
        self.label1.configure(text=self.dato)
        

ç

        
  
        
