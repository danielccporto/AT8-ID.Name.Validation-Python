<p align="center">
    <img src="assets/logo_infnet.png" width="70" height="70" />
</p>

# *Assessment*

## Exercício 8

**Atenção:**
- É importante que você desenvolva o programa totalmente, do início ao fim, na IDE do Replit (**AQUI MESMO!!**⚠️**NÃO crie um repl no seu perfil do Replit para fazer o Assessment**⚠️). Você **NÃO** deve escrever o código em outra IDE e depois copiá-lo para cá.
- **NÃO** é permitido usar nenhum recurso que não faça parte do conteúdo desta disciplina, a menos que explicitamente autorizado no enunciado.
- Use comentários para explicar o que cada parte do código faz.
- Após concluir as tarefas, submeta suas soluções aqui e no Moodle (postando lá os links para seus projetos do Replit).

Neste exercício, você deverá criar uma nova versão do programa do Exercício 7, incluindo a validação de ID e Nome conforme a descrição a seguir.

## Validação de entrada

Caso um valor de entrada inválido seja detectado, o programa deverá notificar o usuário, **detalhando o problema identificado**, e encerrar a funcionalidade que estava sendo executada, retornando ao menu.

**Atenção:**

- Apenas as validações especificadas a seguir são necessárias. Considere que o usuário respeitará todos os demais aspectos não cobertos por estas especificações.
- Uma revisão dos métodos de strings pode ser útil: https://www.w3schools.com/python/python_ref_string.asp

### ID

O ID é um nº inteiro positivo que identifica cada cadastro. Esse nº corresponderá à posição de cada cadastro na estrutura de armazenamento. Ou seja, o ID do 1º cadastro será 1, o do 2º será 2 e assim sucessivamente.

Sempre que uma funcionalidade requerer um ID informado pelo usuário, o programa deverá verificar se o ID recebido é válido no contexto em questão.

Por exemplo: não é possível remover um cadastro com ID inexistente; na inserção de um novo cadastro, o campo ID deve ser deixado em branco, ou ser um ID já em uso, ou ser o próximo ID que não estiver em uso (lembrando que a sequência de IDs começa em 1).

### Nome

Como especificado para os dados do cadastro, o nome deve ser composto por primeiro nome e um único sobrenome.

O programa pode aceitar que o usuário informe o primeiro nome e o sobrenome com quaisquer combinações de maiúsculas e minúsculas, mas deverá ajustá-los para que a 1ª letra seja maiúscula e as demais minúsculas. Além disso, deverá verificar se são compostos por uma única palavra (ou seja, sem espaços).