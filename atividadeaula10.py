#1
def comparar():
    n1 =  int(input('Digite um número> '))
    n2 =  int(input('Digite um número> '))

    if n1 % 2 == 0 and n2 % 2 == 0:
        print('Ambos sã pares')
    elif n1 % 2 == 0 or n2 % 2 == 0:
        print('Um deles é par')
    else:
        print('Ambos impares')


#2

n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
              
def multiplicacao():
    multiplicar = n1 * n2 * n3
    print(multiplicar)
    
multiplicacao()

#3

numero1 = int(input('digite um numero: '))
numero2 = int(input('digite um numero: '))

def elevado():
    elevado = numero1**numero2
    print(elevado)
    
elevado()

#4

def verificar_idade():
    idade =  int(input('idade: '))
    if idade == 18:
        print('18  anos')
    else:
        print('Não tem 18')


# verificar_idade()



# 5
def mostrar_ano():
    ano_atual = 2025
    ano_nascimento = int(input('Ano nascimento:'))
    mes =  int(input('digite o numero do mês 1'))
    cal  =  2025 - ano_nascimento

    if mes <=6:
        print('Ano nascimento', cal)
    else:

         print('Ano nascimento', cal - 1)

#6

def verificar():
    copas = [1958,1962,1970,1994,2002]

    ano =  int(input('Digite o ano que vc acha que o br granhou'))
    if ano in copas:
        print('ganhou!')
    else:
        print('Não ganhou!')

#verificar()6

def restaurante():
    lista =  ['Macarronada', 'Salada', 'Sanbuiche', 'Sorvete']
    print(lista)
    escolha  =  int(input('Digite o id do produto: '))
    print('Escolha: ',  lista[escolha])

while True:
      restaurante()

