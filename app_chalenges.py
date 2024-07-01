# Função para verificar se um número é par ou ímpar
def verificar_paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar
resultado = verificar_paridade(numero)

# Exibe o resultado
print(f"O número {numero} é {resultado}.")
