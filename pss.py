# 1 - criar senha na primeira execução  | pss new
# 2 - cadatrar uma nova senha           | pss a
# 3 - listar serviços salvos            | pss ls 
# 4 - remover senha salva               | pss r -ha <hash> ou -n <nome>
# 5 - recuperar por hash ou nome        | pss ss -h <hash> ou -n <nome>

import sys
import argparse
import pandas as pd
import csv
from os.path import isfile
import hashlib
from cryptocode import encrypt, decrypt

def main():
    parser = argparse.ArgumentParser(description='gerenciador hehe')
    
    parser.add_argument('chave')

    parser.add_argument('-n', '--nome', required = False)
    parser.add_argument('-ha', '--hash', required = False)
    args = parser.parse_args()

    if args.chave == 'new':
        if not isfile('ps.txt'):
            pss = input("pass >> ")
            with open('ps.txt', 'w') as ps:
                r = hashlib.md5(pss.encode())
                ps.write(r.hexdigest())

    # Cadastra nova senha
    elif args.chave == 'a':
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
                    
    # Lista senhas salvas
    elif args.chave == 'ls':
        with open('ps.txt', 'r') as f:
            pss = input("pass >> ")
            r = hashlib.md5(pss.encode())
            ps = f.read()
            ps2 = r.hexdigest()
            if ps == ps2:
                df = pd.read_csv('senhas.csv')
                for _, row in df.iterrows():
                    print(f"Nome: {row['Nome']} | Senha: {decrypt(row['Senha'], pss)}")

    # Remove uma senha por palavra chave
    elif args.chave == 'r':
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

                            if nome == args.nome:
                                ident = nome

                            if ident != nome:
                                writer.writerow(line)
        else:
            print("nada cadastrado!")

    # Recupera uma unica senha
    elif args.chave == 'ss':
        with open('ps.txt', 'r') as f:
            pss = input("pass >> ")
            r = hashlib.md5(pss.encode())
            ps = f.read()
            ps2 = r.hexdigest()
            if ps == ps2:
                df = pd.read_csv('senhas.csv')
                for _, row in df.iterrows():
                    if args.nome == row['Nome']:
                        print(f"Nome: {row['Nome']} | Senha: {decrypt(row['Senha'], pss)}")

if __name__ == '__main__':
    sys.exit(main())
