from Funciones.funciones_generales import *
#from Datos.datos_alumnos import *


seguir = "si"
bandera = False
promediado = False
while seguir == "si":
    opciones = input("Elija una de las siguientes opciones: \n\t1- Cargar datos de los alumnos.\n\t2- Mostrar datos de los alumnos.\n\t3- Promediar notas de los alumnos. \n\t4- Mostrar los promedios (ASC / DESC).\n\t5- Mostrar el/los estudiante/s con mayor promedio.\n\t6- Buscar estudiante por legajo.\n\t7- Salir del programa.\n")

    match opciones:
        case "1":
            if bandera == False:
                lista_legajos, lista_nombre_apellido, lista_genero, lista_notas_1, lista_notas_2 = cargar_datos(4)
                bandera = True
        case "2":
            if bandera == True:
                mostrar_informe(lista_legajos, lista_nombre_apellido, lista_genero, lista_notas_1, lista_notas_2)
        case "3":
            if bandera == True:
                lista_promedios = promediar_alumnos(lista_notas_1, lista_notas_2)
                lista = []
                mostrar_promedios_mayores(lista_legajos, lista_nombre_apellido, lista_genero, lista_notas_1, lista_notas_2, lista_promedios,lista)
                promediado = True
        case "4":
            if bandera == True and promediado == True:
                ordenar_promedios_ASC_DESC(lista_promedios, lista_legajos, lista_nombre_apellido, lista_genero, lista_notas_1, lista_notas_2, False)
                mostrar_promedios_mayores(lista_legajos, lista_nombre_apellido, lista_genero, lista_notas_1, lista_notas_2, lista_promedios,lista)
        case "5":
            if bandera == True and promediado == True:
                lista_promedio_mayor = mayor_promedio(lista_promedios)
                mostrar_promedios_mayores(lista_legajos, lista_nombre_apellido, lista_genero, lista_notas_1, lista_notas_2, lista_promedios, lista_promedio_mayor)
        case "6":
            buscar_mostrar_por_legajo(lista_legajos, lista_nombre_apellido, lista_genero, lista_notas_1, lista_notas_2)
        case "7":
            print("EL PROGRAMA SE CERRÓ CORRECTAMENTE.")
            break
    seguir = input("Desea seguir? s/n: ")






