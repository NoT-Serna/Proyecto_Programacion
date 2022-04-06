def gol1():
        jugador1 = int(input("Ingrese el numero del jugador"))
        x = int(input("Si gol escriba 1, sino escriba 2"))
        gol_local = 0
        if x==1:
            gol_local+=1
            print("Gol jugador numero",jugador1)
        elif x==2:
            gol_local+=0
        
        return gol_local
    
def gol2():
        jugador2 = int(input("Ingrese el numero del jugador"))
        x = int(input("Si gol escriba 1, sino escriba 2"))
        gol_visitante = 0
        if x==1:
            gol_visitante+=1
            print("Gol jugador numero",jugador2)
        elif x==2:
            gol_visitante+=0
        
        return gol_visitante
        
     
print("marcador parcial","local",gol1(),":","visitante",gol2())
