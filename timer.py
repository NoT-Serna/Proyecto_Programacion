import time

def countdown(num_of_mins):
    while num_of_mins:
        m, s = divmod(num_of_mins, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='/r')
        time.sleep(1)
        num_of_mins -= 1
        
    print('Countdown finished.')

inp = input('Ingrese el numero de minutos de juego: ')
countdown(inp)
