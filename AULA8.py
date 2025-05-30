idade =  int(input('Digite sua idade'))
titulo_eleitor  =  input('Possui Título de eleitor? s ou n')

if idade >= 16 and titulo_eleitor == 's':
    print('Pode votar')
else:
    print('Você não pode Votar')