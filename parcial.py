from funciones import *

seguir = True


while seguir:
    match menu():
        case "1":
            lista_bicicletas = cargar_datos("bicicletas.csv")
        case "2":
            imprimir_pantalla(lista_bicicletas)
            pausar()
        case "3":
            asignar_tiempos(lista_bicicletas)
            imprimir_pantalla(lista_bicicletas)
            pausar()
        case "4":
            ganador(lista_bicicletas)
            pausar()
        case "5":
            filtrar_tipo_csv(lista_bicicletas)
            pausar()
        case "6":
            promedios = promedios_por_tipo(lista_bicicletas)
            print(promedios)
            pausar()
        case "7":
            ord_tip_tiemp_asc = orden_tipo_tiempo_asc(lista_bicicletas)
            print(ord_tip_tiemp_asc)
            pausar()
        case "8":
            guardar_ascendente_tiempo_json(ord_tip_tiemp_asc)
        case "9":
            seguir = False