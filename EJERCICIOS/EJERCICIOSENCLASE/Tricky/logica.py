# 25 / 10
"""
Este modulo contiene las funciones logicas del juego:
* declararVariables() => retorna las variables necesarias para el juego
* ganaCirculo() => retorna un booleano True si gana Circulo
* ganaCruz() => retorna un booleano True si gana Cruz
* verificarGanador() => Entrega un Booleano dependiendo del ganador
* verificarPosicionCirculo() => Verifica que la posicion sea valida
* verificarPosicionCruz() => Verifica que la posicion sea valida
* insertarCirculo() => altera las filas para poner el circulo en la posicion dada
* insertarCruz() => altera las filas para poner la cruz en la posicion dada
"""
import interfaz

def declararVariables():
    fila1 = [" "," " ," "]
    fila2 = [" "," " ," "]
    fila3 = [" "," " ," "]
    circulo = 0
    cruz = 0
    jugando = True
    ganaCirculo = False
    ganaCruz = False

def ganaCirculo():
    ganaCirculo = True

def ganaCruz():
    ganaCruz = True

def verificarGanador():
    if fila1[0] == "O" and fila2[0] == "O" and fila3[0] == "O":
      ganaCirculo = True
    if fila1[1] == "O" and fila2[1] == "O" and fila3[1] == "O":   
      ganaCirculo = True
    if fila1[2] == "O" and fila2[2] == "O" and fila3[2] == "O":   
      ganaCirculo = True
    if fila1 == ["O","O","O"]:
      ganaCirculo = True
    if fila2 == ["O","O","O"]:
      ganaCirculo = True
    if fila3 == ["O","O","O"]:
      ganaCirculo = True
    if fila1[0] == "O" and fila2[1] == "O" and fila3[2] == "O":
      ganaCirculo = True  
    if fila1[2] == "O" and fila2[1] == "O" and fila3[0] == "O":
      ganaCirculo = True
    if fila1[0] == "X" and fila2[0] == "X" and fila3[0] == "X":
      ganaCruz = True
    if fila1[1] == "X" and fila2[1] == "X" and fila3[1] == "X":   
      ganaCruz = True
    if fila1[2] == "X" and fila2[2] == "X" and fila3[2] == "X":   
      ganaCruz = True
    if fila1 == ["X","X","X"]:
      ganaCruz = True
    if fila2 == ["X","X","X"]:
      ganaCruz = True
    if fila3 == ["X","X","X"]:
      ganaCruz = True
    if fila1[0] == "X" and fila2[1] == "X" and fila3[2] == "X":   
      ganaCruz = True
    if fila1[2] == "X" and fila2[1] == "X" and fila3[0] == "X":   
      ganaCruz = True
    if ganaCirculo:
        print("Gana Circulo") 
        jugando = False
    if ganaCruz:
        print("Gana Cruz")
        jugando = False

def verificarPosicionCirculo():
    if circulo in [1,2,3]:
        if fila1[circulo-1] in ['X','O'] :
            print('Posicion no valida')
            interfaz.turnoCirculo()
    if circulo in [4,5,6]:
        if fila2[circulo-4] in ['X','O'] :
            print('Posicion no valida')
            interfaz.turnoCirculo()        
    if circulo in [7,8,9]:
        if fila3[circulo-7] in ['X','O'] :
            print('Posicion no valida')
            interfaz.turnoCirculo()

def verificarPosicionCruz():
    if cruz in [1,2,3]:
        if fila1[cruz-1] in ['X','O'] :
            print('Posicion no valida')
            interfaz.turnoCruz()
    if cruz in [4,5,6]:
        if fila2[cruz-4] in ['X','O'] :
            print('Posicion no valida')
            interfaz.turnoCruz()        
    if cruz in [7,8,9]:
        if fila3[cruz-7] in ['X','O'] :
            print('Posicion no valida')
            interfaz.turnoCruz()

def insertarCirculo():
    if circulo in [1,2,3]:
        fila1.pop(circulo-1)
        fila1.insert(circulo-1,"O")
    if circulo in [4,5,6]:
        fila2.pop(circulo-4)
        fila2.insert(circulo-4, "O")
    if circulo in [7,8,9]:
        fila3.pop(circulo-7)
        fila3.insert(circulo-7, "O") 

def insertarCruz():
    if cruz in [1,2,3]:
        fila1.pop(cruz-1)
        fila1.insert(cruz-1,"X")
    if cruz in [4,5,6]:
        fila2.pop(cruz-4)
        fila2.insert(cruz-4, "X")
    if cruz in [7,8,9]:
        fila3.pop(cruz-7)
        fila3.insert(cruz-7, "X") 