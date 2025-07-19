import os

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    print(f"Intentando abrir: {ruta_script_absoluta}")
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            print("\n--- Resultado de la ejecución ---\n")
            exec(codigo, globals())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    # Subimos un nivel desde "Parcial 02" a la carpeta raíz del proyecto
    ruta_base = os.path.dirname(os.getcwd())

    opciones = {
        '1': 'Parcial 01/Semana 02/Ejemplo de Abstraccion.py',
        '2': 'Parcial 01/semana 03/Promedio_semanal_del_clima_POO..py',
        '3': 'Parcial 01/Semana 04/Sistema_seguros_Conseseg.py',
        '4': 'Parcial 01/Semana 05/Ejemplo_Tipos_de_datos_Identificadores.py',
        '5': 'Parcial 01/Semana 06/Clases_objetos_herencia_encapsulamiento _y_polimorfismo..py',
        '6': 'Parcial 01/Semana 07/Ejemplo_sistema reservacion_de_vuelos.py',
    }

    while True:
        print("\nMenú Principal - Dashboard")
        for key, value in opciones.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            print("Ruta completa del script:", ruta_script)
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
