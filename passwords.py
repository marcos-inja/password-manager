from cryptocode import encrypt, decrypt
import hashlib
from os.path import isfile
import csv
import pandas as pd
import os
import sys
import pathlib


class Passwords:
    def __init__(self, args):
        self.args = args
        home_folder = os.getenv('HOME')
        pathlib.Path(f'{home_folder}/.pss').mkdir(exist_ok=True)
        self.path_passwords = f'{home_folder}/.pss/service_ps.csv'
        self.master_password = f'{home_folder}/.pss/master_ps.txt'

    def _run(self, msg='Register a password using $pss new'):
        if isfile(self.master_password):
            with open(self.master_password, 'r') as f:
                password = input('pass >> ')
                password_encrypt = hashlib.md5(password.encode()).hexdigest()
                password_file = f.read()
                if password_encrypt != password_file:
                    sys.exit('invalid password')
                return password
        else:
            sys.exit(msg)

    def new(self):
        if not isfile(self.master_password):
            password = input('pass >> ')
            with open(self.master_password, 'w') as ps:
                r = hashlib.md5(password.encode())
                ps.write(r.hexdigest())

    def register(self):
        password = self._run('Nothing registered yet')
        name = input('service >> ')
        user = input('user >> ')
        pass_service = input('password >> ')
        if not isfile(self.path_passwords):
            with open(self.path_passwords, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'User', 'Pass'])

        with open(self.path_passwords, 'a') as ps:
            writer = csv.writer(ps)
            writer.writerow([name, user, encrypt(pass_service, password)])

    def show_all(self):
        password = self._run('Nothing registered yet')
        df = pd.read_csv(self.path_passwords)
        for _, row in df.iterrows():
            print(
                f"Name: {row['Name']} | User: {row['User']} | Password: {decrypt(row['Pass'], password)}"
            )

    def remove(self):
        _ = self._run('Nothing registered yet')
        with open(self.path_passwords, 'r') as f:
            csv_rows = csv.reader(f)
            rows_list = list(csv_rows)

        with open(self.path_passwords, 'w') as f:
            writer = csv.writer(f)
            ident = None
            for row in rows_list:
                name = row['Name']

                if name == self.args.name:
                    ident = name

                if ident != name:
                    writer.writerow(row)

    def find_by_key(self):
        password = self._run('Nothing registered yet')
        df = pd.read_csv(self.path_passwords)
        for _, row in df.iterrows():
            if self.args.name == row['Name']:
                print(
                    f"Name: {row['Name']} | User: {row['User']} | Password: {decrypt(row['Pass'], password)}"
                )
