import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números DESCENDENTES, desde el 1 al 5.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        lista_numeros = list(range(0,5,1))
        for numero in reversed(range (5)):
            mensaje = f"{numero}"
            alert ("resuelto", mensaje)

       
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()