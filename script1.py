import sqlite3 as conector

try:

    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    comando = ''' CREATE TABLE IF NOT EXISTS Pessoa (
                    cpf INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY (cpf)
                );'''
    
    cursor.execute(comando)
    conexao.commit()
    
    print("Tabela 'Pessoa' criada com sucesso!")

except conector.DatabaseError as erro:
    print("Erro ao criar a tabela:", erro)

finally:
    
    if 'conexao' in locals() and conexao:
        cursor.close()
        conexao.close()
        print("Conexão com o banco de dados fechada.")

