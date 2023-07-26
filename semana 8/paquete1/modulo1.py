class Cliente:
    def __init__(self, nombre, correo, edad, intereses):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.intereses = intereses

    def comprar(self):
        objeto = input("Qué deseas comprar?")
        puntodeventa = input("Dónde deseas comprar?")
        print(f"El cliente {self.nombre} ha comprado {objeto} en {puntodeventa}.")
        print(f"Se ha enviado una factura a su correo {self.correo}.")

    def contactar(self):
        print(f"Se ha enviado una notificación al cliente {self.nombre} al correo {self.correo}")
        print(f"En la notificación se incluyen promociones de los temas: {self.intereses}")

    def __str__(self):
        texto = f"Se ha creado al cliente {self.nombre}."
        return texto