# Gerenciador de senhas 
Feito para ser o mais simples possível, como eu estava com preguiça de abrir um gerenciador de senhas gráfico, resolvi fazer esse para ser usado no terminal, meio que sigo o KISS nesse gerenciador haha!
## Para configurar o gerenciador
- Ter o Python 3.8+ instalado assim como o PIP.
- Então rodar:
    ```sh
    pip install -r requirements.txt
    ```
## Uso de maneira amigável
Isso serve para executar em qualquer diretorio sem precisa passar o caminho completo.

### Primeiramente vamos criar uma váriavel no .bashrc ou .zshrc:

Dentro do diretorio `gerenciador-de-senhas` execute `pwd` para pegar o caminho completo. volte para o diretorio de usuario e abra o **.bashrc ou .zshrc** adicione a seguinte linha

```sh
export pss=<diretorio_pego_com_pwd>/pss.py
```
- Exemplo:
![image](https://user-images.githubusercontent.com/76446913/138572625-baf6852d-9da1-4d27-b627-cfad5ff82148.png)


Saia e `source .zshrc` ou `source .bashrc`
- Devemos criar uma senha:
    ```sh
    python $pss new
    ```
- Para cadastrar um novo serviço:
    ```sh
    python3 $pss add
    ```
- Para listar todos os serviços:
    ```sh
    python3 $pss ls
    ```
- Para exibir um serviço especifico:
    ```sh
    python3 $pss l -n <nome_do_serviço>
    ```
    > Remova o <> antes de executar
- Para remover um serviço:
    ```sh
    python3 $pss r -n <nome_do_serviço>
    ```
    > Remova o <> antes de executar

## Para usar dentro do diretório raiz
Antes de tudo devemos criar uma senha:
```sh
python3 pss.py new
```
- Para cadastrar um novo serviço:
    ```sh
    python3 pss.py add
    ```
- Para listar todos os serviços:
    ```sh
    python3 pss.py ls
    ```
- Para exibir um serviço especifico:
    ```sh
    python3 pss.py l -n <nome_do_serviço>
    ```
    > Remova o <> antes de executar
- Para remover um serviço:
    ```sh
    python3 pss.py r -n <nome_do_serviço>
    ```
    > Remova o <> antes de executar

Para editar, simplesmente apague o serviço que tem algo errado e cadastre novamente, é bem mais simples hehe.
