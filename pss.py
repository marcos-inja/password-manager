from passwords import Passwords
import argparse
import sys

HELP = """
[ 1 - criar senha na primeira execução:  pss new                        ]
[ 2 - cadatrar uma nova senha:           pss a                          ]
[ 3 - listar serviços salvos:            pss ls                         ]
[ 4 - remover senha salva:               pss r -ha <hash> ou -n <nome>  ]
[ 5 - recuperar por hash ou nome:        pss ss -h <hash> ou -n <nome>  ]
"""

def main():
    parser = argparse.ArgumentParser(description='gerenciador hehe')
    parser.add_argument('chave', help=HELP)
    parser.add_argument('-n', '--nome', required=False)
    parser.add_argument('-ha', '--hash', required=False)
    args = parser.parse_args()

    funcoes = Passwords(args)

    if args.chave == 'new':
        funcoes.new()

    # Cadastra nova senha
    elif args.chave == 'a':
        funcoes.run(funcoes.cadastra_senha)

    # Lista senhas salvas
    elif args.chave == 'ls':
        funcoes.run(funcoes.lista_senhas, 'Nothing registered yet')

    # Remove uma senha por palavra chave
    elif args.chave == 'r':
        funcoes.run(funcoes.remove, 'Nothing registered yet')

    # Recupera uma unica senha
    elif args.chave == 'ss':
        funcoes.run(funcoes.encotra_por_chave, 'Nothing registered yet')

    else:
        sys.exit('Flag not find!')


if __name__ == '__main__':
    sys.exit(main())
