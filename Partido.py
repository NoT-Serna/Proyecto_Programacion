import Jugador as jg

class Partido: 
    def __init__(self):
        self.nombre_local="" # inicializa los nombres de los equipos con un string vacio
        self.nombre_visitante=""
        self.jugadores = []# inicializa una lista de jugadores vacia donde se van a agregar los jugadores que hagan faltas
        self.marcador=[0,0] # inicializa una lista con dos ceros para el marcador
            
    def get_nombre_local(self):
        return self.nombre_local
        
    def get_nombre_visitante(self):
        return self.nombre_visitante
    
    def set_nombre_local(self, new_nombre_local):
        self.nombre_local=new_nombre_local
        
    def set_nombre_visitante(self, new_nombre_visitante):
        self.nombre_visitante=new_nombre_visitante
        
    def agregar_goles_local(self):
        self.marcador[0]+=1 #le suma 1 a los "goles" del equipo local en la variable marcador
    
    def agregar_goles_visitante(self):
        self.marcador[1]+=1#le suma 1 a los "goles" del equipo visitante en la variable marcador
        
    def acceder_goles_local(self):#actua como un getter para acceder a los goles del equipo local
        return self.marcador[0]
        
    def acceder_goles_visitante(self):#actua como un getter para acceder a los goles del equipo visitante
        return self.marcador[1]
    
    def agregar_jugador(self, num_jersey): # actua como un metodo setter pero con un objeto de la clase jugador 
        nuevo_jugador = jg.Jugador(num_jersey)
        self.jugadores.append(nuevo_jugador)# le  agrega el nuevo objeto jugador a la lista de jugadores con sus metodos y atributos
    
    
    def agregar_falta(self, num_jersey):
        jugador_encontrado = False #se crea esta variable para determinar si un jugador se ha encontrado o no(se usara para determinar si no se ha encontrado) y se empieza en false 
        for jugador in self.jugadores:
            if jugador.get_nro_jersey() == num_jersey: #evalua si el nro_jersey ingresado coincide con algun jugador de la lista
                jugador.agregar_falta()
                jugador_encontrado = True
                break #termina la iteracion
        if not jugador_encontrado:#si la variable se mantuvo en falso significa que no se encontro jugador y entonces se muestra que no existe
            print(f"El jugador con jersey #{num_jersey} no existe")
            
    def acceder_faltas(self,num_jersey):
        jugador_encontrado = False #se crea esta variable para determinar si un jugador se ha encontrado o no(se usara para determinar si no se ha encontrado) y se empieza en false 
        for jugador in self.jugadores:
            if jugador.get_nro_jersey() == num_jersey:
                jugador_encontrado = True
                return jugador.get_nro_faltas() # retorna el valor de numero de faltas del jugador
                break
        if not jugador_encontrado:
            print(f"El jugador con jersey #{num_jersey} no existe")
                
    
        
        
        
