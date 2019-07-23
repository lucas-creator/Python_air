def check_in():
    passageiros = []

    while len(passageiros) <= 4:
        passageiro = input('Digite o nome do passageiro: ')
        passageiros.append(passageiro)
        arquivo = open('passageiros.txt', 'w')
        for passengers in passageiros:
            arquivo.writelines(passengers + '\n')
        arquivo.close()

    print('Passageiros embarcados!')
