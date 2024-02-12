import os

# Diretório onde estão os arquivos
diretorio = "E:\\00Rangel\\01Projetos\\Python\\ETL\\dados\\"

# Listar os arquivos no diretório
arquivos = os.listdir(diretorio)

for nome_arquivo in arquivos:
    # Verificar se o arquivo possui o prefixo 'limpo_Frequencia_' e a extensão .csv
    if nome_arquivo.startswith('limpo_Frequencia_') and nome_arquivo.endswith('.csv'):
        # Remover o prefixo 'limpo_'
        novo_nome = nome_arquivo.replace('limpo_', '')
        caminho_antigo = os.path.join(diretorio, nome_arquivo)
        caminho_novo = os.path.join(diretorio, novo_nome)
        os.rename(caminho_antigo, caminho_novo)
        print(f'O arquivo {nome_arquivo} foi renomeado para {novo_nome}.')
