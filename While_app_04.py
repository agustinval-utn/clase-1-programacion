import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Al presionar el botón ‘Validar número’, mediante prompt solicitar al usuario que ingrese un número. 
Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no coincidir con el rango, 
volverlo a solicitar hasta que la condición se cumpla
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_numero = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_numero_on_click)
        self.btn_validar_numero.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_numero_on_click(self):
        contador = 0
        valormax = 9
        salida_prompt = prompt("numero", "inserte numero")
        salida_prompt = int(salida_prompt)
        while salida_prompt > 9:
            contador += 1
            mensaje = "intente de nuevo"
            if contador == 2:
                break
        else:
            while salida_prompt < 0:
                contador += 1
                mensaje = "intente de nuevo"
                if contador == 2:
                    break
            else: mensaje = "bien hecho"
        alert("resultado", mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()