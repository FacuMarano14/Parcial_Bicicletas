from os import system
from random import randint
import json

def limpiar_pantalla():
    """Limpia la pantalla
    """
    system("cls")
#-------------------------------------------------------------------------------------------------------------------------------------
def pausar():
    """Pausa la animacion entre operaciones
    """
    system("pause")
#-------------------------------------------------------------------------------------------------------------------------------------
def menu()-> str:
    """Menu de opciones

    Returns:
        str: opcion elegida
    """
    limpiar_pantalla()
    print("Menu de opciones")
    print("1 - Cargar Datos")
    print("2 - Imprimir Lista")
    print("3 - Tiempos")
    print("4 - Ganador")
    print("5 - Filtrar por Tipo")
    print("6 - Promedio por Tipo")
    print("7 - Posiciones")
    print("8 - Guardar Posiciones")
    print("9 - Salir")
    opcion = input("Ingrese opcion: ")
    return opcion
#-------------------------------------------------------------------------------------------------------------------------------------
def get_acutal_path(nombre_archivo:str)->str:
    """Obtiene la ruta completa del archivo

    Args:
        nombre_archivo (str): Nombre del archivo

    Returns:
        str: Ruta del archivo
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)
#-------------------------------------------------------------------------------------------------------------------------------------
def cargar_datos(nombre_archivo:str)-> list:
    """Carga los datos de un archivo CSV y los almacena en una lista de diccionarios.

    Returns:
        list: Lista de diccionarios con los datos del archivo CSV
    """
    with open(get_acutal_path(nombre_archivo), "r", encoding="utf-8") as archivo:
        lista = []
        encabezado = archivo.readline().strip("\n").split(",")
        for linea in archivo.readlines():
            bicicleta = {}
            linea = linea.strip("\n").split(",")
            
            id_bike, nombre, tipo, tiempo = linea
            bicicleta["id_bike"] = int(id_bike)
            bicicleta["nombre"] = nombre
            bicicleta["tipo"] = tipo
            bicicleta["tiempo"] = int(tiempo)
            lista.append(bicicleta)
    return lista
#-------------------------------------------------------------------------------------------------------------------------------------
def imprimir_pantalla(lista: list):
    """Muestra la lista que se le pase

    Args:
        lista (list): lista que se muestra en pantalla
    """
    for dato in lista:
        print(f"{dato['id_bike']}, {dato['nombre']}, {dato['tipo']}, {dato['tiempo']}")
#-------------------------------------------------------------------------------------------------------------------------------------
def mapear_lista(procesadora, lista:list)-> list:
    """_summary_

    Args:
        procesadora (_type_): funcion lambda a desarrollar
        lista (list): lista a mapear

    Returns:
        _type_: lista mapeada
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append(procesadora(el))
    return lista_retorno
#-------------------------------------------------------------------------------------------------------------------------------------
def filtrar_listas(funcion,lista:list)->list:                       #sirve para filtrar cualquier lista con cualquier valor
    """filtrar_listas

    Args:
        funcion (_type_): ponemos lo que queramos que filtre nuestra funcion
        lista (list): pasamos la lista original 

    Returns:
        list: retorna la lista filtrada 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for el in lista:
        if funcion(el): 
            lista_retorno.append((el))
    return lista_retorno
#-------------------------------------------------------------------------------------------------------------------------------------
def asignar_tiempos(lista:list)->list:
    """Asigna tiempos aleatorios

    Args:
        lista (list): Le paso la lista con los tiempos en 0

    Returns:
        list: Le devuelvo la lista con valores aleatorios entre 50 y 120
    """
    for elem in lista:
        tiempo = randint(50,120)
        elem["tiempo"] = tiempo
    return lista
#-------------------------------------------------------------------------------------------------------------------------------------
def calcular_menor(lista:list)->int:
    """Calcula el numero mas pequeño de una lista

    Args:
        lista (list): Lista de numeros

    Raises:
        ValueError: Si la lista esta vacia lanza este error

    Returns:
        int: El numero mas pequeño de la lista
    """
    if not lista:
        raise ValueError("No esta definido el mayor de una lista vacia")
    
    flag = False
    for numero in lista:
        if flag == False or numero < num_menor:
            num_menor = numero
            flag = True
    return num_menor
#-------------------------------------------------------------------------------------------------------------------------------------
def mapear_tiempo_nombre(lista:list)->list:
    """Mapea lista de diccionarios a lista de tuplas

    Args:
        lista (list): lista de diccionarios con claves "tiempo" y "nombre"

    Returns:
        _type_: Lista de tuplas en la que cada tupla tiene tiempo y nombre
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append((el["tiempo"], el["nombre"]))
    return lista_retorno
#-------------------------------------------------------------------------------------------------------------------------------------
def ganador(lista:list):
    """Indica al ganador con menor tiempo en una lista de bicicletas

    Args:
        lista (list): Lista de diccionarios con información de bicicletas, incluyendo "tiempo" y "nombre".

    Returns:
        None: Imprime el nombre del ganador y su tiempo.
    """
    tiempo_nombre = mapear_tiempo_nombre(lista)
    ganador = calcular_menor(tiempo_nombre)
    mensaje = f"El ganador es: {ganador[1]} y su tiempo es {ganador[0]}"
    return print(mensaje)
#-------------------------------------------------------------------------------------------------------------------------------------
def mapear_tipo_tiempo(lista:list)->list:
    """Mapea una lista de diccionarios a una lista de tuplas (tipo, tiempo).

    Args:
        lista (list): Lista de diccionarios con claves "tipo" y "tiempo".

    Returns:
        list: Lista de tuplas donde cada tupla contiene el tipo y el tiempo.
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append((el["tipo"], el["tiempo"]))
    return lista_retorno
#-------------------------------------------------------------------------------------------------------------------------------------
def filtrar_por_tipo(lista:list, tipo_bici:str)->list:
    """Filtra una lista de bicicletas por tipo de bicicleta.

    Args:
        lista (list): Lista de diccionarios con información de bicicletas.
        tipo_bici (str): El tipo de bicicleta para filtrar.

    Returns:
        list: Lista filtrada de diccionarios que solo contienen el tipo de bicicleta especificado.
    """
    lista_retorno = []
    for el in lista:
        if el["tipo"] == tipo_bici:
            lista_retorno.append(el)
    return lista_retorno
#-------------------------------------------------------------------------------------------------------------------------------------
def guardar_archivo_csv(lista:list,nombre_archivo_csv)->any:
    """guardar_archivo_csv

    Args:
        lista (list): paso una lista
        nombre_archivo_csv (_type_): el nombre del archivo que quiero ponerle 

    Returns:
        any: no devuelve nada
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    with open(get_acutal_path(nombre_archivo_csv), "w", encoding="utf-8") as archivo: #hace lo mismo que el anterior pero aca pasa el nombre a mayusculas
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for persona in lista:
            values = list(persona.values())
            l = []
            for value in values:
                if isinstance(value,int):
                    l.append(str(value))
                elif isinstance(value,float):
                    l.append(str(value))
                else:
                    l.append(value)

            linea = ",".join(l) + "\n"
            archivo.write(linea)
#-------------------------------------------------------------------------------------------------------------------------------------
def totalizar_listas(lista:list)->int:
    """Suma todos los elementos de una lista de números.

    Args:
        lista (list): Lista de números.

    Returns:
        int: La suma de todos los números en la lista.
    """
    total = 0
    for numero in lista:
        total += numero
    return total
#-------------------------------------------------------------------------------------------------------------------------------------
def calcular_promedio_3(lista:list)->float:
    """Calcula el promedio de una lista de números.

    Args:
        lista (list): Lista de números.

    Returns:
        float: El promedio de los números en la lista.

    Raises:
        ValueError: Si la lista está vacía.
    """
    cant = len(lista)
    if cant == 0:
        raise ValueError("No esta definido el promedio de una lista vacia")
    return totalizar_listas(lista) / cant
#-------------------------------------------------------------------------------------------------------------------------------------
def filtrar_tipo_csv(lista:list)->any:
    """Filtra una lista de bicicletas por tipo y guarda los resultados en un archivo CSV.

    Args:
        lista (list): Lista de diccionarios con información de bicicletas.

    Returns:
        any: Resultado de la función guardar_archivo_csv.
    """
    tipo_bici = input("Indique tipo de bicicleta: ").upper()
    tipos_de_bici = filtrar_por_tipo(lista, tipo_bici)
    archivo_csv = guardar_archivo_csv(tipos_de_bici, f"filtro_bicis_{tipo_bici}.csv")
    return archivo_csv
#-------------------------------------------------------------------------------------------------------------------------------------
def promedio_tipo_bici(lista:list,target)->any:
    """Calcula el promedio de tiempo para un tipo específico de bicicleta.

    Args:
        lista (list): Lista de diccionarios con información de bicicletas.
        target (str): El tipo de bicicleta para el cual calcular el promedio.

    Returns:
        any: El promedio de tiempo para el tipo de bicicleta especificado.

    Raises:
        TypeError: Si el primer parámetro no es una lista.
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    tipo = filtrar_listas(lambda tiempo: (tiempo["tipo"] == target),lista)
    tiempo = mapear_lista(lambda tiempo: (tiempo["tiempo"]),tipo)
    promedio = calcular_promedio_3(tiempo)
    return promedio
#-------------------------------------------------------------------------------------------------------------------------------------
def promedios_por_tipo(lista:list)->str:
    """Calcula los promedios de tiempo para cada tipo de bicicleta y genera un mensaje.

    Args:
        lista (list): Lista de diccionarios con información de bicicletas.

    Returns:
        str: Mensaje con los promedios de tiempo por tipo de bicicleta.
    """
    bmx = promedio_tipo_bici(lista, "BMX")
    playera = promedio_tipo_bici(lista, "PLAYERA")
    mtb = promedio_tipo_bici(lista, "MTB")
    paseo = promedio_tipo_bici(lista, "PASEO")
    mensaje = f"Promedio BMX: {bmx:.2f}\nPromedio PLAYERA: {playera:.2f}\nPromedio MTB: {mtb:.2f}\nPromedio PASEO: {paseo:.2f}\n"
    return mensaje
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
def ordenar_ascendente_por_tiempo(lista)->list:
    """Ordena una lista de bicicletas en orden ascendente por tiempo.

    Args:
        lista (list): Lista de diccionarios con información de bicicletas.

    Returns:
        list: Lista ordenada en orden ascendente por tiempo.

    Raises:
        TypeError: Si el primer parámetro no es una lista.
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j]['tiempo'] < lista[min_idx]['tiempo']:
                min_idx = j
        # Intercambiar elementos
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    
    return lista
#-------------------------------------------------------------------------------------------------------------------------------------
def orden_tipo_tiempo_asc(lista:list)->list:
    """Filtra una lista de bicicletas por tipo y ordena los resultados en orden ascendente por tiempo.

    Args:
        lista (list): Lista de diccionarios con información de bicicletas.

    Returns:
        list: Lista filtrada y ordenada en orden ascendente por tiempo.
    """
    tipo_bici = input("Indique tipo de bici: ").upper()
    lista_filtrada = filtrar_listas(lambda tipo: tipo["tipo"] == tipo_bici,lista)
    orden_ascendente_tiempo = ordenar_ascendente_por_tiempo(lista_filtrada)
    return orden_ascendente_tiempo
#-------------------------------------------------------------------------------------------------------------------------------------
def guardar_archivo_json(archivo_json, bici)->None:
    """Guarda una lista de bicicletas en un archivo JSON.

    Args:
        archivo_json (str): El nombre del archivo JSON.
        bici (list): Lista de diccionarios con información de bicicletas.

    Returns:
        None
    """
    with open(get_acutal_path(archivo_json), "w", encoding="utf-8") as archivo_json:
        return json.dump(bici, archivo_json, indent = 4)
#-------------------------------------------------------------------------------------------------------------------------------------
def guardar_ascendente_tiempo_json(lista: list)->None:
    """Ordena una lista de bicicletas en orden ascendente por tiempo y guarda los resultados en un archivo JSON.

    Args:
        lista (list): Lista de diccionarios con información de bicicletas.

    Returns:
        None
    """
    orden_ascendente_tiempo = ordenar_ascendente_por_tiempo(lista)
    archivo_json = guardar_archivo_json("ord_asc_tiemp.json", orden_ascendente_tiempo)
    return archivo_json
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------