# Cria uma lista de números (pode estar vazia para testar a exceção)
numeros = [8,20,45,63,250,20]

try:
    # Calcula a soma dos elementos da lista
    soma = sum(numeros)
    
    # Calcula a quantidade de elementos na lista
    quantidade = len(numeros)
    
    # Tenta calcular a média dos elementos da lista
    media = soma / quantidade
    
    # Exibe o resultado da média
    print("A média dos valores na lista é:", media)
except ZeroDivisionError as e:
    # Captura e lida com a exceção de divisão por zero
    print("Erro: não é possível calcular a média de uma lista vazia.")
except Exception as e:
    # Captura e lida com qualquer outra exceção
    print("Ocorreu um erro inesperado:", e)
