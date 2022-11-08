# 08 - 11 - 2022

"""
Crear una clase llamada ComidaColombiana
atributos: componente1, componente2, componente3
métodos: nutrir y provocar
"""

class ComidaColombiana: 
    def __init__(self,ingrediente1, ingrediente2, ingrediente3):
        self.ingrediente1 = ingrediente1
        self.ingrediente2 = ingrediente2
        self.ingrediente3 = ingrediente3
    
    #para crear metodos (funciones)
    def provocar(self,opcion):
        if opcion in ["huele bien","se ve bien","tengo hambre"]:
            return "Este alimento provoca"
        else: 
            return "Este alimento no provoca"
    
    def nutrir(self,opcion):
        if opcion in ["estoy enfermo","tengo nauseas","el doctor me prohibio"]:
            return "Este alimento no me puede nutrir"
        else:
            return "Este alimento me nutre"

# Como creo el objeto

bandejaPaisa = ComidaColombiana("chorizo","arepa","arroz")
sancochoDeGallina = ComidaColombiana("gallina","papa","caldo")
ajiacoSantafereño = ComidaColombiana("arracacha","papa","pollo")

print(isinstance(bandejaPaisa, ComidaColombiana)) # isinstance pregunta si un elemento si pertenece a una clase

# Como acceder a los atributos de un objeto
atributo1Bandeja = bandejaPaisa.ingrediente1
atributo2sancocho = sancochoDeGallina.ingrediente2
atributo3Ajiaco = ajiacoSantafereño.ingrediente3

print("atributos ==>", atributo1Bandeja,atributo2sancocho,atributo3Ajiaco)

# Como acceder a los metodos de un objeto

print(ComidaColombiana.__dict__) # da la posibilidad de ver las funciones que tiene una clases

salida1 = bandejaPaisa.provocar("tengo hambre")
print(salida1)