import Jugador as jg


#nombre de equipos

class Partido:#partido comentar todo el codigo estas son las logicas 
    def __init__(self):
        self.nombre_local=""
        self.nombre_visitante=""
        self.jugadores = []
        self.marcador=[0,0]
            
    def get_nombre_local(self):
        return self.nombre_local
        
    def get_nombre_visitante(self):
        return self.nombre_visitante
    
    def set_nombre_local(self, new_nombre_local):
        self.nombre_local=new_nombre_local
        
    def set_nombre_visitante(self, new_nombre_visitante):
        self.nombre_visitante=new_nombre_visitante
        
    def agregar_jugador(self, num_jersey):
        nuevo_jugador = jg.Jugador(num_jersey)
        self.jugadores.append(nuevo_jugador)
        
    def agregar_goles_local(self):
        self.marcador[0]+=1
    
    def agregar_goles_visitante(self):
        self.marcador[1]+=1
        
    def acceder_goles_local(self):#actua como un getter
        return self.marcador[0]
        
    def acceder_goles_visitante(self):
        return self.marcador[1]
    
    # def acceder_jugadores(self):
    #     for jugador in self.jugadores:
    #        # jugador.get_nro_jersey 
    #        # jugador.get_nro_faltas
    #        return jugador
        

    
    
    def agregar_falta(self, num_jersey):
        jugador_encontrado = False #se crea esta variable para determinar si un jugador se ha encontrado o no(se usara para determinar si no se ha encontrado) y se empieza en false 
        for jugador in self.jugadores:
            print(jugador)
            if jugador.get_nro_jersey() == num_jersey:
                jugador.agregar_falta()
                jugador_encontrado = True
                print(f"Se le agregó una falta al jugador #{num_jersey}")
                break
        if not jugador_encontrado:#si la variable se mantuvo en falso significa que no se encontro jugador y entonces se muestra que no existe
            print(f"El jugador con jersey #{num_jersey} no existe")
            
    def acceder_faltas(self,num_jersey):
        jugador_encontrado = False
        for jugador in self.jugadores:
            print(jugador)
            if jugador.get_nro_jersey() == num_jersey:
                jugador_encontrado = True
                return jugador.get_nro_faltas() # retorna el valor de numero de faltas del jugador
                break
        if not jugador_encontrado:
            print(f"El jugador con jersey #{num_jersey} no existe")
                
    
        
        
        
partido = Partido()
partido.agregar_jugador(33)
partido.agregar_jugador(43)

for i in partido.jugadores:
    print(i)

# print(partido.jugadores)
# print(":")