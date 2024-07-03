# Define os valores esperados para o nome de usuário e a senha
usuario_esperado = "usuario123"
senha_esperada = "senha123"

# Solicita ao usuário que insira o nome de usuário e a senha
usuario_fornecido = input("Digite o nome de usuário: ")
senha_fornecida = input("Digite a senha: ")

# Verifica se o nome de usuário e a senha correspondem aos valores esperados
if usuario_fornecido == usuario_esperado and senha_fornecida == senha_esperada:
    print("Acesso concedido.")
else:
    print("Nome de usuário ou senha incorretos. Acesso negado.")
