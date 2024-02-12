import pyodbc
import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")

# Conectando no Banco de Dados
conn = pyodbc.connect(
    Driver='{ODBC Driver 17 for SQL Server}',
    Server='SETIC-20000231',
    Database='FrequenciaRO',
    Trusted_Connection='Yes',
)
cursor = conn.cursor()
print("Conectado com Sucesso")

# Carregando diversos arquivos simultaneamente
lista_dataFrames = []
lista_nome = []
diretorio = "E:\\00Rangel\\01Projetos\\Python\\ETL\\dados\\"
for arq in os.listdir(diretorio):
    if arq.endswith(".csv"):
        nome_arquivo = "\\" + arq
        nome_df = pd.read_csv(diretorio+nome_arquivo, sep=',' , encoding='UTF-8',)
        print("Arquivo: ", arq)
        lista_dataFrames.append(nome_df)
        #x = arq.rfind(".")
        #lista_nome.append(arq[:x])
        #print(arq[:x])
print("Arquivos carregados com sucesso")

# Concatenando os arquivos em um único DataFrame
contador = 1
df_concatenado = lista_dataFrames[0]
for i in lista_dataFrames[1:]:
    df_concatenado = pd.concat([df_concatenado, lista_dataFrames[contador]])
    contador += 1
print (df_concatenado)

for row in df_concatenado.itertuples():
    print(row)
    cursor.execute('''
        INSERT INTO FrequenciaRO.dbo.Frequencia
        (Matricula, Nome, Cpf, Cargo, Lotacao, Sublotacao, Localidade, Ano, Mes, Faltas, DiasTrabalhados, Ocorrencia1, Ocorrencia2, Observacoes)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        row.Matricula,
        row.Nome,
        row.Cpf,
        row.Cargo,
        row.Lotacao,
        row.Sublotacao,
        row.Localidade,
        row.Ano,
        row.Mes,
        row.Faltas,
        row.DiasTrabalhados,
        row.Ocorrencia1,
        row.Ocorrencia2,
        row.Observacoes)
    conn.commit()
cursor.close()
conn.close()