import interfaz
import logica

interfaz.explicarJuego()
tableroJuego = logica.obtenerTableroLogico()

for turno in range(0,15):
    numero = str(input("Ingerese el numero que desea colocar: "))
    posicion = int(input("Ingrese posicion de juego: "))
    tableroJuego = logica.actualizarTableroLogico(tableroJuego, posicion, numero)
    interfaz.dibujarTablero(tableroJuego)
    posibleGanador = logica.determinarGanador(tableroJuego)
    if posibleGanador:
        print("Felicidades ha ganado el juego ")
    else:
        print("Perdiste")