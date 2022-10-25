# 25 / 10
import interfaz
import logica

interfaz.reglas()
logica.declararVariables()

while jugando == True :
    logica.verificarGanador()
    interfaz.turnoCirculo()
    logica.verificarTurnoCirculo()
    logica.insertarCirculo()
    interfaz.imprimirTablero()
    logica.verificarGanador()
    interfaz.turnoCruz()
    logica.verificarTurnoCruz()
    logica.insertarCruz()    
    interfaz.imprimirTablero()
