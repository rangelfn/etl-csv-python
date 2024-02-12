import pandas as pd

# Define o caminho do arquivo CSV
caminho_arquivo = 'dados.csv'

# Lê o arquivo CSV com o pandas
dataframe = pd.read_csv(caminho_arquivo)

# Renomeia a coluna 'Obs08' para 'Observacoes'
dataframe = dataframe.rename(columns={'Obs08': 'Observacoes'})

# Adiciona as novas colunas 'Ocorrencia1' e 'Ocorrencia2' com valores '00'
dataframe['Ocorrencia1'] = '00'
dataframe['Ocorrencia2'] = '00'

# Define o caminho do arquivo de saída
caminho_arquivo_saida = 'dados_transformados.csv'

# Grava o dataframe transformado em um novo arquivo CSV
dataframe.to_csv(caminho_arquivo_saida, index=False)

print("Arquivo transformado gravado com sucesso!")