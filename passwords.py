from cryptocode import encrypt, decrypt
import hashlib
from os.path import isfile
import csv
import pandas as pd
import os

class Passwords:
    def __init__(self, args):
        home_folder = os.getenv('HOME')
        self.args = args
        self.path_passwords = f'{home_folder}/.senhas_servicos.csv'
        self.master_password = f'{home_folder}/.master_ps.txt'


    def new(self):
        if not isfile(self.master_password):
            pss = input("pass >> ")
            with open(self.master_password, 'w') as ps:
                r = hashlib.md5(pss.encode())
                ps.write(r.hexdigest())

    def cadastra_senha(self):
        if isfile(self.master_password):
            with open(self.master_password, 'r') as f:
                pss = input("pass >> ")
                r = hashlib.md5(pss.encode())
                ps = f.read()
                ps2 = r.hexdigest()

                if ps == ps2:
                    nome = input("Nome >> ")
                    senha = input("Senha >> ")
                    if not isfile(self.path_passwords):
                        with open(self.path_passwords, 'w') as f:
                            w = csv.writer(f)
                            w.writerow(['Nome', 'Senha'])

                    with open(self.path_passwords, 'a') as cu:
                        escrever = csv.writer(cu)
                        escrever.writerow([nome, encrypt(senha, pss)])
        else:
            print("cadastre uma senha usando pss new")

    def lista_senhas(self):
        if isfile(self.path_passwords):
            with open(self.master_password, 'r') as f:
                pss = input("pass >> ")
                r = hashlib.md5(pss.encode())
                ps = f.read()
                ps2 = r.hexdigest()
                if ps == ps2:
                    df = pd.read_csv(self.path_passwords)
                    for _, row in df.iterrows():
                        print(
                            f"Nome: {row['Nome']} | Senha: {decrypt(row['Senha'], pss)}")
        else:
            print("Nada cadastrado ainda!")

    def remove(self):
        if isfile(self.path_passwords):
            senha = input("pass >> ")
            with open(self.master_password, 'r') as f:
                r = hashlib.md5(senha.encode())
                ps = f.read()
                ps2 = r.hexdigest()

                if ps == ps2:
                    with open(self.path_passwords, 'r') as f:
                        linhas = csv.reader(f)
                        lst = list(linhas)

                    with open(self.path_passwords, 'w') as cu:
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
        if isfile(self.path_passwords):
            with open(self.master_password, 'r') as f:
                pss = input("pass >> ")
                r = hashlib.md5(pss.encode())
                ps = f.read()
                ps2 = r.hexdigest()
                if ps == ps2:
                    df = pd.read_csv(self.path_passwords)
                    for _, row in df.iterrows():
                        if self.args.nome == row['Nome']:
                            print(
                                f"Nome: {row['Nome']} | Senha: {decrypt(row['Senha'], pss)}")
        else:
            print("Nada cadastrado ainda!")
