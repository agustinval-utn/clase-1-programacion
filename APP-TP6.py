'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos # maximo
b. nombre y edad del candidato con menos votos # minimo
c. el promedio de edades de los candidatos # promedio
d. total de votos emitidos. # total
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        continuar = True
        flag = 0
        contador = 1
        numeromax = -1
        nombremax = ""
        numeromin = 9999
        todosvotos = 0
        todosvotos = int(todosvotos)
        todosedad = False
        numerocandidatos = False

        while  True:
            nombre = prompt("nombre", "ingresar nombre")
            while (nombre == None or nombre == "") or not nombre.isalpha:
                nombre = prompt ("nombre", "reingresar nombre")

            edad = prompt("edad", "ingrese edad")
            while edad == None or not edad.isdigit:
                    edad = prompt ("edad", "reingrese edad")
                    edad = int(edad)
                    if edad < 25:
                         edad = prompt("reingrese edad", "reingrese edad")

            if todosedad == 0:
                 todosedad = int(edad)
            else:
                 todosedad = todosedad + int(edad)

                    
                
            votos = prompt("votos", "ingrese votos")
            votos = int(votos)
            if todosvotos == False:
                 todosvotos = votos
            else: 
                todosvotos = todosvotos + votos
                 
            if numeromax  < votos:
                 numeromax = votos
                 nombremax = nombre
                 
            if numeromin > votos:
                 numeromin = votos
                 nombremin = nombre

            if numerocandidatos == False:
                 numerocandidatos = 1
            elif numerocandidatos >= 1:
                 numerocandidatos = numerocandidatos + 1

            pregunta = question ("ingresar mas?", "otros candidatos")
            if pregunta == True:
                 contador += 1
                 continue
            else:
                 if pregunta == False:
                      break
            
        numerocandidatos = int(numerocandidatos)
        promedio = todosedad / numerocandidatos
                 
        print(f"{numeromax}  {nombremax}\n"\
              f"{numeromin} {nombremin}\n"\
              f"{promedio}\n"\
              f"{todosvotos}")
              








if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
