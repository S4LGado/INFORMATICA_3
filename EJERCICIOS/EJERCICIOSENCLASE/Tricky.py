#18/10

print("BIENVENIDO A JUGAR TRICKY")
print("REGLAS")
print("Las posiciones van numeradas del 1 al 9 de la sguiente forma")
print("1|2|3")
print("4|5|6")
print("7|8|9")
fila1 = [" "," " ," "]
fila2 = [" "," " ," "]
fila3 = [" "," " ," "]
juego = [fila1,fila2,fila3]
circulo = 0
cruz = 0
jugando = True
ganaCirculo = False
ganaCruz = False
chuza = 0
chuza1 = 0
chuza2 = 0
chuza3 = 0
chuza4 = 0
chuza5 = 0
while jugando:
  for fila in juego:
    if fila[0] == "O":
      chuza = chuza + 1
      if chuza == 3:
        ganaCirculo = True
    if fila[1] == "O":
      chuza1 = chuza1 + 1
      if chuza1 == 3:
        ganaCirculo = True
    if fila[2] == "O":
      chuza2 = chuza2 + 1
      if chuza2 == 3:
        ganaCirculo = True
    if fila == ["O","O","O"]:
      ganaCirculo = True      
    if fila[0] == "X":
      chuza3 = chuza3 + 1
      if chuza3 == 3:
        ganaCruz = True
    if fila[1] == "X":
      chuza4 = chuza4 + 1
      if chuza4 == 3:
        ganaCruz = True
    if fila[2] == "X":
      chuza5 = chuza5 + 1
      if chuza5 == 3:
        ganaCruz = True
    if fila == ["X","X","X"]:
      ganaCruz = True
    if ganaCruz:
      print("Gana Cruz")
      break
    if ganaCirculo:
      print("Gana Circulo")
      break
  circulo = int(input("Digite en que posicion colocar el circulo: "))
  if circulo in [1,2,3]:
    fila1.pop(circulo-1)
    fila1.insert(circulo-1,"O")
  if circulo in [4,5,6]:
    fila2.pop(circulo-4)
    fila2.insert(circulo-4, "O")
  if circulo in [7,8,9]:
    fila3.pop(circulo-7)
    fila3.insert(circulo-7, "O") 
  print(fila1)
  print(fila2)
  print(fila3)
  cruz = int(input("Digite en que posicion colocar la cruz: "))
  if cruz in [1,2,3]:
    fila1.pop(cruz-1)
    fila1.insert(cruz-1,"X")
  if cruz in [4,5,6]:
    fila2.pop(cruz-4)
    fila2.insert(cruz-4, "X")
  if cruz in [7,8,9]:
    fila3.pop(cruz-7)
    fila3.insert(cruz-7, "X") 
  print(fila1)
  print(fila2)
  print(fila3)