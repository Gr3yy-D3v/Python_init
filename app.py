import os

def exibir_nome_do_programa():
    print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█""")

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. listar Restaurante')
    print('3. ativar Restaurante')
    print('4. Sair\n')


def finalizar_app():
    os.system('cls')
    #os.system('clear') no mac
    print('Finalizando o app\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma das opções: '))
    #opcao_escolhida = int(opcao_escolhida)
    """
    Def = Definir uma função para um fim. Utilizado para organizar o código.
    """


    if opcao_escolhida == 1 :
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2 :
        print('Listar restaurantes')
    elif opcao_escolhida == 3 :
        print('ativar restaurantes')
    else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()