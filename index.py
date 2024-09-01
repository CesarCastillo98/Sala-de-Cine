salas = {}

def menu():
    print("\n--- Menú Principal ---")
    print("1. Crear sala")
    print("2. Ver sala")
    print("3. Asignar puesto")
    print("4. Cargar sala")
    print("5. Salir")
    return input("Seleccione una opción: ")

def crear_sala():
    nombre_sala = input ("Ingrese el nombre de la sala: ")
    filas = int(input("Ingrese la cantidad de filas: "))
    columnas = [['0' for _ in range(columnas)] for _ in range(filas)]

    salas[nombre_sala] = salas
    print(f"Sala '{nombre_sala}' creada exitosamente.")
    
    def ver_sala():
    nombre_sala = input("Ingrese el nombre de la sala a visualizar: ")
    if nombre_sala in salas:
        sala = salas[nombre_sala]
        filas = len(sala)
        columnas = len(sala[0])

        letras = [chr(65 + i) for i in range(columnas)]

        ancho_celda = max(4, len(str(filas)))

        print(" " * (ancho_celda + 1), end="")
        for letra in letras:
            print(f"{letra.center(ancho_celda)}", end="")
        print("")

        for num_fila, fila in enumerate(sala, start=1):
            print(str(num_fila).rjust(ancho_celda), end=" ")
            for asiento in fila:
                print(f"[{asiento.center(1)}]".rjust(ancho_celda), end=" ")
            print("")
    else:
        print("La sala no existe.")


  
