from tkinter import *
raiz= Tk()

#Ventana principal
raiz.title("Registro del partido")
raiz.resizable(True,True)
raiz.iconbitmap("hockey.ico")
#raiz.geometry("650x350")
raiz.config(bg= "grey")

#Contenido
myFrame= Frame()
myFrame.pack(side = "left")
myFrame.config(bg="dark grey")
myFrame.config(width = "650", height="750")
myFrame.config(bd=35)
myFrame.config(relief= "sunken")
myFrame.config(cursor= "hand2")

raiz.mainloop()
