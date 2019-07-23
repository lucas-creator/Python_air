def lista():
    passageiros = []
    with open('passageiros.txt') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            passageiros.append(linha)

    for passenger in passageiros:
        print(passenger)
