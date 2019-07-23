def consulta():
    passageiros = []
    with open('passageiros.txt') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            passageiros.append(linha)

    nome = input('Qual passageiro deseja consultar: ')
    if nome in passageiros:
        print('O passageiro {} está na poltrona {}.'.format(nome, passageiros.index(nome)+1))
    else:
        print('Passageiro não encontrado')
