import datetime
from Vehiculo import Automovil, Moto

class EstacionamientoSimple:
    def __init__(self, total_puestos=40):
        self.total_puestos = total_puestos
        self.puestos = [None] * total_puestos
        self.registros_activos = {}

    def mostrar_estado(self):
        print("\n" + "="*50)
        print(f" ESTADO ACTUAL DEL ESTACIONAMIENTO ({self.total_puestos} PUESTOS HABILES)")
        print("="*50)
        
        puestos_ocupados = 0
        for i in range(self.total_puestos):
            if self.puestos[i] is not None:
                placa = self.puestos[i]
                vehiculo = self.registros_activos[placa]
                print(f" Puesto {i+1:02d}: [OCUPADO] - Placa: {placa} | Tipo: {vehiculo.tipo} | Conductor: {vehiculo.nombre}")
                puestos_ocupados += 1
            else:
                print(f" Puesto {i+1:02d}: [LIBRE]")
        
        puestos_disponibles = self.total_puestos - puestos_ocupados
        print("-"*50)
        print(f" Total puestos ocupados: {puestos_ocupados}")
        print(f" Puestos disponibles: {puestos_disponibles}")
        print("="*50)

    def registrar_entrada(self, tipo_opcion, nombre, cedula, placa):
        if None not in self.puestos:
            return False, "[ERROR] ¡Estacionamiento lleno! No hay puestos disponibles."

        if placa in self.registros_activos:
            return False, f"[ERROR]: El vehiculo con placa {placa} ya se encuentra adentro."

        puesto_libre = self.puestos.index(None)
        hora_actual = datetime.datetime.now()
        
        if tipo_opcion == "1":
            vehiculo = Automovil(placa, nombre, cedula, hora_actual)
        else:
            vehiculo = Moto(placa, nombre, cedula, hora_actual)

        self.puestos[puesto_libre] = placa
        self.registros_activos[placa] = vehiculo

        return True, f"[EXITO] Vehiculo ({vehiculo.tipo}) registrado exitosamente.\n   Asignado al Puesto #{puesto_libre + 1}\n   Hora de entrada: {hora_actual.strftime('%H:%M:%S')}"

    def registrar_salida(self, placa):
        if not self.registros_activos:
            return False, "[ERROR] No hay vehiculos estacionados actualmente."

        if placa not in self.registros_activos:
            return False, f"[ERROR]: No se encontro ningun vehiculo registrado con la placa {placa}."

        vehiculo = self.registros_activos[placa]
        hora_salida = datetime.datetime.now()
        
        diferencia = hora_salida - vehiculo.hora_entrada
        minutos_totales = int(diferencia.total_seconds() / 60)
        if minutos_totales < 1:
            minutos_totales = 1

        puesto_idx = self.puestos.index(placa)
        self.puestos[puesto_idx] = None
        del self.registros_activos[placa]

        # --- GENERAR ARCHIVO .TXT DE COMPROBANTE ---
        nombre_archivo = f"comprobante_{placa}.txt"
        contenido = (
            "========================================\n"
            "     COMPROBANTE DE SALIDA (UNIVERSITARIO)\n"
            "========================================\n"
            f"• Tipo de Vehiculo: {vehiculo.tipo}\n"
            f"• Conductor: {vehiculo.nombre}\n"
            f"• Cedula: {vehiculo.cedula}\n"
            f"• Placa: {placa}\n"
            f"• Puesto liberado: P{puesto_idx + 1}\n"
            f"• Hora de entrada: {vehiculo.hora_entrada.strftime('%H:%M:%S')}\n"
            f"• Hora de salida: {hora_salida.strftime('%H:%M:%S')}\n"
            f"• Tiempo de estancia: {minutos_totales} minuto(s)\n"
            "========================================\n"
        )

        try:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                archivo.write(contenido)
        except Exception as e:
            print(f"[ADVERTENCIA] No se pudo guardar el archivo TXT: {e}")

        comprobante = (
            "\n" + "="*40 + "\n"
            "     COMPROBANTE DE SALIDA (UNIVERSITARIO)\n"
            f"   • Tipo: {vehiculo.tipo}\n"
            f"   • Conductor: {vehiculo.nombre}\n"
            f"   • Cedula: {vehiculo.cedula}\n"
            f"   • Placa: {placa}\n"
            f"   • Puesto liberado: P{puesto_idx + 1}\n"
            f"   • Tiempo de estancia: {minutos_totales} minuto(s)\n"
            f"   (Comprobante guardado en {nombre_archivo})\n"
            + "="*40
        )
        return True, comprobante