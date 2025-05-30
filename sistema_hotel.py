banco_dados =  {}

nome1 = input('Nome: ')
idade1 = input('Idade: ')
senha1 = input('senha: ')

nome2 = input('Nome: ')
idade2 = input('Idade: ')
senha2 = input('senha: ')

nome3 = input('Nome: ')
idade3 = input('Idade: ')
senha3 = input('senha: ')

banco_dados['nomes'] = [nome1, nome2, nome3]
banco_dados['idades'] = [idade1, idade2, idade3]
banco_dados['senhas'] = [senha1, senha2, senha3]
print(banco_dados)

login_nome = input('digite seu nome >>')
senha_acesso = input('digite sua senha >>')

if login_nome in banco_dados['nomes'] and senha_acesso in banco_dados ['senhas']:
   print('seja bem vindo ao sistema!')
else:
	print('acesso negado, tente novamente!')