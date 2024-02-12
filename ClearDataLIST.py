import os
import csv

# Define uma função com os parametros
def limpar_caracteres(indesejaveis, texto):
    for caractere in indesejaveis:
        texto = texto.replace(caractere, ' ')
    return texto

# Define os caracteres indesejáveis que você deseja substituir
caracteres_indesejaveis = ['   ','@', '#', '$', '%', '(', ')', ',,', '.', '--', '/']
# caracteres_indesejaveis = [' ,',', ']
# caracteres_indesejaveis = ['�']

# Define o caminho da pasta que contém os arquivos CSV
pasta = "E:\\00Rangel\\01Projetos\\Python\\ETL\\dados\\"

# Lista todos os arquivos na pasta
arquivos = os.listdir(pasta)

# Itera sobre os arquivos CSV
for arquivo in arquivos:
    if arquivo.endswith('.csv'):
        caminho_arquivo = os.path.join(pasta, arquivo)
        caminho_arquivo_saida = os.path.join(pasta, 'limpo_' + arquivo) #Define nome de prefixo para o arquivo CSV

        # Abre o arquivo de entrada para leitura e o arquivo de saída para escrita
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_entrada, open(caminho_arquivo_saida, 'w', newline='', encoding='utf-8') as arquivo_saida:
            leitor_csv = csv.reader(arquivo_entrada)
            escritor_csv = csv.writer(arquivo_saida)

            linhas_limpas = []
            for linha in leitor_csv:
                linha_limpa = [limpar_caracteres(caracteres_indesejaveis, valor) for valor in linha]
                if any(linha_limpa):
                    linhas_limpas.append(linha_limpa)

            if linhas_limpas:
                escritor_csv.writerows(linhas_limpas)

        print(f"Arquivo {arquivo} limpo gravado com sucesso!")
