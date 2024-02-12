import pyodbc
import pandas as pd

conn = pyodbc.connect(
    Driver='{ODBC Driver 17 for SQL Server}',
    Server='SETIC-20000231',
    Database='FrequenciaTeste',
    Trusted_Connection='Yes',
)

cursor = conn.cursor()
print("Conectado com Sucesso")

data = pd.read_csv(r'E:\00Rangel\01Projetos\Python\ETL\dados\Frequencia_2018-01.csv', sep=',')
df = pd.DataFrame(data)
print(df.head(20))

for row in df.itertuples():
    cursor.execute('''
        INSERT INTO FrequenciaTeste.dbo.FrequenciaTeste
            (Matricula, Nome, Cpf, Cargo,
            Lotacao, Sublotacao, Localidade,
            Ano, Mes, Faltas, DiasTrabalhados,
            Ocorrencia1, Ocorrencia2, Observacoes)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
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

