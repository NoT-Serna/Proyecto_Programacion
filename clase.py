class Jugador:
    def __init__(self,nro_jersey,nro_faltas):
        self.nro_jersey=nro_jersey
        self.nro_faltas=nro_faltas
    
    def set_nro_jersey(self):
        return self.nro_jersey
        
    def get_nro_jersey(self,nro_jersey):
        self.nro_jersey=nro_jersey
 
    def set_nro_faltas(self):
        return self.nro_faltas

    def get_nro_faltas(self,nro_faltas):
        self.nro_faltas=nro_faltas
        