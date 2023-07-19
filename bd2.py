import mysql.connector
from faker import Faker

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
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS professor(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        data_nascimento DATE,
        cidade_natal VARCHAR(255),
        estado VARCHAR(2),
        renda_percapta FLOAT,
        formacao VARCHAR(255)
    )
''')

fake = Faker ("pt_BR")
dados_professores = []
for i in range (1, 10001):
    nome = fake.name()
    data_nascimento = fake.date_of_birth()
    cidade_natal = fake.city()
    estado = fake.estado_sigla()
    renda_percapta = fake.pyfloat(left_digits = 4, right_digits = 2, positive = True)
    formacao = fake.text(max_nb_chars=255)
    
    dados_professores.append((
        nome, data_nascimento, cidade_natal, estado, renda_percapta, formacao
    ))

inserir_query = '''
    INSERT INTO professor(
        nome, data_nascimento, cidade_natal, estado, renda_percapta, formacao
    )
    VALUES(%s,%s,%s,%s,%s,%s)
'''

cursor.executemany(inserir_query,dados_professores)

conexao.commit()
conexao.close()