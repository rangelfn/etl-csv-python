import os

# Diretório onde estão os arquivos
diretorio = "E:\\00Rangel\\01Projetos\\Python\\ETL\\dados\\Diversos\\"

# Listar os arquivos no diretório
arquivos = os.listdir(diretorio)

for nome_arquivo in arquivos:
    if nome_arquivo.endswith('.csv'):  # Verificar se o arquivo possui a extensão .csv
        novo_nome = nome_arquivo.replace('Presenca_', 'Frequencia_')  # Substituir parte do nome do arquivo
        caminho_antigo = os.path.join(diretorio, nome_arquivo)
        caminho_novo = os.path.join(diretorio, novo_nome)
        os.rename(caminho_antigo, caminho_novo)
        print(f'O arquivo {nome_arquivo} foi renomeado para {novo_nome}.')


