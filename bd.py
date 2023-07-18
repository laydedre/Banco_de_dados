import mysql.connector

def conectar():
    host = 'localhost'
    usuario = 'root'
    senha = 'admin'
    banco_de_dados = 'bancoteste'
    
    conexao = mysql.connector.connect(
        host = host,
        user = usuario,
        password = senha,
        database = banco_de_dados
    )
    return conexao

def criar_tabela(conexao):
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS aluno(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            data_nascimento DATE,
            cidade_natal VARCHAR(255),
            bairro VARCHAR(255)
            )
        ''')
    conexao.commit()
    
def cadastrar_aluno(conexao,nome,data_nascimento,cidade_natal,bairro):
    cursor = conexao.cursor()
    
    inserir_query = '''
    INSERT INTO aluno(conexao,nome, data_nascimento,cidade_natal,bairro)
    VALUES(%s,%s,%s,%s)
    '''
    valores = (nome, data_nascimento,cidade_natal,bairro)
    cursor.execute(inserir_query,valores)
    conexao.commit()
    
def main ():
    conexao = conectar()
    criar_tabela(conexao)
    
    print("CADASTRO DE ALUNO")
    nome = input("NOME DO ALUNO: ")
    data_nascimento = input("DATA DE NASCIMENTO (AAAA-MM-DD): ")
    cidade_natal = input("CIDADE NATAL: ")
    bairro = input("BAIRRO: ")
    
    cadastrar_aluno(conexao,nome,data_nascimento,cidade_natal,bairro)
    
    print("ALUNO CADASTRADO COM SUCESSO")
    
    conexao.close()
    
if __name__ == "__main__":
    main()