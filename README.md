# Gerenciador de senhas 
Feito para ser o mais simples possivel, como eu estava com preguiça de abrir um gerenciador de senhas gráfico, resolvi fazer esse para ser usado no terminal, meio que sigo o KISS nesse gerenciador haha.
## Para configurar o gerenciador
- Ter o Python 3.8+ instalado assim como o PIP.
- Então rodar:
    ```sh
    pip install -r requirements.txt
    ```
## Para usar
Antes de tudo devemos criar uma senha:
```sh
python3 pss.py new
```
- Para cadastrar um novo serviço:
    ```sh
    python3 pss.py a
    ```
- Para listar todos os serviços:
    ```sh
    python3 pss.py ls
    ```
- Para exibir um serviço especifico:
    ```sh
    python3 pss.py ss -n <nome_do_serviço>
    ```
    > Remova o <> antes de executar
- Para remover um serviço:
    ```sh
    python3 pss.py r -n <nome_do_serviço>
    ```
    > Remova o <> antes de executar

Para editar, simplesmente apague o serviço que tem algo errado e re-cadastre, é bem mais simples hehe.
