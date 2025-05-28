#vazia
lista = []

#lista preenchida

lista_teste = [1,2,3,4,5,6,7,8,9]
#              0 1 2 3 4 5 6 7 8

print(lista_teste[2])

lista_teste[5] = 100
print(lista_teste)

#funções

lista = []

#alteram a estrutura da lista:
#append() extend() +=() insert()
#append vai adicionar apenas um dado

lista.append(10)
print(lista)

#varios dados no final da lista -> extend() +=()
lista.extend([10,20,30,40,50,100, 'teste', True])
print(lista)

lista += ('a', 'b')
print(lista)

#add dado em um indice especifico

lista.insert(0, 200)
print(lista)

#deletar dado del remove pop

lista.pop()#deletar o ultimo dado
lista.pop(0)# deletar o indic que declrou

print(lista)

lista.remove('a')

del lista[0]

print(lista)
print(len(lista))
