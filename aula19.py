import sqlite3


conexao = sqlite3.connect('meu_banco_de_dados.db')


cursor = conexao.cursor()


cursor.execute('''
       CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY NOT NULL ,        
        nome TEXT NOT NULL,
        idade INTERGER NOT NULL,
        cidade TEXT NOT NULL
    )        
''')


nome = input('digite um nome: ')
idade = int(input('digite sua idade: '))
cidade = input('cidade: ')
id = int(input('Id: '))


cursor.execute('''
        INSERT INTO pessoas (id,nome, idade, cidade) 
        VALUES (?, ?, ?,?)
''', (id,nome,idade,cidade))


conexao.commit()
cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()


for pessoa in pessoas:
    print(f'''ID: {pessoa[0]}, nome: {pessoa[1]}, idade:
    {pessoa[2]}, cidade: {pessoa[3]}''')
    
conexao.close()

