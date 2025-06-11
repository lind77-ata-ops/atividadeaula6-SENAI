# nome =  input('nome: ')


# match nome:
#     case 'Carlos':
#         print('Olá ', nome)
#     case 'Maria':
#         print('Olá', nome)
#     case _:
#         print('Não foi dessa vez')



n = int(input('Teste'))


match n:
    case 10:
        print('O numero é ', n)
    case 20:
        print('O numero é ', n)


    case _:
        print('O numero desconhecido')        




match numero:
    case x if x == 100:
        print('é 100')
    case x if x > 100:
        print('x é > 100')
    case x if x < 100:
        print('numero é menor que 100')


