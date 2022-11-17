class Estudiante:
    def __init__(self,nombre,edad,codigo,notas):
        self.nombre = nombre
        self.edad = edad
        self.codigo = codigo
        self.notas = notas
    
    def calcularPromedio(self):
        promedio = round(sum(self.notas)/len(self.notas),2)
        return promedio

    def determinarMejorNota(self):
        mejorNota = max(self.notas)
        return mejorNota

    def determinarPeorNota(self):
        peorNota = min(self.notas)
        return peorNota 

class Curso:
    def __init__(self,nombre_curso,nombre_profesor,estudiantes):
        self.nombre_curso = nombre_curso
        self.nombre_profesor = nombre_profesor
        self.estudiantes = estudiantes

    def calcularMediaDelCurso(self):
        media = 0
        for i in range (0,len(self.estudiantes)):
            media = media + self.estudiantes[i].calcularPromedio()

        media = media / len (self.estudiantes)    
        return media
    
    def determinarAprobados(self):
        diccionarioDefinitiva = {}
        for i in range(0,len(self.estudiantes)):
            diccionarioDefinitiva[self.estudiantes[i].nombre] = self.estudiantes[i].calcularPromedio()
        diccionarioAprobados = {}
        diccionarioReprobados = {}
        for estudiante in diccionarioDefinitiva.keys():
            if diccionarioDefinitiva[estudiante] >= 3.0:
                diccionarioAprobados[estudiante] = 'Aprueba'
            else: 
                diccionarioReprobados[estudiante] = 'No Aprueba'
        return diccionarioAprobados, diccionarioReprobados
            
if __name__ == "__main__":
    estudiante1 = Estudiante("Cristian Pachon",20,"019",[5.0,1.0,1.0])
    estudiante2 = Estudiante("Juan Salgado",21,"020",[5.0,5.0,5.0])
    estudiante3 = Estudiante("Terminator",24,"021",[4.0,2.5,3.0])
    listaEstudiantes = [estudiante1,estudiante2,estudiante3]
    
    curso1 = Curso("Informatica","Cristian Pachon",listaEstudiantes)

    print(curso1.calcularMediaDelCurso())
    print(curso1.determinarAprobados())
