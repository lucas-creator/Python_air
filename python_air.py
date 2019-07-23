import check_in
import lista_passageiros
import consulta

print('*'*30)
print('******** Python AIR ********')
print('*'*30)

print('Selecione opção no menu abaixo')
print('(1) Check IN\n(2) Listar Passageiros\n(3) Consultar Passageiros')

option = int(input('Defina a opção: '))

if(option == 1):
    print('Enbarcar Passageiros')
    check_in.check_in()
elif(option == 2):
    print('Lista de Passageiros')
    lista_passageiros.lista()
elif(option == 3):
    print('Consultar Passageiros')
    consulta.consulta()
