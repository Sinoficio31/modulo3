from estacionamiento import EstacionamientoSimple

def menu():
    estacionamiento = EstacionamientoSimple(total_puestos=40)

    while True:
        print("\n========================================")
        print("   SISTEMA DE ESTACIONAMIENTO UNIVERSITARIO")
        print("========================================")
        print(" 1. Ver mapa del estacionamiento y puestos libres")
        print(" 2. Registrar Entrada de Vehiculo")
        print(" 3. Registrar Salida y calcular tiempo de estancia")
        print(" 4. Salir")
        print("========================================")

        try:
            opcion = int(input("\nSeleccione una opcion (1-4): "))
        except ValueError:
            print("\n[ERROR DE ENTRADA] Debe ingresar un numero entero (1, 2, 3 o 4).")
            continue

        if opcion == 1:
            estacionamiento.mostrar_estado()
            
        elif opcion == 2:
            print("\n--- REGISTRAR ENTRADA ---")
            print(" Seleccione el tipo de vehiculo:")
            print(" [1] Automovil")
            print(" [2] Motocicleta")
            tipo_vehiculo = input(" Opcion (1 o 2): ").strip()

            if tipo_vehiculo not in ["1", "2"]:
                print("[ERROR] Tipo de vehiculo no valido.")
                continue

            nombre = input("Ingrese el nombre del conductor: ").strip()
            if not nombre.replace(" ", "").isalpha():
                print("[ERROR] El nombre solo debe contener letras.")
                continue

            cedula = input("Ingrese la cedula del conductor: ").strip()
            if not cedula.isdigit():
                print("[ERROR] La cedula debe contener unicamente numeros.")
                continue

            placa = input("Ingrese la placa del vehiculo: ").strip().upper()
            if not placa.isalnum():
                print("[ERROR] La placa solo puede contener letras y numeros.")
                continue

            if not nombre or not cedula or not placa:
                print("[ERROR] Todos los campos son obligatorios.")
                continue

            exito, mensaje = estacionamiento.registrar_entrada(tipo_vehiculo, nombre, cedula, placa)
            print(f"\n{mensaje}")
            
        elif opcion == 3:
            print("\n--- REGISTRAR SALIDA ---")
            placa = input("Ingrese la placa del vehiculo a retirar: ").strip().upper()
            exito, mensaje = estacionamiento.registrar_salida(placa)
            print(f"\n{mensaje}")
            
        elif opcion == 4:
            print("\n[INFO] Programa finalizado con exito.")
            break
        else:
            print("\n[ADVERTENCIA] Opcion no valida. Ingrese un numero entre 1 y 4.")

if __name__ == "__main__":
    menu()