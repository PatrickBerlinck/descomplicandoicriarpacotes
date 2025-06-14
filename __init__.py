"""
__init__.py: Este arquivo torna o diretório 'grimaud_calculator' um pacote Python.
Ele também expõe as principais funções dos módulos 'operations' e 'calculator'.
"""

# Importa as funções de operações básicas do módulo operations.py
from .operations import add, subtract, multiply, divide

# Importa a função principal da calculadora interativa do módulo calculator.py
from .calculator import calculate

# Define a versão do seu pacote. É uma boa prática incluir isso.
__version__ = "0.1.0"

# Opcionalmente, você pode definir quais nomes são importados
# quando alguém faz 'from grimaud_calculator import *'.
# Isso é útil para controlar a API pública do seu pacote.
__all__ = ["add", "subtract", "multiply", "divide", "calculate"]