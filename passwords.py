from cryptocode import encrypt, decrypt
import hashlib
from os.path import isfile
import csv
import pandas as pd
import os
import pathlib

class Passwords:
    def __init__(self, args):
        home_folder = os.getenv('HOME')
        self.args = args
        pathlib.Path(f'{home_folder}/.pss').mkdir(exist_ok=True)
        self.path_passwords = f'{home_folder}/.pss/senhas_servicos.csv'
        self.master_password = f'{home_folder}/.pss/master_ps.txt'


    def new(self):
        if not isfile(self.master_password):
            password = input("pass >> ")
            with open(self.master_password, 'w') as ps:
                r = hashlib.md5(password.encode())
                ps.write(r.hexdigest())

    def cadastra_senha(self):
        if isfile(self.master_password):
            with open(self.master_password, 'r') as f:
                password = input("pass >> ")
                r = hashlib.md5(password.encode())
                ps = f.read()
                ps2 = r.hexdigest()

                if ps == ps2:
                    name_service = input("Nome >> ")
                    user_service = input("User >> ")
                    pass_service = input("Senha >> ")
                    if not isfile(self.path_passwords):
                        with open(self.path_passwords, 'w') as f:
                            w = csv.writer(f)
                            w.writerow(['Nome', 'User', 'Senha'])

                    with open(self.path_passwords, 'a') as ps:
                        escrever = csv.writer(ps)
                        escrever.writerow([name_service, user_service, encrypt(pass_service, password)])
        else:
            print("cadastre uma senha usando pss new")

    def lista_senhas(self):
        if isfile(self.path_passwords):
            with open(self.master_password, 'r') as f:
                password = input("pass >> ")
                r = hashlib.md5(password.encode())
                ps = f.read()
                ps2 = r.hexdigest()
                if ps == ps2:
                    df = pd.read_csv(self.path_passwords)
                    for _, row in df.iterrows():
                        print(
                            f"Nome: {row['Nome']} | Usuario: {row['User']} | Senha: {decrypt(row['Senha'], password)}")
        else:
            print("Nada cadastrado ainda!")

    def remove(self):
        if isfile(self.path_passwords):
            password = input("pass >> ")
            with open(self.master_password, 'r') as f:
                r = hashlib.md5(password.encode())
                ps = f.read()
                ps2 = r.hexdigest()

                if ps == ps2:
                    with open(self.path_passwords, 'r') as f:
                        linhas = csv.reader(f)
                        lst = list(linhas)

                    with open(self.path_passwords, 'w') as f:
                        writer = csv.writer(f)
                        ident = None
                        for line in lst:
                            nome, senha = line

                            if nome == self.args.nome:
                                ident = nome

                            if ident != nome:
                                writer.writerow(line)
        else:
            print("Nada cadastrado ainda!")

    def encotra_por_chave(self):
        if isfile(self.path_passwords):
            with open(self.master_password, 'r') as f:
                password = input("pass >> ")
                r = hashlib.md5(password.encode())
                ps = f.read()
                ps2 = r.hexdigest()
                if ps == ps2:
                    df = pd.read_csv(self.path_passwords)
                    for _, row in df.iterrows():
                        if self.args.nome == row['Nome']:
                            print(
                                f"Nome: {row['Nome']} | Usuario: {row['User']} | Senha: {decrypt(row['Senha'], password)}")
        else:
            print("Nada cadastrado ainda!")
