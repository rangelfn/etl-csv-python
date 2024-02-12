import csv

def limpar_caracteres(indesejaveis, texto):
    for caractere in indesejaveis:
        texto = texto.replace(caractere, '')
    return texto

# Define os caracteres indesejáveis que você deseja substituir
caracteres_indesejaveis = ['@', '#', '$', '%']

# Define o caminho do arquivo de entrada e de saída
arquivo_entrada = "E:\\00Rangel\\01Projetos\\Python\\ETL\\dados\\Diversos\\Frequencia_2008.csv"
arquivo_saida = "E:\\00Rangel\\01Projetos\\Python\\ETL\\dados\\Diversos\\Limpo_Frequencia_2008.csv"

# Abre o arquivo de entrada para leitura e o arquivo de saída para escrita
with open(arquivo_entrada, 'r') as arquivo_entrada, open(arquivo_saida, 'w', newline='') as arquivo_saida:
    leitor_csv = csv.reader(arquivo_entrada)
    escritor_csv = csv.writer(arquivo_saida)

    for linha in leitor_csv:
        linha_limpa = [limpar_caracteres(caracteres_indesejaveis, valor) for valor in linha]
        escritor_csv.writerow(linha_limpa)

print("Arquivo limpo gravado com sucesso!")