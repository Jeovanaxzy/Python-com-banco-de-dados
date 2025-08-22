import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

cpf = 12345678900
nome = 'Maria'
nascimento = '1995-05-10'
oculos = 0

comando_seguro = '''
INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?);
'''

cursor.execute(comando_seguro, (cpf, nome, nascimento, oculos))

# Efetivação e fechamento
conexao.commit()
cursor.close()
conexao.close()
