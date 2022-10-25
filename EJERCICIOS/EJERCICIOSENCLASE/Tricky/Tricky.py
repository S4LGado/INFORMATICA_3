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
circulo = 0
cruz = 0
jugando = True
ganaCirculo = False
ganaCruz = False
while jugando:
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
    break
  if ganaCruz:
    print("Gana Cruz")
    break
  circulo = int(input("Digite en que posicion colocar el circulo: "))
  if circulo in [1,2,3]:
      if fila1[circulo-1] in ['X','O'] :
          print('Posicion no valida')
          circulo = int(input("Digite en que posicion colocar el circulo: "))
  if circulo in [4,5,6]:
      if fila2[circulo-4] in ['X','O'] :
          print('Posicion no valida')
          circulo = int(input("Digite en que posicion colocar el circulo: "))
  if circulo in [7,8,9]:
      if fila3[circulo-7] in ['X','O'] :
          print('Posicion no valida')
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
  fila1Vista = fila1[0] + '|' + fila1[1] + '|' + fila1[2] 
  fila2Vista = fila2[0] + '|' + fila2[1] + '|' + fila2[2]
  fila3Vista = fila3[0] + '|' + fila3[1] + '|' + fila3[2]
  print(fila1Vista)
  print(fila2Vista)
  print(fila3Vista)
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
    break
  if ganaCruz:
    print("Gana Cruz")
    break
  cruz = int(input("Digite en que posicion colocar la cruz: "))
  if cruz in [1,2,3]:
      if fila1[cruz-1] in ['X','O'] :
          print('Posicion no valida')
          cruz = int(input("Digite en que posicion colocar la cruz: "))
  if cruz in [4,5,6]:
      if fila2[cruz-4] in ['X','O'] :
          print('Posicion no valida')
          cruz = int(input("Digite en que posicion colocar la cruz: "))      
  if cruz in [7,8,9]:
      if fila3[cruz-7] in ['X','O'] :
          print('Posicion no valida')
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
  fila1Vista = fila1[0] + '|' + fila1[1] + '|' + fila1[2] 
  fila2Vista = fila2[0] + '|' + fila2[1] + '|' + fila2[2]
  fila3Vista = fila3[0] + '|' + fila3[1] + '|' + fila3[2]
  print(fila1Vista)
  print(fila2Vista)
  print(fila3Vista)