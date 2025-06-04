dicionario = {'nome': 'Clara', 'idade': 25, 'cidade':'Guarulhos'}

for key,value in dicionario.items():
    print(key, value)
    
    
dicionario = {'nome': 'Clara', 'idade': 25, 'cidade':'Guarulhos'}

for value in dicionario.values():
    print(value)
    
    
dicionario = {'nome': 'Clara', 'idade': 25, 'cidade':'Guarulhos'}

for key in dicionario.keys():
    print(key)
    
    
lista_keys = []
lista_valores = []
dicionario = {'nome': 'Clara', 'idade': 25, 'cidade':'Guarulhos'}
for k,v in dicionario.items():
    lista_keys.append(k)
    lista_valores.append(v)
print(lista_keys)
print(lista_valores) 