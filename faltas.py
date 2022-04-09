import clase
falta_menor=["intento ataque", "broken stick", "charging", "boarding", "cross checking", "delaying", "elbowing", " falling on the puck","handpass", "high sticks", "holding", "hoocking","interference","slashing","tripping" ]
falta_mayor=["fighting","interference by spectators", "checking from behind", 'leaving penalty bench', "abuse of officials", "profane language", ]

nro_jugador= int(input("Ingrese el numero de jersey del jugador penalizado: "))

def falta_penalizacion():
    x=input("Ingrese el nombre de la falta: ")
    faltas=0

    if x in falta_menor:
        print("El jugador penalizado debe permanecer durante 2 minutos en el penalty box")
        faltas+=1
        
    elif x in falta_mayor:
        print("El jugador penalizado debe permanecer durante 10 minutos en el penalty box")
        faltas+=3
        
    elif x not in falta_menor or x not in falta_mayor:
        print("la falta no existe o esta escrita de forma incorrecta")
    
    return faltas
nro_faltas=falta_penalizacion()
jugador=clase.Jugador(nro_jugador,nro_faltas)

def misconduct():
    
    if jugador.nro_faltas < 2:
        print("El jugador con numero de jersey",jugador.nro_jersey, "no esta en riesgo de misconduct")    
    else:
        print("El jugador con numero de jersey",jugador.nro_jersey, "se debe de expulsar al jugador del partido")
