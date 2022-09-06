"""  a) Determine el numero de metodos que tienen los strings, enteros, flotantes, listas, diccionarios,
      b) Determine el tipo de variable resultado de las siguientes operaciones:
         "123" + 3 no tiene solucion
         3 + "123" no tiene solucion
         [] + [] = []
         [1] + [1,2,3] = [1, 1, 2, 3]
         (1,) + (1,2,3) = (1, 1, 2, 3)
         (1,2,3) + (1,) = (1, 1, 2, 3)
         {"a", "b"} | {"c"} = {'a', 'b', 'c'}
         {"a", "b"} & {"a", "c"} = {'a'}
         False and 2 False
         True and 5 True
         False or 0 False
         True or 5 True
         1 and True True""" 

print ({"a", "b"} & {"a", "c"})