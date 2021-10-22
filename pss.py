PARA_HELP = """
  1 - criar senha na primeira execução:  pss new
| 2 - cadatrar uma nova senha:           pss a
| 3 - listar serviços salvos:            pss ls
| 4 - remover senha salva:               pss r -ha <hash> ou -n <nome>
| 5 - recuperar por hash ou nome:        pss ss -h <hash> ou -n <nome>
"""

import sys
import argparse
import pandas as pd
import csv
from os.path import isfile
import hashlib
from cryptocode import encrypt, decrypt


class Metodos:
    def __init__(self, args):
        self.args = args
    

    def new(self):
        if not isfile('ps.txt'):
            pss = input("pass >> ")
            with open('ps.txt', 'w') as ps:
                r = hashlib.md5(pss.encode())
                ps.write(r.hexdigest())


    def cadastra_senha(self):
        if isfile('ps.txt'):
            with open('ps.txt', 'r') as f:
                pss = input("pass >> ")
                r = hashlib.md5(pss.encode())
                ps = f.read()
                ps2 = r.hexdigest()
                
                if ps == ps2:
                    nome = input("Nome >> ")
                    senha = input("Senha >> ")
                    if not isfile('senhas.csv'):
                        with open('senhas.csv', 'w') as f:
                            w = csv.writer(f)
                            w.writerow(['Nome', 'Senha'])

                    with open('senhas.csv', 'a') as cu:  
                        escrever = csv.writer(cu)
                        escrever.writerow([nome, encrypt(senha, pss)])
        else:
            print("cadastre uma senha usando pss new")


    def lista_senhas(self):
        if isfile("senhas.csv"):
            with open('ps.txt', 'r') as f:
                pss = input("pass >> ")
                r = hashlib.md5(pss.encode())
                ps = f.read()
                ps2 = r.hexdigest()
                if ps == ps2:
                    df = pd.read_csv('senhas.csv')
                    for _, row in df.iterrows():
                        print(f"Nome: {row['Nome']} | Senha: {decrypt(row['Senha'], pss)}")
        else:
            print("Nada cadastrado ainda!")


    def remove(self):
        if isfile('senhas.csv'):
            senha = input("pass >> ")
            with open('ps.txt', 'r') as f:
                r = hashlib.md5(senha.encode())
                ps = f.read()
                ps2 = r.hexdigest()
                
                if ps == ps2:
                    with open('senhas.csv', 'r') as f:
                        linhas = csv.reader(f)
                        lst = list(linhas) 

                    with open('senhas.csv', 'w') as cu:   
                        writer = csv.writer(cu)
                        ident = None
                        for line in lst:
                            nome, senha = line

                            if nome == self.args.nome:
                                ident = nome

                            if ident != nome:
                                writer.writerow(line)
        else:
            print("nada cadastrado!")


    def encotra_por_chave(self):
        if isfile("senhas.csv"):
            with open('ps.txt', 'r') as f:
                pss = input("pass >> ")
                r = hashlib.md5(pss.encode())
                ps = f.read()
                ps2 = r.hexdigest()
                if ps == ps2:
                    df = pd.read_csv('senhas.csv')
                    for _, row in df.iterrows():
                        if self.args.nome == row['Nome']:
                            print(f"Nome: {row['Nome']} | Senha: {decrypt(row['Senha'], pss)}")
        else:
            print("Nada cadastrado ainda!")


def main():
    parser = argparse.ArgumentParser(description='gerenciador hehe')
    parser.add_argument('chave', help=PARA_HELP)
    parser.add_argument('-n', '--nome', required = False)
    parser.add_argument('-ha', '--hash', required = False)
    args = parser.parse_args()

    funcoes = Metodos(args)

    if args.chave == 'new':
        funcoes.new()

    # Cadastra nova senha
    elif args.chave == 'a':
        funcoes.cadastra_senha()

    # Lista senhas salvas
    elif args.chave == 'ls':
        funcoes.lista_senhas()

    # Remove uma senha por palavra chave
    elif args.chave == 'r':
        funcoes.remove()

    # Recupera uma unica senha
    elif args.chave == 'ss':
        funcoes.encotra_por_chave()
    
    else:
        sys.exit("Flag not find!")
        

if __name__ == '__main__':
    sys.exit(main())
