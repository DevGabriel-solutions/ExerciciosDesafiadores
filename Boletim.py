print('=' * 20 + 'Cadastros' + '=' * 20)
boletim = []
def exibir_menu():
    print('Digite o número do serviço: ')
    print(f"{'Cadastrar Aluno':<20} - 1")
    print(f"{'Remover Aluno':<20} - 2")
    print(f"{'Exibir Boletim':<20} - 3")
    print(f"{'Sair':<20} - 4")
    return input('Opção: ')

opcao = exibir_menu()

while opcao != '4':

    if opcao == '1':
        print('=' * 20 + 'Cadastro de Alunos' + '=' * 20)
        nome = input('Digite o nome do aluno: ').upper()
        nota1 = float(input('Insira nota 1: '))
        nota2 = float(input('Insira nota 2: '))
        media = (nota1 + nota2) /2
        dados_aluno = [nome, nota1, nota2, media]
        boletim.append(dados_aluno)
        opcao = exibir_menu()

    elif opcao == '2':
        print('=' * 20 + 'Remoção de cadastro' + '=' * 20)

        if not boletim:
            print('A lista de alunos está vazia')
        else:
            tentar_novamente = 's'
            while tentar_novamente == 's':

                nome_remover = input('Digite o nome do aluno a ser removido: ').upper()
                aluno_removido = False

                for indice, aluno in enumerate(boletim):
                    if aluno[0].upper() == nome_remover.upper():
                        boletim.pop(indice)

                        print(f'Aluno: {nome_remover} removido com sucesso!')
                        aluno_removido = True
                        tentar_novamente = 'n'
                        break

                if not aluno_removido:
                    print(f'Erro: Aluno {nome_remover} não encontrado.')
                    tentar_novamente = 'n'
                    escolha = input('Deseja digitar outro nome(s) ou voltar ao menu(n)? ').lower()

                    if escolha == 's':
                        tentar_novamente = 's'  # Continua o loop interno
                    else:
                        tentar_novamente = 'n'  # Sai do loop interno e volta ao Menu principal

        opcao = exibir_menu()  # Volta ao Menu principal



    elif opcao == '3':
        print('=' * 20 + 'Exibir Boletim' + '=' * 20)

        if not boletim:
            print('Nenhum aluno foi cadastrado.')
            ver_detalhes = 'n'
        else:
            print('==Boletim Geral==')
            for aluno in boletim:
                nome_aluno = aluno[0]
                media_aluno = aluno[3]
                print(f'Nome: {nome_aluno} - média - {media_aluno}')
            ver_detalhes = 's'

        while ver_detalhes == 's':
            aluno_detalhe = input('Ver detalhes de aluno: ').upper()

            if aluno_detalhe:
                aluno_encontrado = False

                for aluno in boletim:
                    if aluno[0].upper() == aluno_detalhe.upper():
                        nome = aluno[0]
                        nota1 = aluno[1]
                        nota2 = aluno[2]
                        media = aluno[3]
                        print(f'Aluno: {nome}\nNota 1: {nota1}\nNota 2: {nota2}\nMedia: {media:.1f} ')
                        aluno_encontrado = True
                        break

                if not aluno_encontrado and boletim:
                    print(f'Aluno {aluno_detalhe} não encontrado.')
                escolha = input('Deseja ver detalhes de outro aluno (s) ou voltar ao menu(n)?').lower()

                if escolha == 's':
                    ver_detalhes = 's'
                else:
                    ver_detalhes = 'n'
            else:
                ver_detalhes = 'n'

        opcao = exibir_menu()

    else:
        print('Opção Invalida!')
        opcao = exibir_menu()

print('Programa encerrado!')






