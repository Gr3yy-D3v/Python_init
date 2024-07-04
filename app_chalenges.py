# Solicita ao usuário que insira um número
numero = int(input("Digite um número para ver sua tabuada: "))

# Usa um loop for para percorrer os números de 1 a 10
for o in range(1, 11):
    resultado = numero * o
    print(f"{numero} x {o} = {resultado}")
