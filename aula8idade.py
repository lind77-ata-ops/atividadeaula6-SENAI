idade  =  int(input('idade: '))

if idade  <=12:
    print('Criança')
elif idade >12 and idade <=14:
    print('pré - Adolescente')
elif idade >=15 and idade <=17:
    print('Adolescente')
elif idade >=18 and idade <= 25:
    print('Jovem')
elif idade>25 and idade <=64:
    print('Adulto')
else:
    print('Idoso(a)')