import csv 

def cargar_paises(nombre_archivo):
    """
    Lee un archivo CSV y retorna una lista de diccionarios.
    Maneja excepciones si el archivo no existe o hay errores de formato.
    """
    lista_paises = []
    try:
        # Abrimos el archivo en modo lectura
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            # DictReader usa la primera fila del CSV como claves del diccionario
            lector_csv = csv.DictReader(archivo)
            
            for fila in lector_csv:
                # Armamos el diccionario del país, convirtiendo población y superficie a enteros
                pais = {
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(fila["poblacion"].strip()),
                    "superficie": int(fila["superficie"].strip()),
                    "continente": fila["continente"].strip()
                }
                lista_paises.append(pais)
                
        print(f"Éxito: Se cargaron {len(lista_paises)} países correctamente desde el archivo.")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'. Verifica que esté en la misma carpeta.")
    except ValueError as e:
        print(f"Error de formato en los datos (revisa que población y superficie sean números): {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")
        
    return lista_paises

def agregar_pais(lista_paises):
    """Solicita los datos de un nuevo país, valida que no estén vacíos y lo agrega a la lista."""
    print("\n--- AGREGAR NUEVO PAÍS ---")
    
    nombre = input("Ingrese el nombre del país: ").strip()
    continente = input("Ingrese el continente: ").strip()
    
    # Validación de campos vacíos
    if not nombre or not continente:
        print("Error: El nombre y el continente no pueden estar vacíos.")
        return

    # Validación de tipos numéricos
    try:
        poblacion = int(input("Ingrese la población (número entero): ").strip())
        superficie = int(input("Ingrese la superficie en km2 (número entero): ").strip())
    except ValueError:
        print("Error: La población y la superficie deben ser valores numéricos enteros.")
        return

    # Si todo es correcto, creamos el diccionario y lo agregamos
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    lista_paises.append(nuevo_pais)
    print(f"Éxito: {nombre} ha sido agregado correctamente.")


def actualizar_pais(lista_paises):
    """Busca un país por nombre y permite actualizar su población y superficie."""
    print("\n--- ACTUALIZAR DATOS DE UN PAÍS ---")
    nombre_buscado = input("Ingrese el nombre del país a actualizar: ").strip().lower()
    
    # Buscamos el país iterando la lista
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre_buscado:
            print(f"País encontrado: {pais['nombre']} (Población: {pais['poblacion']}, Superficie: {pais['superficie']})")
            try:
                nueva_poblacion = int(input("Ingrese la nueva población: ").strip())
                nueva_superficie = int(input("Ingrese la nueva superficie: ").strip())
                
                # Actualizamos los valores en el diccionario
                pais["poblacion"] = nueva_poblacion
                pais["superficie"] = nueva_superficie
                
                print(f"Éxito: Los datos de {pais['nombre']} han sido actualizados.")
                return # Salimos de la función una vez actualizado
                
            except ValueError:
                print("Error: Los valores ingresados deben ser numéricos.")
                return
                
    # Si termina el bucle y no hizo 'return', es que no lo encontró
    print("Error: No se encontró ningún país con ese nombre.")

def mostrar_resultados(resultados):
    """Función auxiliar para imprimir listas de países formateadas."""
    if not resultados:
        # Mensaje claro si no hay resultados
        print("No se encontraron países que coincidan con los criterios de búsqueda.")
    else:
        print(f"\nSe encontraron {len(resultados)} resultados:")
        print("-" * 50)
        for p in resultados:
            print(f"- {p['nombre']} | Continente: {p['continente']} | Población: {p['poblacion']} | Sup: {p['superficie']} km2")
        print("-" * 50)

def quitar_tildes(texto):
    """
    Reemplaza las vocales con tilde por su equivalente sin tilde.
    Útil para hacer comparaciones de cadenas más robustas.
    """
    reemplazos = (
        ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
        ("Á", "a"), ("É", "e"), ("Í", "i"), ("Ó", "o"), ("Ú", "u")
    )
    for vocal_con_tilde, vocal_sin_tilde in reemplazos:
        texto = texto.replace(vocal_con_tilde, vocal_sin_tilde)
    return texto

def buscar_pais_nombre(lista_paises):
    """Busca países por coincidencia exacta o parcial en su nombre (ignorando tildes y mayúsculas)."""
    print("\n--- BUSCAR PAÍS POR NOMBRE ---")
    busqueda_cruda = input("Ingrese el nombre (o parte de él) a buscar: ").strip()
    
    # Normalizamos la búsqueda: quitamos tildes y pasamos a minúsculas
    busqueda = quitar_tildes(busqueda_cruda).lower()
    
    resultados = []
    for pais in lista_paises:
        # Normalizamos también el nombre del país guardado
        nombre_normalizado = quitar_tildes(pais["nombre"]).lower()
        if busqueda in nombre_normalizado:
            resultados.append(pais)
            
    mostrar_resultados(resultados)


def filtrar_por_continente(lista_paises):
    """Filtra y muestra los países que pertenecen a un continente específico (ignorando tildes)."""
    print("\n--- FILTRAR POR CONTINENTE ---")
    continente_crudo = input("Ingrese el continente: ").strip()
    
    # Normalizamos la entrada del usuario
    continente_buscado = quitar_tildes(continente_crudo).lower()
    
    resultados = []
    for pais in lista_paises:
        # Normalizamos el continente guardado
        continente_normalizado = quitar_tildes(pais["continente"]).lower()
        if continente_normalizado == continente_buscado:
            resultados.append(pais)
            
    mostrar_resultados(resultados)


def filtrar_por_rango_poblacion(lista_paises):
    """Filtra países cuya población esté dentro de un rango numérico dado."""
    print("\n--- FILTRAR POR RANGO DE POBLACIÓN ---")
    try:
        min_pob = int(input("Ingrese la población mínima: ").strip())
        max_pob = int(input("Ingrese la población máxima: ").strip())
    except ValueError:
        print("Error: Los valores ingresados deben ser numéricos enteros.")
        return

    resultados = []
    for pais in lista_paises:
        if min_pob <= pais["poblacion"] <= max_pob:
            resultados.append(pais)
            
    mostrar_resultados(resultados)


def filtrar_por_rango_superficie(lista_paises):
    """Filtra países cuya superficie esté dentro de un rango numérico dado."""
    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")
    try:
        min_sup = int(input("Ingrese la superficie mínima (km2): ").strip())
        max_sup = int(input("Ingrese la superficie máxima (km2): ").strip())
    except ValueError:
        print("Error: Los valores ingresados deben ser numéricos enteros.")
        return

    resultados = []
    for pais in lista_paises:
        if min_sup <= pais["superficie"] <= max_sup:
            resultados.append(pais)
            
    mostrar_resultados(resultados)

def ordenar_paises(lista_paises):
    """Ordena la lista de países según el criterio elegido."""
    print("\n--- ORDENAR PAÍSES ---")
    print("1. Por Nombre (A-Z)")
    print("2. Por Población (Mayor a menor)")
    print("3. Por Superficie (Ascendente o Descendente)")
    
    opcion = input("Seleccione el criterio (1-3): ").strip()
    
    if opcion == '1':
        # sorted() con lambda ordena tomando el valor de la clave "nombre"
        lista_ordenada = sorted(lista_paises, key=lambda x: x["nombre"])
        print("\nPaíses ordenados por Nombre (A-Z):")
        mostrar_resultados(lista_ordenada)
        
    elif opcion == '2':
        # reverse=True lo ordena de mayor a menor
        lista_ordenada = sorted(lista_paises, key=lambda x: x["poblacion"], reverse=True)
        print("\nPaíses ordenados por Población (Mayor a Menor):")
        mostrar_resultados(lista_ordenada)
        
    elif opcion == '3':
        orden = input("¿Desea orden (A)scendente o (D)escendente?: ").strip().upper()
        if orden == 'A':
            lista_ordenada = sorted(lista_paises, key=lambda x: x["superficie"])
            print("\nPaíses ordenados por Superficie (Menor a Mayor):")
            mostrar_resultados(lista_ordenada)
        elif orden == 'D':
            lista_ordenada = sorted(lista_paises, key=lambda x: x["superficie"], reverse=True)
            print("\nPaíses ordenados por Superficie (Mayor a Menor):")
            mostrar_resultados(lista_ordenada)
        else:
            print("Error: Letra no válida. Ingrese A o D.")
    else:
        print("Error: Opción de ordenamiento no válida.")


def mostrar_estadisticas(lista_paises):
    """Calcula y muestra estadísticas clave del dataset de países."""
    print("\n--- ESTADÍSTICAS ---")
    
    if not lista_paises:
        print("No hay datos de países para calcular estadísticas.")
        return

    # 1. País con mayor y menor población usando max() y min()
    pais_mayor_pob = max(lista_paises, key=lambda x: x["poblacion"])
    pais_menor_pob = min(lista_paises, key=lambda x: x["poblacion"])
    
    print(f"País con mayor población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']} hab.)")
    print(f"País con menor población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']} hab.)")

    # 2. Promedio de población y superficie
    total_poblacion = sum(p["poblacion"] for p in lista_paises)
    total_superficie = sum(p["superficie"] for p in lista_paises)
    cantidad_paises = len(lista_paises)
    
    # Redondeamos a 2 decimales para que quede más prolijo
    promedio_pob = total_poblacion / cantidad_paises
    promedio_sup = total_superficie / cantidad_paises
    
    print(f"Promedio de población: {promedio_pob:.2f} hab.")
    print(f"Promedio de superficie: {promedio_sup:.2f} km2")

    # 3. Cantidad de países por continente usando un diccionario auxiliar
    conteo_continentes = {}
    for p in lista_paises:
        continente = p["continente"]
        if continente in conteo_continentes:
            conteo_continentes[continente] += 1
        else:
            conteo_continentes[continente] = 1
            
    print("\nCantidad de países por continente:")
    for cont, cantidad in conteo_continentes.items():
        print(f"- {cont}: {cantidad}")

def mostrar_menu():
    """Imprime las opciones del menú principal completas."""
    print("\n" + "="*40)
    print("      SISTEMA DE GESTIÓN DE PAÍSES      ")
    print("="*40)
    print("1. Agregar un país")
    print("2. Actualizar población y superficie")
    print("3. Buscar un país por nombre")
    print("4. Filtrar por continente")
    print("5. Filtrar por rango de población")
    print("6. Filtrar por rango de superficie")
    print("7. Ordenar países")
    print("8. Mostrar estadísticas")
    print("9. Salir")
    print("="*40)

# ==========================================
# Bloque principal de ejecución
# ==========================================
if __name__ == "__main__":
    archivo_csv = "paises.csv"
    datos_paises = cargar_paises(archivo_csv)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-9): ").strip()
        
        if opcion == '1':
            agregar_pais(datos_paises)
        elif opcion == '2':
            actualizar_pais(datos_paises)
        elif opcion == '3':
            buscar_pais_nombre(datos_paises)
        elif opcion == '4':
            filtrar_por_continente(datos_paises)
        elif opcion == '5':
            filtrar_por_rango_poblacion(datos_paises)
        elif opcion == '6':
            filtrar_por_rango_superficie(datos_paises)
        elif opcion == '7':
            ordenar_paises(datos_paises)
        elif opcion == '8':
            mostrar_estadisticas(datos_paises)
        elif opcion == '9':
            print("Saliendo del sistema... ¡Éxitos con el TPI!")
            break
        else:
            print("Error: Opción no válida. Ingrese un número del 1 al 9.")