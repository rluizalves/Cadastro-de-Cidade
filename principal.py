from src.classes.cidade import Cidade

#import sys
#sys.path.insert(0, '../src')
#import unittest
#from cidade import Cidade
import json

sair = False

arquivo = open('./src/bd/bd.json','r')
lista_cidade = json.loads(arquivo.read())
arquivo.close()

while sair ==False:
    #Recebendo informações da cidade
    nome_cidade = input('Digite o nome da cidade: ')
    populaçao_cidade = int(input('Digite a população da cidade: '))
    sigla_estado = input('Digite a sigla do estado: ')   
    nome_estado = input('Digite o nome do estado: ')
    #instanciar a cidade
    uf = { 'sigla': sigla_estado, 'nome': nome_estado }
    nova_cidade = lista_cidade(nome_cidade, populaçao_cidade, uf)
    #adiciona a cidade na lista
    lista_cidade.append({

        'nome': nova_cidade.nome,
        'populacao': nova_cidade.populacao,
        'uf': {
            'sigla':nova_cidade.uf['sigla'],
            'nome': nova_cidade.uf['nome'],
        }

    })

    resposta = input('Cadastrar outra cidade? (S/N)')

    #Verificando a resposta correta S ou N
    resposta_incorreta = resposta.upper() != 'S' and resposta.upper() != 'N' 

    while resposta_incorreta:
        print('Resposta inválida. A resposta deve ser S ou N.')
        resposta = input('Deseja cadastrar uma nova cidade? (S/N)')
    if resposta.upper() == 'N':
        sair = True


arquivo = open('./src/bd/bd.json','w')
arquivo.write(json.dumps(lista_cidade))
arquivo.close()