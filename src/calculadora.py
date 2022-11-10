def sumar(*args: float) -> float:
    """sumar Funcion para sumar todos los valores que se pasen como argumento

    :return: Devuelve la suma de los numeros
    :rtype: float
    """
    total = 0
    if len(args) < 2:
        raise Exception("Argumentos Insuficientes")
    for numero in args:
        total += numero
    return total


def restar(*args: float) -> float:
    """sumar Funcion para restar todos los valores que se pasen como argumento

    :return: Devuelve la resta de los numeros
    :rtype: float
    """
    total = 0

    if len(args) < 2:
        raise Exception("Argumentos Insuficientes")

    for numero in args:
        total -= numero
    return total


def multiplicar(*args: float) -> float:
    """sumar Funcion para multiplicar todos los valores que se pasen como
     argumento

    :return: Devuelve el producto de los numeros
    :rtype: float
    """

    total = 1
    if len(args) < 2:
        raise Exception("Argumentos Insuficientes")

    for numero in args:
        total *= numero
    return total


def dividir(*args: float) -> float:
    """sumar Funcion para dividir todos los valores que se pasen como argumento

    :return: Devuelve el resultado de la division de los numeros que se pasen
     como argumento
    :rtype: float
    """

    if len(args) < 2:
        raise Exception("Argumentos Insuficientes")

    for ciclo in range(len(args)):
        try:
            if ciclo == 0:
                total = args[0]
            else:
                total /= args[ciclo]
        except ZeroDivisionError:
            raise ZeroDivisionError("No es posible dividir por 0")
            
    return total