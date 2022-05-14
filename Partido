import Jugador as jg

class Partido:#partido comentar todo el codigo estas son las logicas usar el terminal tambien hacer para goles
    def __init__(self): 
        self.jugadores = []
            
    def agregar_jugador(self, num_jersey):
        nuevo_jugador = jg.Jugador(num_jersey)
        self.jugadores.append(nuevo_jugador)
        
    def agregar_falta(self, num_jersey):
        jugador_encontrado = False
        for jugador in self.jugadores:
            print(jugador)
            if jugador.get_nro_jersey() == num_jersey:
                jugador.agregar_falta()
                jugador_encontrado = True
                print(f"Se le agregó una falta al jugador #{num_jersey}")
                break
        if not jugador_encontrado:
            print(f"El jugador con jersey #{num_jersey} no existe")
