"""
Módulo operations.py: Contém as funções de operações aritméticas básicas.
"""

def add(a, b):
    """
    Soma dois números.
    Args:
        a (float ou int): O primeiro número.
        b (float ou int): O segundo número.
    Returns:
        float ou int: A soma dos dois números.
    """
    return a + b

def subtract(a, b):
    """
    Subtrai o segundo número do primeiro.
    Args:
        a (float ou int): O primeiro número.
        b (float ou int): O segundo número.
    Returns:
        float ou int: A diferença entre os dois números.
    """
    return a - b

def multiply(a, b):
    """
    Multiplica dois números.
    Args:
        a (float ou int): O primeiro número.
        b (float ou int): O segundo número.
    Returns:
        float ou int: O produto dos dois números.
    """
    return a * b

def divide(a, b):
    """
    Divide o primeiro número pelo segundo.
    Args:
        a (float ou int): O numerador.
        b (float ou int): O denominador.
    Returns:
        float: O quociente da divisão.
    Raises:
        ValueError: Se o denominador for zero.
    """
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b
