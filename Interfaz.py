import tkinter as tk
from tkinter import messagebox as mb
import Partido as part

partido=part.Partido()#crea un objeto de la clase Partido del modulo Partido para ser usado dentro de todo el recorrido del programa

class Final:# Ultima ventana que el usuario vera en pantalla al finalizar el partido donde mostrara todo los resultados
    def __init__(self):
        self.goles_local=partido.acceder_goles_local()
        self.goles_visitante=partido.acceder_goles_visitante()
        self.nombre_local=partido.get_nombre_local()
        self.nombre_visitante=partido.get_nombre_visitante()
        self.root = tk.Tk(className='Resultados Finales')
        self.root.geometry('200x200')
        self.labelZ = tk.Label(self.root, text="Resultados Finales")
        self.labelZ.pack()
        for jugador in partido.jugadores:#por cada jugador ingresado en la lista de jugadores muestra en ventana sus numero de jerseys y su numero de faltas
            self.labelX=tk.Label(self.root,text=jugador)
            self.labelX.pack() 
            
        self.labelA = tk.Label(self.root, text="Marcador Final:") # Muestra el Marcador Final
        self.labelB=tk.Label(self.root,text=self.nombre_local)
        self.labelC=tk.Label(self.root,text=self.goles_local)
        self.labelD=tk.Label(self.root,text=self.nombre_visitante)
        self.labelE=tk.Label(self.root,text=self.goles_visitante)
        
        self.labelA.pack()# muestra los widgets
        self.labelB.pack()
        self.labelC.pack()
        self.labelD.pack()
        self.labelE.pack()
                    
        self.root.mainloop()

class Marcador():#Ventana que muestra el marcador parcial
    def __init__(self):
        self.goles_local=partido.acceder_goles_local()#accede a los goles que se llevan en la clase Partido para usarlas en el marcador
        self.goles_visitante=partido.acceder_goles_visitante()
        self.nombre_local=partido.get_nombre_local()#le asigna al atributo lo ingresado en la primer ventana  para ser usado en el marcador
        self.nombre_visitante=partido.get_nombre_visitante() 
        self.root = tk.Tk(className='Marcador parcial')
        self.root.geometry('200x200')
        self.labelA = tk.Label(self.root, text="Marcador parcial:")
        self.labelB=tk.Label(self.root,text=self.nombre_local)#muestra lo ingresado al principio en los nombres de los equipos
        self.labelC=tk.Label(self.root,text=self.goles_local)#muestra el numero de goles que llevan desde la clase partido
        self.labelD=tk.Label(self.root,text=self.nombre_visitante)#muestra lo ingresado al principio en los nombres de los equipos
        self.labelE=tk.Label(self.root,text=self.goles_visitante)#muestra el numero de goles que llevan desde la clase partido
        self.button1 = tk.Button(self.root,text = 'Siguiente',command=lambda:[self.root.destroy()])
           
        self.labelA.pack()#muestra los widgets
        self.labelB.pack()
        self.labelC.pack()
        self.labelD.pack()
        self.labelE.pack()
        self.button1.pack()

        self.root.mainloop()

class Goles():#Ventana para ingresar goles
    def __init__(self):
        self.nombre_local=partido.get_nombre_local()#recibe los nombres ingresados en la ventana inicial para usarlos en los botones
        self.nombre_visitante=partido.get_nombre_visitante()
        self.root = tk.Tk(className='Gol')
        self.root.geometry('200x100')
        self.labelA = tk.Label(self.root, text="¿Que equipo anoto?")
        self.button1 = tk.Button(self.root,text = self.nombre_local,command=lambda:[self.root.destroy(),self.gol_local()])
        # boton que sirve para pasar al marcador parcial con el gol del equipo 
        self.button2 = tk.Button(self.root, text = self.nombre_visitante, command=lambda:[self.root.destroy(),self.gol_visitante()])
        # boton que sirve para pasar al marcador parcial con el gol del equipo

        self.labelA.pack() # muestra los widgets
        self.button1.pack()
        self.button2.pack()
        self.root.mainloop()
       
    def gol_local(self): #le suma un gol al equipo local y crea la ventana del marcador parcial
            partido.agregar_goles_local()
            marcador=Marcador()
            return marcador
  
    def gol_visitante(self): #le suma un gol al equipo local y crea la ventana del marcador parcial
            partido.agregar_goles_visitante() 
            marcador=Marcador()
            return marcador
   

class Faltas:#ventana donde se ingresan las faltas
    def __init__(self):
        self.root = tk.Tk(className='Falta')#titulo de la ventana
        self.root.geometry('300x300')#tamaño de la ventana
        self.labelA = tk.Label(self.root, text="1.Ingresar el numero del jersey del jugador")#mensaje de texto para ingresar el numero del jugador
        self.labelB = tk.Label(self.root, text="2.Ingrese el nombre de la falta")#mensaje de texto para ingresar el nombre de la falta
        
        self.entry_1 = tk.StringVar(self.root)#declara el tipo de dato que se va a ingresar en entry_widget1
        self.entry_2 = tk.StringVar(self.root)#declara el tipo de dato que se va a ingresar en entry_widget2
        self.entry_widget_1 = tk.Entry(self.root, textvariable=self.entry_1)#crea la caja de texto para ingresar el numero del jersey
        self.entry_widget_2 = tk.Entry(self.root, textvariable=self.entry_2)#crea la caja de texto para ingresar el nombre de la falta
      
        self.button1 = tk.Button(self.root,
                           text = 'Listo',
                           command=lambda:[self.sancion(self.entry_1.get(), self.entry_2.get()),self.misconduct(self.entry_1.get(), self.entry_2.get()),
                                           self.root.destroy()  # funciones
                                           ])#boton que servira para mostrar lo que se hara con el jugador que hizo
                                            #la falta, con la funcion decision y guardar que recibe como parametros lo
                                            #que se entro en las cajas de texto

        self.labelA.pack()#se muestra el mensaje de textoA
        self.entry_widget_1.pack()#se muestra la caja de texto1
        self.labelB.pack()#se muestra el mensaje de textoB
        self.entry_widget_2.pack()#se muestra el mensaje de texto2
        self.button1.pack()#muestra el boton 

        self.root.mainloop()#permite cerrar la ventana
       
    def sancion(self, numero_jugador, nombre_falta):#funcion que muestra la sancion correspondiente a la falta recibe como parametros los elementos escritos en el entry_widget1 y entry_widget2
        falta_menor=["intento ataque", "broken stick", "charging", "boarding", "cross checking", "delaying", "elbowing", " falling on the puck","handpass", "high sticks", "holding", "hoocking","interference","slashing","tripping" ]
        falta_mayor=["fighting","interference by spectators", "checking from behind", 'leaving penalty bench', "abuse of officials", "profane language", ]
        if nombre_falta in falta_menor:#si la falta escrita esta en falta menor 
            mb.showinfo("Penalizacion","El jugador penalizado debe permanecer durante 2 minutos en el penalty box")#muestra un mensaje que diga que se debe hacer con el jugador
        elif nombre_falta in falta_mayor:#si la falta escrita esta en falta menor 
            mb.showinfo("Penalizacion","El jugador penalizado debe permanecer durante 10 minutos en el penalty box")#muestra un mensaje que diga que se debe hacer con el jugador
        elif nombre_falta not in falta_menor or nombre_falta not in falta_mayor:
            mb.showinfo("Penalizacion","la falta no existe o esta escrita de forma incorrecta")
            
    def misconduct(self,numero_jugador,nombre_falta): #funcion que aumenta el numero de faltas que lleva el jugador ingresado y decide si esta en riesgo de ser expulsado
        partido.agregar_jugador(numero_jugador)#agrega el jugador ingresado al partido
        partido.agregar_falta(numero_jugador)#le suma uno al nro_faltas que lleva
        if partido.acceder_faltas(numero_jugador)<2:
            mb.showinfo("Accion","El jugador no esta en riesgo de misconduct")
        else:
            mb.showinfo("Accion","El jugador debe ser expulsado")

class Mensaje2():#Ventana principal
    def __init__(self):
        self.root = tk.Tk(className='¿Que desea hacer?')#titulo de la ventana
        self.root.geometry('500x400')#tamaño de la ventana
        self.labelA = tk.Label(self.root, text="1.Ingresar una falta")
        self.labelB = tk.Label(self.root, text="2.Ingresar una anotacion")
        self.labelC = tk.Label(self.root, text="3.Finalizar el partido")
       
        self.button1 = tk.Button(self.root,
                           text = 'Oprima aqui.',
                           command=lambda:[self.falta()]) # boton para pasar a la ventana de faltas
        self.button2 = tk.Button(self.root,
                           text = 'Oprima aqui.',
                           command=lambda:[self.gol()])# boton para pasar a la ventana de goles
        self.button3 = tk.Button(self.root,
                           text = 'Oprima aqui.',
                           command=lambda:[self.finalizar()])# boton para pasar a la ventana final

        self.labelA.pack()# muestra los widgets
        self.button1.pack()
        self.labelB.pack()
        self.button2.pack()
        self.labelC.pack()
        self.button3.pack()

        self.root.mainloop()
       
    def falta(self):# pasa al menu donde se ingresan las faltas
        menu_falta=Faltas()
        return menu_falta
    def gol(self):# pasa al menu donde se ingresan los goles
        menu_gol=Goles()
        return menu_gol
   
    def finalizar(self):# pasa al menu final
       self.root.destroy()
       final=Final()
       return final

class Mensaje1():#Ventana de inicio
   def __init__(self):
       self.root = tk.Tk(className='Orden del juego')#titulo de la ventana
       self.root.geometry('400x300')#tamaño de la ventana

       self.labelA = tk.Label(self.root, text="Ingrese el nombre del equipo local:")
       self.labelB = tk.Label(self.root, text="Ingrese el nombre del equipo visitante:")       
       
       self.button = tk.Button(self.root,
                          text = 'Iniciar partido',
                          command=lambda:[self.guardar_nombres(self.entry_1.get(), self.entry_2.get()),self.cambio() ])
       #boton que servira para guardar los nombres de los equipos, con la funcion que recibe lo ingresado en las cajas de texto
        #y cambia la ventana

       
       self.entry_1 = tk.StringVar()#declara el tipo de dato que se va a ingresar en entry_widget1
       self.entry_2 = tk.StringVar()
       self.entry_widget_1 = tk.Entry(self.root, textvariable=self.entry_1)#crea la caja de texto para ingresar el nombre del equipo local
       self.entry_widget_2 = tk.Entry(self.root, textvariable=self.entry_2)#crea la caja de texto para ingresar el nombre del equipo visitante

       self.labelA.pack()# muestra todos los widgets
       self.entry_widget_1.pack()
       self.labelB.pack()
       self.entry_widget_2.pack()
       self.button.pack()

       self.root.mainloop()

   def guardar_nombres(self,local,visitante):#recibe como parametros lo ingresado en las cajas de texto
       partido.set_nombre_local((local)) #establece lo ingresado en las cajas de texto como los atributos de nombre del equipo local y visitante respectivamente
       partido.set_nombre_visitante((visitante))
   
   def cambio(self):
       self.root.destroy()#cierra la ventana actual
       menu=Mensaje2() #crea otra ventana
       return menu
        
       
app = Mensaje1()

