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
    sala = [['0' for _ in range(columnas)] for _ in range(filas)]

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
        
def asignar_puesto():
    # Solicita al usuario el nombre de la sala donde quiere asignar el asiento
    nombre_sala = input("Ingrese el nombre de la sala: ")
    
    # Verifica si la sala existe en el diccionario 'salas'
    if nombre_sala in salas:
        # Obtiene la matriz de asientos de la sala seleccionada
        sala = salas[nombre_sala]
        # Calcula el número de filas y columnas de la sala
        filas = len(sala)
        columnas = len(sala[0])
        
        # Bucle para asegurar que el usuario ingrese un número de fila válido
        while True:
            try:
                # Solicita al usuario que seleccione la fila
                fila = int(input(f"Seleccione la fila del 1 al {filas}: "))
                if 1 <= fila <= filas:  # Verifica que la fila esté dentro del rango válido
                    break  # Sale del bucle si la fila es válida
                else:
                    print("Número de fila fuera de rango. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número.")
        
        # Genera una lista de letras correspondientes a las columnas (A, B, C, etc.)
        letras = [chr(65 + i) for i in range(columnas)]
        
        # Bucle para asegurar que el usuario ingrese una letra de columna válida
        while True:
            # Solicita al usuario que seleccione la columna
            Cletra = input(f"Seleccione la letra de la columna (A-{letras[-1]}): ").upper()
            if Cletra in letras:  # Verifica que la letra esté dentro del rango válido
                columna = letras.index(Cletra)  # Obtiene el índice de la columna seleccionada
                break  # Sale del bucle si la columna es válida
            else:
                print("Letra fuera de rango. Intente de nuevo.")
        
        # Verifica si el asiento está disponible
        if sala[fila-1][columna] == '0':  # '0' indica que el asiento está disponible
            sala[fila-1][columna] = 'X'  # Marca el asiento como ocupado ('X')
            print(f"Asiento {Cletra}{fila} asignado correctamente.")
        else:
            print("El asiento ya está ocupado. Intente con otro.")  # Informa si el asiento está ocupado
    else:
        print("La sala no existe.")  # Informa si la sala no existe en el diccionario 'salas'
     


  
# Bucle principal - Marilyn
def main():
    while True:
        opcion = menu()
        if opcion == '1':
            crear_sala()
        elif opcion == '2':
            ver_sala()
        elif opcion == '3':
            asignar_puesto()
        elif opcion == '4':
            cargar_salas()
        elif opcion == '5':
            guardar_salas()
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()