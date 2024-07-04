# Inicializa a variável para armazenar a soma
soma = 0

# Usa um loop for para percorrer os números de 1 a 10
for numero in range(1, 11):
    # Verifica se o número é ímpar
    if numero % 2 != 0:
        # Adiciona o número ímpar à soma
        soma += numero

# Exibe o resultado
print("A soma dos números ímpares de 1 a 10 é:", soma)
