def obtenerTableroLogico():
    tableroLogico = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    return tableroLogico

def actualizarTableroLogico(tableroLogico, posicion, caracter):
    tableroLogico[posicion] = caracter
    return tableroLogico

def determinarGanador(tableroLogico):
    gana = None
    a = False
    b = False 
    c = False
    d = False
    e = False
    f = False 
    g = False
    h = False
    if tableroLogico[0] != None and tableroLogico[1] != None and tableroLogico[2] != None and tableroLogico[3] != None and tableroLogico[4] != None and tableroLogico[5] != None and tableroLogico[6] != None and tableroLogico[7] != None and tableroLogico[8] != None and tableroLogico[9] != None and tableroLogico[10] != None and tableroLogico[11] != None and tableroLogico[12] != None and tableroLogico[13] != None and tableroLogico[14] != None and tableroLogico[15] != None:
        if tableroLogico[0] != tableroLogico[4] and tableroLogico[0] != tableroLogico[8] and tableroLogico[0] != tableroLogico[12]:
            a = True
        if tableroLogico[0] != tableroLogico[1] and tableroLogico[0] != tableroLogico[2] and tableroLogico[0] != tableroLogico[3]:
            b = True
        if tableroLogico[4] != tableroLogico[5] and tableroLogico[4] != tableroLogico[6] and tableroLogico[4] != tableroLogico[7]:
            c = True
        if tableroLogico[8] != tableroLogico[9] and tableroLogico[8] != tableroLogico[10] and tableroLogico[8] != tableroLogico[11]:
            d = True
        if tableroLogico[12] != tableroLogico[13] and tableroLogico[12] != tableroLogico[14] and tableroLogico[12] != tableroLogico[15]:
            e = True
        if tableroLogico[1] != tableroLogico[5] and tableroLogico[1] != tableroLogico[9] and tableroLogico[1] != tableroLogico[13]:
            f = True   
        if tableroLogico[2] != tableroLogico[6] and tableroLogico[2] != tableroLogico[10] and tableroLogico[2] != tableroLogico[14]:
            g = True
        if tableroLogico[3] != tableroLogico[7] and tableroLogico[3] != tableroLogico[11] and tableroLogico[3] != tableroLogico[15]:
            h = True 
        if a and b and c and d and e and f and g and h:
            gana = True
    return gana