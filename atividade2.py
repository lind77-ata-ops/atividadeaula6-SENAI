# sistema de notas

senha  =  '1234'
acesso =  'lind'
p  =   0
lista_notas  = []

while p  <= 3:
    senha_user = input('Digite sua senha: ')
    login =  input('Digite seu login: ')
    p = p + 1
    if senha == senha_user and login == acesso:
        print('Sistema de notas')
        quantas_notas =  int(input('Quantiade notas: '))
        for n in range(quantas_notas):
            nota =  float(input('Digita a nota: '))
            lista_notas.append(nota)
            soma = sum(lista_notas)
            media  =  soma / quantas_notas
        print('Media - ', media)
        break
             
        
        
    else:
        print('Digitação incorreta! ')
else:
    print('Conta bloqueada!!')
    
    
