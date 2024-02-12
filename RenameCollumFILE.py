import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv("E:\\00Rangel\\01Projetos\\Python\\ETL\\dados\\Diversos\\Frequencia_2008.csv")

# Renomear as colunas
colunas = {
    'FltJan08': 'FltJan',
    'FrqJan08': 'FrqJan',
    'FltFev08': 'FltFev',
    'FrqFev08': 'FrqFev',
    'FltMar08': 'FltMar',
    'FrqMar08': 'FrqMar',
    'FltAbr08': 'FltAbr',
    'FrqAbr08': 'FrqAbr',
    'FltMai08': 'FltMai',
    'FrqMai08': 'FrqMai',
    'FltJun08': 'FltJun',
    'FrqJun08': 'FrqJun',
    'FltJul08': 'FltJul',
    'FrqJul08': 'FrqJul',
    'FltAgo08': 'FltAgo',
    'FrqAgo08': 'FrqAgo',
    'FltSet08': 'FltSet',
    'FrqSet08': 'FrqSet',
    'FltOut08': 'FltOut',
    'FrqOut08': 'FrqOut',
    'FltNov08': 'FltNov',
    'FrqNov08': 'FrqNov',
    'FltDez08': 'FltDez',
    'FrqDez08': 'FrqDez',
    'Obs08': 'Observacoes'
}
df.rename(columns=colunas, inplace=True)

# Adicionar colunas Ano e Mes
df['Ano'] = 2008
df['Mes'] = '00'

# Adicionar colunas Ocorrencia1 e Ocorrencia2
df['Ocorrencia1'] = '00'
df['Ocorrencia2'] = '00'

# Salvar as modificações em um novo arquivo CSV
df.to_csv('arquivo_modificado.csv', index=False)