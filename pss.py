from passwords import Passwords
import argparse
import sys

HELP = """
[ 1 - criar senha na primeira execução:  pss new                         ]
[ 2 - cadatrar uma nova senha:           pss add                         ]
[ 3 - listar serviços salvos:            pss ls                          ]
[ 4 - remover senha salva:               pss r -ha <hash> or -n <name> ]
[ 5 - recuperar por hash ou nome:        pss l -h <hash> or -n <name>    ]
"""

def main():
    parser = argparse.ArgumentParser(description='KISS password manager')
    parser.add_argument('key', help=HELP)
    parser.add_argument('-n', '--name', required=False)
    parser.add_argument('-ha', '--hash', required=False)
    args = parser.parse_args()

    passwords = Passwords(args)

    if args.key == 'new':
        passwords.new()

    # Cadastra nova senha
    elif args.key == 'add':
        passwords.register()

    # Lista senhas salvas
    elif args.key == 'ls':
        passwords.show_all()

    # Remove uma senha por palavra chave
    elif args.key == 'r':
        passwords.remove()

    # Recupera uma unica senha
    elif args.key == 'l':
        passwords.find_by_key()

    else:
        sys.exit('Flag not find!')


if __name__ == '__main__':
    sys.exit(main())
