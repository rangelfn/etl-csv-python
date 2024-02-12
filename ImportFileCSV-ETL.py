import pandas as pd
import pyodbc

# Configuração da conexão com o banco de dados
server = 'SETIC-20000231'
database = 'Frequencia'
driver = '{ODBC Driver 17 for SQL Server}'
trusted_connection = 'Yes'

# Criação da conexão com o banco de dados
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'
connection = pyodbc.connect(connection_string)

# Leitura dos dados do arquivo CSV
csv_file = 'E:\\00Rangel\\01Projetos\\Python\\ETL\\Frequencia_2001-01.csv'
df = pd.read_csv(csv_file)

# Inserção dos dados nas tabelas
for index, row in df.iterrows():
    cursor = connection.cursor()

    # Inserir dados na tabela Pessoa (PessoaID é auto incremento, não é necessário incluir no insert)
    cpf = row['Cpf']
    nome = row['Nome']
    try:
        cursor.execute("INSERT INTO Pessoa (CPF, Nome) VALUES (?, ?)", cpf, nome)
        cursor.commit()
    except pyodbc.IntegrityError:
        pass

    # Inserir dados na tabela Servidor (PessoaID é auto incremento, não é necessário incluir no insert)
    matricula = row['Matricula']
    cargo = row['Cargo']
    try:
        cursor.execute("INSERT INTO Servidor (Matricula, Cargo, CPF) VALUES (?, ?, ?)", matricula, cargo, cpf)
        cursor.commit()
    except pyodbc.IntegrityError:
        pass

    # Inserir dados na tabela Lotacao (PessoaID e ServidorID são auto incremento, não é necessário incluir no insert)
    lotacao = row['Lotacao']
    sublotacao = row['Sublotacao']
    localidade = row['Localidade']
    cursor.execute("INSERT INTO Lotacao (Lotacao, Sublotacao, Localidade, Matricula) VALUES (?, ?, ?, ?)", lotacao, sublotacao, localidade, matricula)
    cursor.commit()

    # Inserir dados na tabela Frequencias (PessoaID e ServidorID são auto incremento, não é necessário incluir no insert)
    ano = row['Ano']
    mes = row['Mes']
    faltas = row['Faltas']
    dias_trabalhados = row['DiasTrabalhados']
    observacoes = row['Observacoes']
    cursor.execute("INSERT INTO Frequencias (Ano, Mes, Faltas, DiasTrabalhados, Observacoes, Matricula) VALUES (?, ?, ?, ?, ?, ?)", ano, mes, faltas, dias_trabalhados, observacoes, matricula)
    cursor.commit()

    # Inserir dados na tabela Ocorrencias, caso haja valores não nulos
    ocorrencia1 = row['Ocorrencia1']
    ocorrencia2 = row['Ocorrencia2']
    if not pd.isnull(ocorrencia1):
        try:
            cursor.execute("INSERT INTO Ocorrencias (Codigo, FreqID) SELECT ?, IDENT_CURRENT('Frequencias')", ocorrencia1)
            cursor.commit()
        except pyodbc.IntegrityError:
            pass
    if not pd.isnull(ocorrencia2):
        try:
            cursor.execute("INSERT INTO Ocorrencias (Codigo, FreqID) SELECT ?, IDENT_CURRENT('Frequencias')", ocorrencia2)
            cursor.commit()
        except pyodbc.IntegrityError:
            pass

# Fechar a conexão com o banco de dados
connection.close()

print("Dados do CSV foram salvos no banco de dados com sucesso!")
