import tkinter as tk
from tkinter import messagebox
import random

class JuegoGato4x4:
    def __init__(self, root): #Metodo constructor que inicializa el objeto
        self.root = root #Referencia a la ventana  principal de tkinter
        self.root.title("Juego de Gato 4x4")
        self.tablero = [[None]*4 for _ in range(4)] #Matriz 4x4 que representan el estado del tablero, las cedas se inicializan en cadenas vacias
        self.turno = "X" #X empieza el juego, variable que indica el turno del jugador actual
        self.boton_tablero = [[None]*4 for _ in range(4)] #Matriz para almacenar los botones de la interfaz grafica
        self.crear_tablero() #llamada a un metodo para crear la interfaz grafica del tablero

    def crear_tablero(self):
        for fila in range(4):
            for columna in range(4):
                boton = tk.Button(self.root, text = "", font = ("Arial", 20), width=5, height=5,
                                  command=lambda f=fila, c=columna: self.hacer_movimientos(f,c)) #Crea un boton para cada celda del tablero
                #font (define el estilo y tamano de la fuente)
                #widht, height (define el tamanio del boton)
                #command=lambda f=fila, c=columna: self.hacer_movimientos(f,c) (define la accion a realizar cuando se hace clic. Usa lambda para pasar las coordenadas de la celda al metodo 'hacer movimiento')
                boton.grid(row=fila, column=columna) #Posiciona el boton en la cuadricula
                self.boton_tablero[fila][columna] = boton #Guarda la referencia al boton  en la matriz

    def hacer_movimientos(self, fila, columna):
        if not self.tablero[fila][columna] and self.turno == "X":#verifica si la celda esta vacia y es el turno del jugador X
            self.tablero[fila][columna] = "X"#actualiza el estado del tablero
            self.boton_tablero[fila][columna].config(text="X")#actualizael texto del boton
            if self.comprobar_ganador("X"):#verifica si el jugador X ha ganado
                self.mostrar_mensaje("Jugador X gana!")
                return
            if self.tablero_lleno():#verifica si el tablero esta lleno
                self.mostrar_mensaje("Empate!")
                return
            self.turno = "O"
            self.movimiento_computadora() #Hace que la computadora haga un movimiento
            if self.comprobar_ganador("O"):#verifica si la computadora ha ganado
                self.mostrar_mensaje("Computadora gana!")
            elif self.tablero_lleno():#verifica si el tablero esta lleno
                self.mostrar_mensaje("Empate!")

    def movimiento_computadora(self):
        celdas_vacias = [(fila, columna) for fila in range(4) for columna in range(4) if not self.tablero[fila][columna]] #lista de todas las celdas vacias
        if celdas_vacias:
            fila, columna = random.choice(celdas_vacias)#elije una celda vacia al azar
            self.tablero[fila][columna] = "O"
            self.boton_tablero[fila][columna].config(text="O")#actualiza el texto de la celda
            self.turno = "X" #cambia turno al jugador X

    def comprobar_ganador(self, jugador):
        for fila in range(4):
            if all(self.tablero[fila][columna]== jugador for columna in range(4)):#revisa cada fila para ver si todas las celdas son iguales al jugador actual
                return True
        for columna in range(4):
            if all(self.tablero[fila][columna] == jugador for fila in range(4)):#revisa cada columna para ver si todas las celdas son iguales al jugador actual
                return True
        if all(self.tablero[i][i] == jugador for i in range(4)):#revisa las dos diagonales principales
            return True
        if all(self.tablero[i][3-i] == jugador for i in range(4)):
            return True#retorna True si el jugador ha ganado
        return False#retorna false si el jugador no ha ganado
    
    def tablero_lleno(self):#verifica si todas las celdas del tablero estan ocupadas
        return all(self.tablero[fila][columna] for fila in range(4) for columna in range(4))#retorna True si no hay celdas vacias
    
    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Juego Terminado", mensaje)
        self.root.quit() #Cierra la aplicacion despues de mostrar el mensaje
    
if __name__ == "__main__":
    root = tk.Tk()#crea una nueva ventana de tkinter
    juego = JuegoGato4x4(root)#crea una nueva instancia del juego
    root.mainloop()#inicia el bucle principal de tkinter, mostrando la ventana del juego y manejando eventos
        