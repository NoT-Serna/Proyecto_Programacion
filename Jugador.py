class Jugador:
    def __init__(self,nro_jersey):
        self.nro_jersey=nro_jersey
        self.nro_faltas=0 # empieza el nro_faltas en cero para poder ir aumentandole faltas
    
    def get_nro_jersey(self):
        return self.nro_jersey
        
    def get_nro_faltas(self):
        return self.nro_faltas
 
    def set_nro_faltas(self, new_nro_faltas):
        self.nro_faltas=new_nro_faltas
        
    def agregar_falta(self):
        self.nro_faltas += 1 # le aumenta el nro_faltas al objeto Jugador
        
    def __str__(self):
        return f"Jersey:{self.nro_jersey} Faltas:{self.nro_faltas}"
        
        
