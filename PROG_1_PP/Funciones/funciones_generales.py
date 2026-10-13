from Funciones.funciones_validaciones import *

def crear_lista(cantidad:int, elemento = 0)->list:
    """Crea una lista con una cantidad determinada de elementos.

    Args:
        cantidad (int): Cantidad de elementos que tendrá la lista.
        elemento (int, optional): Valor con el que se rellenará la lista. Defaults to 0.

    Returns:
        list: Retorna lista con la cantidad de elementos especificada.
    """
    lista = [elemento] * cantidad
    return lista

def mostrar_estructura(promedio:bool = True):
    """Imprime por consola la cabecera en forma de tabla para visualizar un informe de estudiantes.

    Args:
        promedio (bool, optional): Usa un criterio booleano para definir si incluye o no la columna
        de promedios. Defaults to True.
    """
    if promedio:
        print("=" * 80)
        print("                 INFORME DE CALIFICACIONES DE ESTUDIANTES           ")
        print("=" * 80)
        print(f"|  {"LEGAJO":<8}| {"NOMBRE Y APELLIDO":<18} | {"GENERO":^7} | {"PARCIAL 1":^11} | {"PARCIAL 2":^11} | {"PROMEDIO":^11} |")
        print("-" * 80)
    else:
        print("=" * 80)
        print("                 INFORME DE CALIFICACIONES DE ESTUDIANTES           ")
        print("=" * 80)
        print(f"|  {"LEGAJO":<8}| {"NOMBRE Y APELLIDO":<18} | {"GENERO":^7} | {"PARCIAL 1":^11} | {"PARCIAL 2":^11} |")
        print("-" * 80)


def pedir_legajo(mensaje:str)->int:
    """Pide por consola el ingreso de un numero de legajo, validando que la entrada no esté vacia,
    sea una cadena numérica de enteros y represente un valor igual o mayor a cero. Repite el pedido
    en caso sea erroneo.

    Args:
        mensaje (str): El texto que se le muestra al usuario al pedir legajo. 

    Returns:
        int: Retorna el número de legajo validado y convertido en entero.
    """
    legajo = input(mensaje)
    bandera = True
    while bandera:
        if validar_cadena_entero(legajo) and validar_caso_vacio(legajo):
            legajo = int(legajo)
            if legajo >= 0:
                bandera = False
            else:
                legajo = input(f"Error. {mensaje}")
        else:
            legajo = input(f"Error. {mensaje}")
    return legajo



def pedir_nombre_apellido(mensaje:str)->str: 
    """Pide por consola el ingreso de nombre y apellido, validando que no esté vacio y que contenga
    caracteres alfabéticos. Repite el pedido en caso sea erroneo.

    Args:
        mensaje (str): El texto que se le muestra al usuario al pedir nombre y apellido. 

    Returns:
        str: Retorna el nombre y apellido validado y convertido en str.
    """
    nombre_apellido = input(mensaje)
    bandera = True
    while bandera:
        if validar_caso_vacio(nombre_apellido) and validar_cadena_alfabetico(nombre_apellido):
            bandera = False
        else:    
            nombre_apellido = input(f"Error. {mensaje}")
    return nombre_apellido



def pedir_genero(mensaje:str)->str:
    """ Pide por consola el ingreso del genero del alumno, validando que corresponda a una de las opciones permitidas. 'F' 'M' 'X'
    o sus minúsculas. En caso de ingresar una minuscula, lo convierte a mayuscula.

    Args:
        mensaje (str): El texto que se le muestra al usuario al pedir genero.

    Returns:
        str: retorna el género validado y en mayuscula.
    """
    genero = input(mensaje)
    while genero != "F" and genero != "M" and genero != "X" and genero != "f" and genero != "m" and genero != "x": 
        genero = input(f"Error. {mensaje}")

    if genero == "f" or genero == "m" or genero == "x":
        genero = pasar_caracter_mayuscula(genero)

    return genero


def pedir_nota(mensaje:str)->int:
    """Pide por consola el ingreso de una nota, validando que no esté vacio, que sea una cadena numérica,
    y que se encuentre en un rango (del 1 al 10). Repite la solicitud en caso de ser erroneo.

    Args:
        mensaje (str): El texto que se le muestra al usuario al solicitar una nota.

    Returns:
        int: Retorna una nota validada y convertida a tipo entero.
    """
    nota = input(mensaje)
    bandera = True
    while bandera:
        if validar_caso_vacio(nota) and validar_cadena_numerico(nota):
            nota = int(nota)
            if validar_rango_numerico(1,10,nota):
                bandera = False
            else:
                nota = input(f"Error. {mensaje}")
        else:
            nota = input(f"Error. {mensaje}")
    return nota



def mostrar_alumno(legajo: list, nombre: list, genero: list, nota1: list, nota2: list):
    """Imprime por consola en formato de tabla  los datos de los alumnos
    Args:
        legajo (list): Lista paralela de legajos.
        nombre (list): Lista paralela de nombre y apellido.
        genero (list): Lista paralela de género.
        nota1 (list): Lista paralela de notas del primer parcial.
        nota2 (list): Lista paralela de notas del segundo parcial.
    """
    print(f"| {legajo:<8} | {nombre:<18} | {genero:^7} | {nota1:^11} | {nota2:^11} |", end = "")



def mostrar_informe(legajo:list, nombre:list, genero:list, nota1:list, nota2:list):
    """Imprime por consola el informe completo de los estudiantes.
    Args:
        legajo (list): Lista paralela con los legajos.
        nombre (list): Lista paralela con los nombres y apellidos.
        genero (list): Lista paralela con los generos.
        nota1 (list): Lista paralela con las notas del primera parcial.
        nota2 (list): Lista paralela con las notas del segundo parcial.
    """
    mostrar_estructura(False)
    for i in range(len(legajo)):
        mostrar_alumno(legajo[i], nombre[i], genero[i], nota1[i], nota2[i])
        print()


def promediar_alumnos(lista_1:list, lista_2:list)->list:
    """Calcula el promedio de las notas de cada alumno

    Args:
        lista_1 (list): Lista con las notas del primer parcial de los alumnos.
        lista_2 (list): Lista con las notas del segundo parcial de los alumnos.

    Returns:
        list: Lista con los promedios de cada alumno, redondeados a dos decimales.
    """
    lista_promedios = crear_lista(len(lista_1))    
    for i in range(len(lista_1)):
        acumulador = lista_1[i] + lista_2[i]
        promedio = acumulador / 2    
        lista_promedios[i] = round(promedio,2)
    return lista_promedios

def mayor_promedio(lista_promedios:list)->list:
    """Busca el valor máximo dentro de una lista y retorna una lista con el o los indices 
    de dicho valor. 

    Args:
        lista_promedios (list): Lista que contiene los promedios numéricos de los alumnos.

    Returns:
        list: Retorna una lista de indices que representan la ubicacion de los datos de los estudiantes.
    """
    lista_indices_mayor = [0]
    mayor = lista_promedios[0]
    for i in range(1, len(lista_promedios)):
        if mayor < lista_promedios[i]:
            mayor = lista_promedios[i]
            lista_indices_mayor = [i]
        elif mayor == lista_promedios[i]:
            lista_indices_mayor += [i]
    return lista_indices_mayor


def mostrar_promedios_mayores(legajo: list, nombre: list, genero: list, nota1: list, nota2: list, promedio:list, lista:list):
    """Imprime por consola un informe  que incluye la columna de promedios. 

    Args:
        legajo (list): Lista paralela con los legajos.
        nombre (list): Lista paralela con los nombres y apellidos.
        genero (list): Lista paralela con los géneros.
        nota1 (list): Lista paralela con las notas del primer parcial.
        nota2 (list): Lista paralela con las notas del segundo parcial
        promedio (list): Lista paralela con los promedios calculados de los alumnos.
        lista (list): Lista paralela con lista de indices opcional para filtrar si se muestra con promedios o no. 
    """
    mostrar_estructura(True)
    if lista:
        for i in range(len(lista)):
            mostrar_alumno(legajo[lista[i]], nombre[lista[i]], genero[lista[i]], nota1[lista[i]], nota2[lista[i]])
            print(f"   {promedio[lista[i]]}   | ", end = "")
            print() 
    else:
        for i in range(len(legajo)):
            mostrar_alumno(legajo[i], nombre[i], genero[i], nota1[i], nota2[i])
            print(f"   {promedio[i]}   | ", end = "")
            print()  
        

def intercambiar(lista:list, i:int, j:int):
    """Intercambia de posición dos elementos de una misma lista (SWAP).
    Args:
        lista (list): Lista que contiene los elementos a intercambiar.
        i (int): El indice del primer elemento.
        j (int): El indice del segundo elemento a intercambiar.
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def ordenar_promedios_ASC_DESC(promedio:list, legajo:list, nombre_apellido:list, genero:list, nota_1:list, nota_2:list, orden = True):
    """Realiza un ordenamiento con manipulaciones de multiples listas en paralelo con un criterio booleano se puede cambiar el orden
    de forma ascendente o descendete.

    Args:
        promedio (list): Lista de promedios que se toma como base para realizar el ordenamiento.
        legajo (list): Lista paralela con los legajos de los alumnos.
        nombre_apellido (list): Lista paralela con los nombres y apellidos de los alumnos.
        genero (list): Lista paralela con los generos de los alumnos.
        nota_1 (list): Lista paralela con las notas del primer parcial.
        nota_2 (list): Lista paralela con las notas del segundo parcial.
        orden (bool, optional): Define el criterio de ordenamiento: True para ordenar de forma ascendente y
        False para descendente. Defaults to True.
    """
    cantidad = len(legajo)

    for i in range(cantidad - 1):
        for j in range(i +1, cantidad):
            if orden:
                if promedio[i] > promedio[j]:
                    intercambiar(promedio, i, j)
                    intercambiar(legajo, i, j)
                    intercambiar(nombre_apellido, i, j)
                    intercambiar(genero, i, j)
                    intercambiar(nota_1, i, j)
                    intercambiar(nota_2, i, j)
            elif promedio[i] < promedio[j]:
                    intercambiar(promedio, i, j)
                    intercambiar(legajo, i, j)
                    intercambiar(nombre_apellido, i, j)
                    intercambiar(genero, i, j)
                    intercambiar(nota_1, i, j)
                    intercambiar(nota_2, i, j)

def buscar_mostrar_por_legajo(legajo:list, nombre:list, genero:list, nota1:list, nota2:list):
    """Pide al usuario por consola el número de legajo para buscarlo y mostrarlo en consola.

    Args:
        legajo (list): Lista paralela con los legajos de los alumnos.
        nombre (list): Lista paralela con los nombres y apellidos de los alumnos.
        genero (list): Lista paralela con los generos de los alumnos.
        nota1 (list): Lista paralela con las notas del primer parcial.
        nota2 (list): Lista paralela con las notas del segundo parcial.
    """
    numero_legajo = pedir_legajo("Ingrese un legajo para buscar al alumno: ")
    for i in range(len(legajo)):
        if numero_legajo == legajo[i]:
            mostrar_estructura(False)
            mostrar_alumno(legajo[i], nombre[i], genero[i], nota1[i], nota2[i])
            print()
            break


def cargar_datos(cantidad:int)->list:
    """ Pide e ingresa por consola los datos correspondientes a una cantidad determinada de estudiantes,

    Args:
        cantidad (int): Recibe la cantidad de alumnos que desea registrar en el sistema.

    Returns:
        list: Retorna 5 listas con los datos correspondientes de cada alumno en el orden ingresado.
    """
    lista_legajos = []
    lista_nombre_apellido = []
    lista_genero = []
    lista_notas_1 = []
    lista_notas_2 = []

    for i in range(cantidad):
        legajo = pedir_legajo("Ingrese el legajo del alumno: ")
        nombre_apellido = pedir_nombre_apellido("Ingrese el nombre y el apellido: ")
        genero = pedir_genero("Ingrese el genero del alumno ('M' 'F' 'X'): ")
        nota_1 = pedir_nota("Ingrese la nota del Primer Parcial: ")
        nota_2 = pedir_nota("Ingrese la nota del Segundo Parcial: ")

        lista_legajos += [legajo]
        lista_nombre_apellido += [nombre_apellido]
        lista_genero += [genero]
        lista_notas_1 += [nota_1]
        lista_notas_2 += [nota_2]

    return lista_legajos, lista_nombre_apellido, lista_genero, lista_notas_1, lista_notas_2






