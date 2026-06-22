# FUNCIONES - TPI --------------------------------------------------------------------------------------

# FUNCION PARA VALIDAR ENTRADAS 'INT'
def validar_numero(mensaje, permitir_cero=True):
    while True:
        try:
            num = int(input(mensaje))
            if num<0:
                print("ERROR. Debe ingresar un numero mayor a cero.")
                print("")
                continue
            return num
        except ValueError:
            print("ERROR. Debe ingresar un numero valido.")
            print("")


# FUNCION PARA VALIDAR ENTRADAS 'STRING'
def validar_texto(mensaje):
    while True:
        try:
            texto =  str(input(mensaje).capitalize())
            if texto == "":
                print("ERROR. No puede estar vacio.")
                print("")
                continue
            return texto
        except ValueError:
            print("ERROR. Debe ingresar letras validas.")
            print("")


# FUNCION PARA BUSCAR UN PAIS
# EXACTO
def buscar_paises(paises, nombre):
    if not paises:
        print("ERROR. No hay paises almacenados.")
        return
    nombre_limpio = text = nombre.strip().capitalize()
    for h in paises:
        if h["Nombre"].strip().capitalize() == nombre_limpio:
            return h
    return None
# PARCIAL
def buscar_pais_parcial(paises):
    print("")
    print("-"*50)
    print("--- BUSCAR PAISES ---")
    print("")
    if not paises:
        print("ERROR. No hay paises almacenados.")
        return
    else:
        nombre = validar_texto("Ingrese nombre o parte del nombre: ").lower()
        resultados = [p for p in paises if nombre in p["Nombre"].lower()]
        if not resultados:
            print(f"ERROR. No se encontraron países que coincidan con '{nombre}'.")
        else:
            for pais in resultados:
                print(f"- Pais: {pais['Nombre']} | Continente: {pais['Continente']} | Poblacion: {pais['Poblacion']} | Superficie: {pais['Superficie']} km²")




# FUNCION PARA MOSTRAR EL MENU
def menu():
    print("""
    - MENU -
    1. Agregar un país.
    2. Actualizar un país.
    3. Buscar un país.
    4. Filtrar países por un dato.
    5. Ordenar países por un dato.
    6. Mostrar estadísticas.
    7. Salir.
    """)


# Funcion para agregar un país con todos los datos necesarios
def agregar_paises(paises):
    print("")
    print("-"*50)
    print("--- AGREGAR PAISES ---")
    print("")
    while True:
        try:
            nombre = validar_texto("Ingresa el nombre del pais: ").capitalize()
            if buscar_paises(paises, nombre) is not None:
                raise ValueError(f"ERROR. El pais '{nombre}' ya existe en el almacenado anteriormente.")
            poblacion = validar_numero("Poblacion: ", permitir_cero=False)
            superficie = validar_numero("Superficie en km²: ", permitir_cero=False)
            continente = validar_texto(f"¿A que continente pertenece {nombre}?: ")
            nuevo_pais = {"Nombre": nombre, "Poblacion": poblacion, "Superficie": superficie, "Continente": continente}
            paises.append(nuevo_pais)
            print(f"¡'{nombre}' agregado con éxito al catálogo!")
            return
        except ValueError as e:
            print(f"ERROR inesperado. {e}")
        

# Funcion para actualizar los datos de Población y Superficie de un País
def actualizar_paises(paises):
    print("")
    print("-"*50)
    print("--- ACTUALIZAR PAISES ---")
    print("")
    if len(paises) == 0:
        print("")
        print("ERROR. No se ha almacenado ningun pais. Ingrese a la opcion 1.")
        print("")
        return
    else:
        nombre = validar_texto("¿Qué pais desea actualizar?: ").capitalize()
        pais_encontrado = buscar_paises(paises, nombre)
        if pais_encontrado is None:
            print(f"El pais '{nombre}' no se encuentra almacenado.")
            return
        else:
            print(f"- Pais: {pais_encontrado['Nombre']} | Continente: {pais_encontrado['Continente']} | Poblacion: {pais_encontrado['Poblacion']} | Superficie: {pais_encontrado['Superficie']} km²")
            while True:
                print("""
                ¿Que dato desea actualizar?
                1. Población.
                2. Superficie.
                """)
                opcion = input("Ingresa una opción (1-2): ")
                try:
                    if not opcion:
                        raise ValueError("ERROR. La opción no puede estar vacía.")
                    elif opcion == 1 or opcion == "1":
                        poblacion = validar_numero(f"¿Qué poblacion tiene {nombre} actualmente?: ", permitir_cero=False)
                        if pais_encontrado["Poblacion"] == poblacion:
                            raise ValueError(f"{nombre} ya tiene esa cantidad de poblacion.")
                        pais_encontrado["Poblacion"] = poblacion
                        print("¡Poblacion actualizado correctamente!")
                        return
                    elif opcion == 2 or opcion == "2":
                        superficie = validar_numero(f"¿Qué superficie tiene {nombre}?(en km²): ", permitir_cero=False)
                        if pais_encontrado["Superficie"] == superficie:
                            raise ValueError(f"{nombre} ya tiene esa superficie almacenada.")
                        pais_encontrado["Superficie"] = superficie
                        print("¡Superficie actualizada correctamente!")
                        return
                    else:
                        print("ERROR. Debe ingresar una numero valido.")
                        continue
                except ValueError as e:
                    print(f"ERROR inesperado. {e}")

# Funcion para filtrar paises
def filtrar_paises(paises):
    print("")
    print("-"*50)
    print(" --- FILTRAR PAÍSES --- ")
    print("")
    if len(paises) == 0:
        print("ERROR. No hay países almacenados para filtrar.")
        return
    while True:
        print("""
        ¿Por qué criterio desea filtrar?
        1. Continente.
        2. Rango de población.
        3. Rango de superficie.
        4. Volver al menú principal.
        """)
        opcion = input("Ingresa una opción (1-4): ").strip()
        resultados = []
        
        if opcion == "1":
            continente = validar_texto("Ingrese el continente a buscar: ").strip().lower()
            resultados = [p for p in paises if p["Continente"].lower() == continente]
        elif opcion == "2":
            print("Defina el rango de población: ")
            min_pob = validar_numero("Población mínima: ")
            max_pob = validar_numero("Población máxima: ")
            resultados = [p for p in paises if min_pob <= p["Poblacion"] <= max_pob]
        elif opcion == "3":
            print("Defina el rango de superficie (km²):")
            min_sup = validar_numero("Superficie mínima: ")
            max_sup = validar_numero("Superficie máxima: ")
            resultados = [p for p in paises if min_sup <= p["Superficie"] <= max_sup]
        elif opcion == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("ERROR. Debe ingresar una opción válida (1-4).")
            continue
            
        # Mostrar los resultados del filtro si es que se eligió la opción 1, 2 o 3
        if not resultados:
            print("ERROR. No se encontraron países que coincidan con esos criterios.")
        else:
            print(f"\nSe encontraron {len(resultados)} resultados:")
            for p in resultados:
                print(f"- Pais: {p['Nombre']} | Continente: {p['Continente']} | Poblacion: {p['Poblacion']} | Superficie: {p['Superficie']} km²")


# Funcion para ordenar la lista como desee el cliente
def ordenar_paises(paises):
    print("")
    print("-"*50)
    print("--- ORDENAR PAÍSES --- ")
    if len(paises) == 0:
        print("ERROR. No hay países almacenados para ordenar.")
        return
    while True:
        print("""
        ¿Por qué criterio desea ordenar?
        1. Nombre (A-Z).
        2. Población (Mayor a Menor).
        3. Superficie (Ascendente o Descendente).
        4. Volver al menú principal.
        """)
        opcion = input("Ingresa una opción (1-4): ").strip()
        
        if opcion == "1":
            # Ordena alfabéticamente por la clave "Pais"
            paises_ordenados = sorted(paises, key=lambda x: x["Nombre"])
            print("\nPaíses ordenados por Nombre (A-Z):")
        elif opcion == "2":
            # Ordena de mayor a menor población usando reverse=True
            paises_ordenados = sorted(paises, key=lambda x: x["Poblacion"], reverse=True)
            print("\nPaíses ordenados por Población (Mayor a Menor):")
        elif opcion == "3":
            orden = input("¿Desea orden (A)scendente o (D)escendente?: ").strip().upper()
            if orden == 'A':
                paises_ordenados = sorted(paises, key=lambda x: x["Superficie"])
                print("\nPaíses ordenados por Superficie (Menor a Mayor):")
            elif orden == 'D':
                paises_ordenados = sorted(paises, key=lambda x: x["Superficie"], reverse=True)
                print("\nPaíses ordenados por Superficie (Mayor a Menor):")
            else:
                print("ERROR. Debe ingresar 'A' o 'D'.")
                continue
        elif opcion == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("ERROR. Debe ingresar una opción válida (1-4).")
            continue
            
        # Imprimimos los resultados si se eligió la opción 1, 2 o 3
        for p in paises_ordenados:
            print(f"- Pais: {p['Nombre']} | Poblacion: {p['Poblacion']} | Superficie: {p['Superficie']} km²")


# Funcion para ver cual es el pais con mayor o menor poblacion
def mayor_menor_población(paises):
    pais_mayor_poblacion = paises[0]
    pais_menor_poblacion = paises[0]
    for pais in paises:
        if pais["Poblacion"] > pais_mayor_poblacion["Poblacion"]:
            pais_mayor_poblacion = pais
        if pais["Poblacion"] < pais_menor_poblacion["Poblacion"]:
            pais_menor_poblacion = pais
    print(f"El pais con mayor poblacion es {pais_mayor_poblacion['Nombre']} con {pais_mayor_poblacion['Poblacion']} habitantes.")
    print(f"El pais con menor poblacion es {pais_menor_poblacion['Nombre']} con {pais_menor_poblacion['Poblacion']} habitantes.")
    return


# Funcion para sacar el promedio de la poblacion
def promedio_población(total_poblacion, paises):
    promedio_poblacion = total_poblacion // len(paises)
    print("")
    print(f"Promedio de población: {promedio_poblacion}")
    return


# Funcion para sacar el promedio de la superficie
def promedio_superficie(total_superficie, paises):
    promedio_superficie = round(total_superficie / len(paises), 2)
    print("")
    print(f"Promedio de superficie: {promedio_superficie}")
    return


# Funcion para contar paises por continentes
def paises_por_continente(paises):
    Asia = 0
    America = 0
    Antartida = 0
    Europa = 0
    Oceania = 0
    for pais in paises:
        if pais["Continente"] == "Asia":
            Asia += 1
        elif pais["Continente"] == "America":
            America += 1
        elif pais["Continente"] == "Antartida":
            Antartida += 1
        elif pais["Continente"] == "Europa":
            Europa += 1
        elif pais["Continente"] == "Oceania":
            Oceania += 1
    print(f"""
            - CANTIDAD DE PAISES POR CONTINENTE -
            Asia = {Asia}
            America = {America}
            Antartida = {Antartida}
            Europa = {Europa}
            Oceania = {Oceania}
            """)
    return


# Funcion para mostrar alguna estadistica
def mostrar_estadisticas(paises): 
    print("")
    print("-"*50)
    total_poblacion = 0
    total_superficie = 0
    if len(paises) == 0:
        print("")
        print("ERROR. No se ha almacenado ningun pais. Ingrese a la opcion 1.")
        print("")
        return
    else:
        for pais in paises:
            total_superficie += pais["Superficie"]
            total_poblacion += pais["Poblacion"]
        while True:
            print("""
                ¿Que desea saber?
                1. País con mayor y menor población.  
                2. Promedio de población.
                3. Promedio de superficie.  
                4. Cantidad de países por continente. 
                """) 
            opcion = input("Ingresa una opción (1-4): ")
            try:
                if not opcion:
                    raise ValueError("ERROR. La opción no puede estar vacía.")
                elif opcion == 1 or opcion == "1":
                    mayor_menor_población(paises)
                    break
                elif opcion == 2 or opcion == "2":
                    promedio_población(total_poblacion, paises)
                    break
                elif opcion == 3 or opcion == "3":
                    promedio_superficie(total_superficie, paises)
                    break
                elif opcion == 4 or opcion == "4":
                    paises_por_continente(paises)
                    break
                else:
                    print("ERROR. Debe ingresar una numero valido.")
                    continue
            except ValueError as e:
                print(f"ERROR inesperado. {e}")


def cargar_datos_csv():
    paises = []
    if not os.path.exists(ARCHIVO_CSV):
        print(f"Aviso: No se encontró el archivo '{ARCHIVO_CSV}'. Se empezará con un catálogo vacío.")
        return paises
    
    try:
        with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Armamos el diccionario asegurando que los números sean enteros
                pais = {
                    "Nombre": fila["Nombre"].strip().capitalize(),
                    "Poblacion": int(fila["Poblacion"]),
                    "Superficie": int(fila["Superficie"]),
                    "Continente": fila["Continente"].strip().capitalize()
                }
                paises.append(pais)
        print(f"¡Éxito! Se cargaron {len(paises)} países desde la base de datos.")
    except Exception as e:
        print(f"ERROR crítico al leer el archivo CSV: {e}")
    return paises

# Funcion para guardar nuevos datos en el archivo
def guardar_datos_csv(paises):
    try:
        with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as archivo:
            # Definimos los encabezados exactos que usarán las claves del diccionario
            Pais = ["Nombre", "Poblacion", "Superficie", "Continente"]
            escritor = csv.DictWriter(archivo, fieldnames=Pais)
            
            escritor.writeheader()
            for pais in paises:
                escritor.writerow(pais)
    except Exception as e:
        print(f"ERROR al intentar guardar en el archivo CSV: {e}")



# MAIN - TPI -------------------------------------------------------------------------------------------------------------------------------------------------
import csv
import os

ARCHIVO_CSV = "paises.csv"

if __name__ == "__main__":
    print("="*100)
    print("")
    print("  BIENVENID@ AL ALMACENAMIENTO DE PAISES  ")
    print("")
    
    # 1. Cargar los datos a la lista ANTES de iniciar el menú
    paises = cargar_datos_csv()
    
    while True:
        menu()
        try:
            opcion = input("Ingresa una opción (1-7): ").strip()
            if not opcion:
                raise ValueError("ERROR. La opción no puede estar vacía.")
            opcion = int(opcion)
            match opcion:
                case 1: 
                    agregar_paises(paises)
                    guardar_datos_csv(paises) # Guardamos los cambios inmediatamente
                case 2: 
                    actualizar_paises(paises)
                    guardar_datos_csv(paises) # Guardamos los cambios inmediatamente
                case 3: 
                    buscar_pais_parcial(paises)
                case 4: 
                    filtrar_paises(paises)
                case 5: 
                    ordenar_paises(paises)
                case 6: 
                    mostrar_estadisticas(paises)
                case 7:
                    print("")
                    print("Guardando datos y saliendo del inventario... ¡Hasta luego!")
                    guardar_datos_csv(paises) # Un último guardado de seguridad al salir
                    break
                case _:
                    print("ERROR. Ingresa un número válido entre el 1 y 7.")
                    print("")
        except ValueError as e:
            print(f"ERROR: Entrada inválida. {e}")
            print("")
