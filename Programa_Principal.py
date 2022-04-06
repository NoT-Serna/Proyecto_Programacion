import goles , timer , faltas


menu="""
Partido numero: x
1.Ingrese el nombre del equipo1:         Ingrese el nombre del equipo2:
2.Hora de inicio del partido:
3.Ingrese falta(si hubo falta):
4.Ingrese gol:
5.Resultados del partido:acabe el temporizador
0. Volver al menú

Ingrese su opción: 
"""
opcion = input(menu)

#numeral 1 
if opcion == "1":
    equipo1=input("Equipo local:")
    equipo2=input("Equipo visitante:")
    print(equipo1, "vs",equipo2)
#numeral 2 
elif opcion == "2":
    timer.iniciar()

#numeral 3
elif opcion == "3":
    falta_penalizacion=faltas.falta_penalizacion()
    faltas.misconduct(falta_penalizacion)    

#numeral 4
elif opcion == "4":
    equipo=input("Que equipo hizo el gol?: ")
    if equipo=="visitante":
        goles.gol2()
    elif equipo=="local":
        goles.gol1()
    
#numeral 5
elif opcion == "5":
    print("marcador final:","local",goles.gol1(),":","visitante",goles.gol2())
    print("")
