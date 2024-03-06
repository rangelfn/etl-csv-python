import os
import pandas as pd

# Caminho da pasta principal
pasta_principal = r'C:\Users\UNIR\OneDrive\Área de Trabalho\Avaliacoes'

# Função para converter arquivos Excel para CSV separar as planilhas e unir os dados das planilhas em dois arquivos distintos.
def unir_dados_csv(pasta):
    dados_docente = pd.DataFrame()  # DataFrame para armazenar dados de DOCENTE
    dados_discente = pd.DataFrame()  # DataFrame para armazenar dados de DISCENTE

    for root, dirs, files in os.walk(pasta):
        for arquivo in files:
            if arquivo.endswith('.csv'):
                print(f"Lendo {arquivo}...")
                caminho_arquivo = os.path.join(root, arquivo)
                # Verificar se o arquivo não está vazio e se contém colunas
                with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                    primeira_linha = f.readline()
                    if primeira_linha.strip() != '':
                        dados_arquivo = pd.read_csv(caminho_arquivo, encoding='utf-8')
                        if 'DOCENTE' in arquivo:
                            dados_docente = pd.concat([dados_docente, dados_arquivo])
                        elif 'DISCENTE' in arquivo and 'BACHARELADO' not in arquivo and 'LICENCIATURA' not in arquivo and 'TURMA' not in arquivo:
                            dados_discente = pd.concat([dados_discente, dados_arquivo])
                    else:
                        print(f"O arquivo {arquivo} está vazio ou não contém colunas, pulando para o próximo arquivo.")

    # Salvar dados de DOCENTE e DISCENTE em arquivos CSV separados
    dados_docente.to_csv(os.path.join(pasta, 'dados_docente.csv'), index=False)
    dados_discente.to_csv(os.path.join(pasta, 'dados_discente.csv'), index=False)

    print("União concluída.")
