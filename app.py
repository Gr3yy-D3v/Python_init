print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█""")

print('1. Cadastrar Restaurante')
print('2. listar Restaurante')
print('3. ativar Restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma das opções: '))


if opcao_escolhida == 1 :
    print('Cadastrar restaurante')
elif opcao_escolhida == 2 :
    print('Listar restaurantes')
elif opcao_escolhida == 3 :
    print('ativar restaurantes')
else:
    print('Encerrando o programa')