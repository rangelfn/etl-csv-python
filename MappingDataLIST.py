import os
import csv

def read_csv_file(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def write_csv_file(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def find_valid_cpf(files):
    valid_cpfs = {}
    for file in files:
        data = read_csv_file(file)
        for row in data:
            cpf = row['Cpf']
            if cpf.isdigit() and len(cpf) == 11:
                matricula = row['Matricula']
                nome = row['Nome']
                lotacao = row['Lotacao']
                key = (matricula, nome, lotacao)
                valid_cpfs[key] = cpf
    return valid_cpfs

def update_cpf(data, valid_cpfs):
    for row in data:
        cpf = row['Cpf']
        if not cpf.isdigit() or len(cpf) != 11 or cpf == "00" or cpf == "NAO CADASTRADO":
            matricula = row['Matricula']
            nome = row['Nome']
            lotacao = row['Lotacao']
            key = (matricula, nome, lotacao)
            if key in valid_cpfs:
                row['Cpf'] = valid_cpfs[key]

def main():
    input_folder = r'E:\00Rangel\01Projetos\Python\ETL\dados'  # Pasta onde estão os arquivos CSV
    output_folder = '.'  # Pasta onde será salvo o arquivo com os CPFs atualizados

    if not os.path.exists(input_folder):
        print(f"O diretório '{input_folder}' não existe. Verifique o caminho do diretório.")
        return

    files = [file for file in os.listdir(input_folder) if file.startswith('Frequencia_') and file.endswith('.csv')]
    if not files:
        print("Nenhum arquivo encontrado no diretório.")
        return

    valid_cpfs = find_valid_cpf([os.path.join(input_folder, file) for file in files])

    if not valid_cpfs:
        print("Nenhum CPF válido encontrado nos arquivos.")
        return

    print("CPFs válidos encontrados:", valid_cpfs)

    for file in files:
        data = read_csv_file(os.path.join(input_folder, file))
        update_cpf(data, valid_cpfs)
        output_filename = os.path.join(output_folder, file)
        write_csv_file(output_filename, data)
        print(f"Arquivo {file} atualizado e salvo como {output_filename}.")

if __name__ == "__main__":
    main()
