import os
import json
import click
from datetime import datetime

DIRETORIO_DADOS = 'dados'
ARQUIVO_NOTAS = 'notas.json'
CAMINHO_ARQUIVO_NOTAS = os.path.join(DIRETORIO_DADOS, ARQUIVO_NOTAS)

def criar_diretorio_e_arquivo():
    if not os.path.exists(DIRETORIO_DADOS):
        os.makedirs(DIRETORIO_DADOS)

    if not os.path.exists(CAMINHO_ARQUIVO_NOTAS):
        with open(CAMINHO_ARQUIVO_NOTAS, 'w') as arquivo:
            json.dump([], arquivo)

def adicionar_nota(titulo, conteudo, tags):
    with open(CAMINHO_ARQUIVO_NOTAS, 'r') as arquivo:
        notas = json.load(arquivo)

        nova_nota = {
            'titulo': titulo,
            'conteudo': conteudo,
            'data': datetime.now().strftime('%d-%m-%y %H:%M:%S'),
            'tags': tags
        }

        notas.append(nova_nota)

        with open(CAMINHO_ARQUIVO_NOTAS, 'w') as arquivo:
            json.dump(notas, arquivo, indent=2)

def listar_notas():
    with open(CAMINHO_ARQUIVO_NOTAS, 'r') as arquivo:
        notas = json.load(arquivo)
        
    for nota in notas:
        print(f"---\nTítulo: {nota['titulo']}\nConteúdo: {nota['conteudo']}\nData: {nota['data']}\nTags: {', '.join(nota['tags'])}")

if __name__ == "__main__":
    criar_diretorio_e_arquivo()
    adicionar_nota(input("Digite o título da nota: "), input("Digite o conteúdo da nota: "), [input("Digite uma tag: "),input("Digite uma segunda tag: ")])
    listar_notas()
                                                                                                                                                    
