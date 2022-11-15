# 15 - 11 - 2022

class Curso:
    def __init__(self,nombre_curso,nombre_profesor,estudiantes):
        self.nombre_curso = nombre_curso
        self.nombre_profesor = nombre_profesor
        self.estudiantes =  estudiantes

    def calcularMediaDelCurso(self):
        mediaDelCurso = {}
        estudiantes = self.estudiantes
        for i in estudiantes.keys:
            mediaDelCurso[i]= sum(estudiantes[i])/len(estudiantes[i])
        return mediaDelCurso
    
    def determinarAprobados(self):
        mediaDelCurso = self.mediaDelCurso
        Aprobados = []


