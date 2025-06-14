Grimaud Calculator
Uma calculadora simples em Python, empacotada para PyPI, oferecendo operações básicas como adição, subtração, multiplicação e divisão.

Instalação
Você pode instalar a grimaud_calculator via pip:

pip install grimaud_calculator

Uso
Para usar a calculadora, você pode importá-la em seu script Python ou executá-la diretamente:

Como módulo (importar e usar funções)
from grimaud_calculator.operations import add, subtract, multiply, divide

resultado_soma = add(10, 5)
print(f"10 + 5 = {resultado_soma}")

resultado_divisao = divide(20, 4)
print(f"20 / 4 = {resultado_divisao}")

Como aplicação interativa
Você pode executar o módulo calculator diretamente se ele for o ponto de entrada principal do seu pacote:

python -m grimaud_calculator.calculator

Isso iniciará o menu interativo da calculadora.

Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório do GitHub.

Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.