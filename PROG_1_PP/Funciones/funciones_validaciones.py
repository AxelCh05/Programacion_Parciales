
def validar_caso_vacio(cadena:str)->bool:
    """Valida si la cadena esta vacia o no.

    Args:
        cadena (str): Recibe una cadena para validar 

    Returns:
        bool: retorna True si la cadena tiene elementos o False si la cadena esta vacia.
    """
    bandera = False
    if len(cadena) != 0:
        bandera = True
    return bandera

def pasar_caracter_mayuscula(caracter:str)->str:
    """Recibe un caracter alfabético y utilizando su valor en el código ASCII, lo convierte en mayúscula
    en caso de ser minúscula.

    Args:
        caracter (str): Recibe un caracter que se desea convertir

    Returns:
        str: Retorna el carácter convertido a mayúscula.
    """
    valor = ord(caracter)
    if valor >= 65 and valor <= 90:
        valor = chr(valor)
    else:
        valor = valor -32
        valor = chr(valor)
    return valor

def validar_rango_numerico(limite_inferior:int, limite_superior:int, validar:int)->bool:
    """Verifica si un número entero se encuentra dentro de un rango determinado.

    Args:
        limite_inferior (int): El valor mínimo permitido del rango.
        limite_superior (int): El valor máximo permitido del rango.
        validar (int): El número entero que se desea comprobar.

    Returns:
        bool: Retorna True si el número se encuentra dentro del rango, o False en caso contrario.
    """
    minimo = limite_inferior
    maximo = limite_superior
    bandera = False                                                                 
    if validar >= minimo and validar <= maximo:
        bandera = True
    return bandera

def validar_caracter_numerico(caracter:str)->bool:
    """Valida si el caracter ingresado es un caracter numérico

    Args:
        caracter (str): Recibe un caracter de tipo string que se desea validar.

    Returns:
        bool: Retorna True si el caracter recibido es un caracter numerico y False caso contrario.
    """
    valor = ord(caracter)
    retorno = True
    if valor < 48 or valor > 57:
        retorno = False
    return retorno

def validar_cadena_numerico(cadena:str)->bool:
    """Valida si el parametro recibido es una cadena numérica.

    Args:
        cadena (str): Recibe un cadena de string que se desea validar

    Returns:
        bool: Retorna True si la cadena es numerica o False en caso contrario.
    """
    retorno = True
    for i in cadena:
        if not validar_caracter_numerico(i):
            retorno = False
            break
    return retorno

def validar_cadena_entero(cadena:str)->bool:
    """ Valida si el parametro recibido es una cadena de enteros o no.
    Args:
        cadena (str): Cadena que se desea validar. 

    Returns:
        bool: Retorna True si la cadena es un entero o devuelve False en caso contrario.
    """
    retorno = True
    if len(cadena) == 1 and cadena == "-":
        retorno = False
    else:
        posicion = 0
        for i in cadena:
            if ord(i) == 45:
                if posicion != 0:
                    retorno = False
                    break
            elif not validar_caracter_numerico(i):
                retorno = False
                break
            posicion += 1
    return retorno


def validar_caracter_alfabetico(caracter:str)->bool:
    """Valida si el parametro recibido es un carácter alfabético o no.
    Args:
        caracter (str): Carácter que se desea validar.
    Returns:
        bool: Devuelve True si el carácter es alfabético o devuelve False en caso contrario.
    """
    valor = ord(caracter)
    retorno = False
    if (valor > 64 and valor < 91) or (valor > 96 and valor < 123) or valor == 32:
        retorno = True
    return retorno

def validar_cadena_alfabetico(cadena:str)->bool:
    """Valida si el parametro recibido es una cadena alfabético o no.
    Args:
        cadena (str): Cadena que se desea validar.
    Returns:
        bool: Retorna True si la cadena es solo alfabético o devuelve False en caso contrario.
    """
    retorno = True
    for i in cadena:
        if not validar_caracter_alfabetico(i): 
            retorno = False
            break
    return retorno


















