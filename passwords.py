import sqlite3
import os


def clear(): return os.system('clear')


MASTER_PASSWORD = '123456'

password = input("Insira sua senha: ")
if password != MASTER_PASSWORD:
    print("Senha inválida, encerrando...")
    exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
""")


def menu():
    print('')
    print('O que deseja fazer?')
    print('******************************')
    print('* i : inserir nova senha     *')
    print('* l : listar serviços salvos *')
    print('* r : recuperar uma senha    *')
    print('* a : apagar uma senha       *')
    print('* s : sair                   *')
    print('******************************')
    print('')


def get_password(service):
    cursor.execute(f"""
        SELECT username, password FROM users
        WHERE service = '{service}'
    """)

    if cursor.rowcount == 0:
        print('Serviço não encontrado')
    else:
        for user in cursor.fetchall():
            print(user)


def insert_password(service, username, password):
    cursor.execute(f"""
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
    """)
    conn.commit()


def show_service():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)


def delete_service(service):
    cursor.execute(f"""
        DELETE FROM users WHERE service = '{service}'
    """)


while True:
    menu()
    reply = input('Qual a opção? R: ').lower()
    if reply not in ['i', 'l', 'r', 's', 'a']:
        print('')
        print('Opção inválida')
        print('')
        continue

    if reply == 's':
        clear()
        break

    elif reply == 'i':
        clear()
        print('Inserir nova senha')
        service = input('Qual o nome do serviço? ')
        username = input('Qual o nome de usúario? ')
        password = input('Qual a senha? ')
        insert_password(service, username, password)

    elif reply == 'l':
        clear()
        print('Serviços salvos: ')
        show_service()

    elif reply == 'r':
        clear()
        print('Ver senha: ')
        service = input('Digite o nome do serviço: ')
        get_password(service)

    elif reply == 'a':
        clear()
        print('Apagar uma senha: ')
        service = input('Digite o nome do serviço: ')
        delete_service(service)
        print(f'{service} foi apagado com sucesso!')

conn.close()
