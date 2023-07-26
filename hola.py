class Vehiculo:
    def arrancar(self):
        print("Se arranco")
    def tocar_bocina(self):
        print("Se toco bocina")
    
class Auto(Vehiculo):
    def abrir_capot(self):
        print("Se abrio el capot")

class Lancha(Vehiculo):
    def __init__(self, nombremotor):
        self.nombremotor = nombremotor
        
class MovimientosEmbarcacion(Lancha):
    def virar_a_babor(self): 
        print("Se viro a babor")
    def estribor(self): 
        print("Se viro a estribor")

auto1 = Auto()
