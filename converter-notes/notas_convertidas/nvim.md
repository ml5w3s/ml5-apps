
--- 
title: "nvim"
created: "2025-02-06T17:50:54,809815Z"
updated: "2025-07-09T15:12:57,503960Z"
tags: []
--- 

nvim

O Vim é um editor de texto avançado que oferece suporte a painéis, que são janelas divididas dentro do editor que podem exibir vários arquivos ou saídas de comandos ao mesmo tempo. Você pode usar painéis no Vim para visualizar e editar vários arquivos ao mesmo tempo ou para exibir a saída de comandos enquanto edita um arquivo.

    CTRL-W + h/j/k/l - move o cursor para o painel à esquerda/abaixo/acima/à direita.
    CTRL-W + +/=/- - aumenta/redimensiona/diminui o tamanho do painel atual.
    CTRL-W + q - fecha o painel atual.

Para gerenciar painéis no Vim, você pode usar os seguintes comandos:

    :split - divide a janela atual em dois painéis, um acima do outro.
    :vsplit - divide a janela atual em dois painéis, um ao lado do outro.

ctlr+w < diminue o tamanho do painel na vertical e ctrl++ na horizontal

Emmet => tags>tag#id$*5>a ctrl+y ,

Apagar espaços e numeração de linha copiadas de uma só vez, no modo normal:
:%s/^\s*\d\+\s*//
