import pandas as pd
import os

# Define o caminho da pasta que contém os arquivos CSV
pasta = "E:\\00Rangel\\01Projetos\\Python\\ETL\\dados\\"
# Lista todos os arquivos na pasta
arquivos = os.listdir(pasta)

# Loop para percorrer cada arquivo CSV
for arquivo in arquivos:
    if arquivo.endswith('.csv'):
        caminho_arquivo = os.path.join(pasta, arquivo)
        caminho_arquivo_saida = os.path.join(pasta, 'transformado_' + arquivo)

        # Lê o arquivo CSV com o pandas
        dataframe = pd.read_csv(caminho_arquivo)

        # Renomeia a coluna 'Obs08' para 'Observacoes'
        dataframe = dataframe.rename(columns={'Obs08': 'Observacoes'})

        # Adiciona as novas colunas 'Ocorrencia1' e 'Ocorrencia2' com valores '00'
        dataframe['Ocorrencia1'] = '00'
        dataframe['Ocorrencia2'] = '00'

        # Grava o dataframe transformado em um novo arquivo CSV
        dataframe.to_csv(caminho_arquivo_saida, index=False)

        print(f"Arquivo {arquivo} transformado e gravado com sucesso!")