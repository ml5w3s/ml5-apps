# Conversor de Notas Gnote para Markdown

Este script converte todas as notas do Gnote para o formato Markdown, com metadados YAML, para que possam ser importadas em outros aplicativos como o QOwnNotes.

## Como Usar

1.  Certifique-se de que você tem o Python 3 instalado.
2.  Execute o script a partir do seu terminal:

    ```sh
    python3 converter.py
    ```

3.  O script irá procurar automaticamente por suas notas do Gnote no diretório `~/.local/share/gnote/`.
4.  Os arquivos convertidos no formato `.md` serão salvos na pasta `notas_convertidas/`.

## Formato de Saída

Cada nota será convertida para um arquivo `.md` contendo um cabeçalho YAML com os seguintes metadados:

-   `title`: O título da nota.
-   `created`: A data de criação original.
-   `updated`: A data da última modificação.
-   `tags`: Uma lista de tags associadas à nota.
