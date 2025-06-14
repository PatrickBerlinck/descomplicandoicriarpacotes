"""
Módulo calculator.py: Contém a lógica principal da calculadora interativa.
"""
from .operations import add, subtract, multiply, divide

def get_numbers():
    """
    Solicita dois números ao usuário e valida a entrada.
    Returns:
        tuple: Uma tupla contendo os dois números (num1, num2).
    """
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            return num1, num2
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")

def calculate():
    """
    Função principal da calculadora, que executa o loop interativo.
    """
    print("Bem-vindo à Calculadora Grimaud!")
    while True:
        print("\nSelecione uma operação:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Sair")

        choice = input("Digite sua escolha (1/2/3/4/5): ")

        if choice == '5':
            print("Obrigado por usar a calculadora!")
            break
        elif choice in ('1', '2', '3', '4'):
            num1, num2 = get_numbers()
            result = None
            operation_symbol = ""

            if choice == '1':
                result = add(num1, num2)
                operation_symbol = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation_symbol = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation_symbol = "*"
            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    operation_symbol = "/"
                except ValueError as e:
                    print(f"Erro: {e}")
                    continue # Volta ao menu principal após erro de divisão por zero

            if result is not None:
                print(f"Resultado: {num1} {operation_symbol} {num2} = {result}")
        else:
            print("Escolha inválida. Por favor, tente novamente.")

# Permite que o módulo seja executado diretamente
if __name__ == "__main__":
    calculate()
