import time

def iniciar(num_of_mins):
    while num_of_mins: 
        mins, secs = divmod(num_of_mins,60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") # pone eso y sobreescribe
        print(" ")
        time.sleep(1) #retrasa la ejecucion del bucle en un segundo
        num_of_mins -= 1
        
    print('Tiempo de partido finalizado.')

inp =int( input('Ingrese el numero de minutos de juego: '))
inp=inp*60
iniciar(inp)
