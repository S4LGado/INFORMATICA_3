class Estudiante:
    def __init__(self,nombre,edad,codigo,notas):
        self.nombre = nombre
        self.edad = edad
        self.codigo = codigo
        self.notas = notas
    
    def calcularPromedio(self):
        promedio = sum(self.notas)/len(self.notas)
        return promedio

    def determinarMejorNota(self):
        mejorNota = max(self.notas)
        return mejorNota

    def determinarPeorNota(self):
        peorNota = min(self.notas)
        return peorNota 

if __name__ == "__main__":
    estudiante1 = Estudiante("Cristian Pachon",20,"019",[5.0,1.0,1.0])
    print(estudiante1.calcularPromedio())
