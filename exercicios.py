#3
s = input('')

match s:
    case '':
        print('vazio')
    case _:
        print('nao é vazio')





#4
numero = int(input('digite um numero: '))
match numero:
    case x if x == 10:
        print('seu numero é igua a 10')
    case x if x > 10:
        print('seu numero é maior que 10')
    case x if x < 10:
        print('seu numero é menor que 10')

#5
idade = int(input('digite sua idade: '))
match idade:
    case x if x <= 12:
        print('voce é uma criança')
    case x if x <= 17:
        print('voce é um adolescente')
    case x if x <= 35:
        print('voce é um jovem')
    case x if x <=64:
        print('voce é um adulto')
    case x if x > 65:
        print('voce é um idoso')

