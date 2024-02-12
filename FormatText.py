import re

# Função para formatar perguntas em negrito
def formatar_perguntas_em_negrito(texto):
    # Usando expressão regular para encontrar padrões de perguntas iniciando com "1.1"
    padrao = r'^\s*(1\.\d+)\s+(.*\?)\s*$'
    texto_formatado = re.sub(padrao, r'**\1 \2**', texto, flags=re.MULTILINE)
    return texto_formatado

# Caminho do arquivo de entrada e saída
caminho_arquivo_entrada = r'C:\00Arquivos\00Rangel\01Projetos\Python\Avaliacao_Curso_Pelo_Docente.txt'
caminho_arquivo_saida = r'C:\00Arquivos\00Rangel\01Projetos\Python\Avaliacao_Curso_Pelo_Docente_negrito.txt'

# Ler o conteúdo do arquivo
with open(caminho_arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada:
    conteudo = arquivo_entrada.read()

# Formatar as perguntas em negrito
conteudo_formatado = formatar_perguntas_em_negrito(conteudo)

# Escrever o conteúdo formatado para um novo arquivo
with open(caminho_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(conteudo_formatado)

print(f'Perguntas em negrito foram salvas em {caminho_arquivo_saida}')
