# --- CLASE MADRE (Superclase) ---
class Vehiculo:
    def __init__(self, placa, nombre, cedula, hora_entrada):
        self.placa = placa
        self.nombre = nombre
        self.cedula = cedula
        self.hora_entrada = hora_entrada
        self.tipo = "Generico"

    def obtener_info(self):
        return f"Placa: {self.placa} | Conductor: {self.nombre} | Tipo: {self.tipo}"


# --- CLASE HIJA 1 ---
class Automovil(Vehiculo):
    def __init__(self, placa, nombre, cedula, hora_entrada, puertas=4):
        super().__init__(placa, nombre, cedula, hora_entrada)
        self.puertas = puertas
        self.tipo = "Automovil"


# --- CLASE HIJA 2 ---
class Moto(Vehiculo):
    def __init__(self, placa, nombre, cedula, hora_entrada, casco_incluido=True):
        super().__init__(placa, nombre, cedula, hora_entrada)
        self.casco_incluido = casco_incluido
        self.tipo = "Motocicleta"