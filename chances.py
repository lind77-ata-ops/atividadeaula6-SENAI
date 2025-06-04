import random

chances = [3,2,1]

for i in chances:
	numero_ale = random.randint(1,11)
	
	print('voce tem apenas...', i, 'chances')
	chute = int(input('digite seu chute: '))
	
	if numero_ale == chute:
		print('acertou em cheio! ')
	else:
		print('errou feio! ')
else:
	print('chances esgotadas!!! perdeu feio')
	