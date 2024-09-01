def ver_sala():
    nombre_sala = input("Ingrese el nombre de la sala a visualizar: ")
    if nombre_sala in salas:
        sala = salas[nombre_sala]
        filas = len(sala)
        columnas = len(sala[0])
        
        # Generar letras dinámicamente para las columnas
        letras = [chr(65 + i) for i in range(columnas)]

        # Calcular el ancho dinámico de las celdas
        ancho_celda = max(4, len(str(filas)))  # Asegura que haya suficiente espacio

        # Mostrar encabezado de las columnas
        print(" " * (ancho_celda + 1), end="")
        for letra in letras:
            print(f"{letra.center(ancho_celda)}", end="")
        print("")
        
        # Mostrar asientos con numeración de filas
        for num_fila, fila in enumerate(sala, start=1):
            print(str(num_fila).rjust(ancho_celda), end=" ")  # Numeración de fila
            for asiento in fila:
                print(f"[{asiento.center(1)}]".rjust(ancho_celda), end=" ")  # Asiento formateado
            print("")
    else:
        print("La sala no existe.")

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
  
