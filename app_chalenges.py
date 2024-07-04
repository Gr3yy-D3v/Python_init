# Cria uma lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicializa a variável para armazenar a soma
soma = 0

try:
    # Usa um loop for para percorrer todos os elementos da lista
    for numero in numeros:
        soma += numero
    
    # Exibe o resultado da soma
    print("A soma de todos os elementos da lista é:", soma)
except TypeError as a:
    # Captura e lida com a exceção do tipo TypeError
    print("Ocorreu um erro ao tentar somar os elementos da lista:", a)
except Exception as a:
    # Captura e lida com qualquer outra exceção
    print("Ocorreu um erro inesperado:", a)
