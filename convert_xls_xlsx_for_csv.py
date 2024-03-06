import os
import pandas as pd

# Diretório onde estão as pastas com os arquivos .xls
diretorio = r'C:\Users\UNIR\OneDrive\Área de Trabalho\Avaliacoes'

# Função para converter arquivos .xls em .csv
def converter_xls_para_csv(pasta):
    for subdir, dirs, files in os.walk(pasta):
        for file in files:
            if file.endswith('.xls'):
                arquivo_xls = os.path.join(subdir, file)
                # Ler o arquivo .xls
                xls = pd.ExcelFile(arquivo_xls)
                # Converter cada planilha do arquivo .xls em um arquivo .csv
                for sheet_name in xls.sheet_names:
                    df = xls.parse(sheet_name)
                    csv_file = os.path.splitext(arquivo_xls)[0] + '_' + sheet_name + '.csv'
                    df.to_csv(csv_file, index=False)
                print(f'Arquivo "{file}" convertido para CSV.')

# Chamar a função para percorrer o diretório e converter os arquivos
converter_xls_para_csv(diretorio)
