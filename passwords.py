import sqlite3
import os


# Usado para limpar o terminal
def clear(): return os.system('clear')


# Defino a senha
MASTER_PASSWORD = '123456'

password = input("Insira sua senha: ")
if password != MASTER_PASSWORD:
    print("Senha inválida, encerrando...")
    exit()

# Conectando ao banco, se não existir ele cria um novo
conn = sqlite3.connect('passwords.db')

# Definindo o cursor do banco
cursor = conn.cursor()

# Criando uma tabela, caso não exista
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
""")


# Criando o as opções do menu
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


# Função que mostra as senhas
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


# Função que insere um novo serviço
def insert_password(service, username, password):
    cursor.execute(f"""
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
    """)
    conn.commit()


# Função que mostra todos os serviços
def show_service():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)


# Função que deleta um serviço
def delete_service(service):
    cursor.execute(f"""
        DELETE FROM users WHERE service = '{service}'
    """)


while True:
    # Chama o menu
    menu()
    reply = input('Qual a opção? R: ').lower()
    # Se não for uma dessas opções ele informa
    if reply not in ['i', 'l', 'r', 's', 'a']:
        print('')
        print('Opção inválida')
        print('')
        continue

    # Caso a opção seja s, ele sai
    if reply == 's':
        clear()
        break

    # Inserir nova senha
    elif reply == 'i':
        clear()
        print('Inserir nova senha')
        service = input('Qual o nome do serviço? ')
        username = input('Qual o nome de usúario? ')
        password = input('Qual a senha? ')
        insert_password(service, username, password)
        print(f'{service} foi inserido com sucesso!')

    # Lista todos os serviços salvos
    elif reply == 'l':
        clear()
        print('Serviços salvos: ')
        show_service()

    # Recupera uma senha, pelo nome do serviço
    elif reply == 'r':
        clear()
        print('Ver senha: ')
        service = input('Digite o nome do serviço: ')
        get_password(service)

    # Apaga uma senha, pelo nome do serviço
    elif reply == 'a':
        clear()
        print('Apagar uma senha: ')
        service = input('Digite o nome do serviço: ')
        delete_service(service)
        print(f'{service} foi apagado com sucesso!')

# Fechando conecção com o banco
conn.close()
