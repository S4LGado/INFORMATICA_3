# 25 / 10

def reglas():
  print("BIENVENIDO A JUGAR TRICKY")
  print("REGLAS")
  print("Las posiciones van numeradas del 1 al 9 de la sguiente forma")
  print("1|2|3")
  print("4|5|6")
  print("7|8|9")

def turnoCirculo():
    circulo = int(input("Digite en que posicion colocar el circulo: "))

def turnoCruz():
    cruz = int(input("Digite en que posicion colocar la cruz: "))
    
def imprimirTablero():
    fila1Vista = fila1[0] + '|' + fila1[1] + '|' + fila1[2] 
    fila2Vista = fila2[0] + '|' + fila2[1] + '|' + fila2[2]
    fila3Vista = fila3[0] + '|' + fila3[1] + '|' + fila3[2]
    print(fila1Vista)
    print(fila2Vista)
    print(fila3Vista)