Este documento serve como guia de navegação para os arquivos e diretórios presentes neste projeto de estudo da linguagem Python. O conteúdo está organizado de forma a separar scripts de conceitos básicos, funções específicas e módulos avançados.

Estrutura de Pastas e Arquivos
Abaixo encontra se o detalhamento do conteúdo de cada diretório principal.

1. Diretório Raiz (Conceitos Fundamentais)
Nesta pasta encontram se os scripts introdutórios que não dependem de outros ficheiros para execução. Eles cobrem a sintaxe essencial da linguagem.

hello_world.py: Script inicial para teste de ambiente.

tipos_de_dados.py: Exemplos de declaração de variáveis e tipagem dinâmica.

input.py e concatena.py: Interação básica com o utilizador e formatação de saídas.

operadores.py: Demonstração de operações matemáticas fundamentais.

condicoes.py e condicoes_pt2.py: Lógica de decisão (if/else) e operações condicionais.

Loops (for.py, while.py, range.py): Estruturas de repetição para iteração de dados.

Funções (funcao.py, lambda.py, recursiva.py): Definição de métodos, funções anónimas e recursividade.

2. Pasta: dicionários
Focada na estrutura de dados de chave valor (dict).

dicionario.py: Introdução à sintaxe, métodos .get(), .keys() e .values().

dicionario_embelezado.py: Uso da biblioteca pprint para visualização organizada de dados complexos.

exercicio.py: Aplicação prática de dicionários para cadastro de produtos e preços.

3. Pasta: funções da lista
Scripts dedicados à manipulação de listas (arrays).

lista.py: Criação e acesso a índices.

metodos_listas.py: Métodos nativos como .append(), .sort(), .remove() e .clear().

4. Pasta: funções de string
Manipulação e tratamento de textos.

strings.py: Métodos de formatação como .upper(), .lower() e .replace().

slice.py: Técnicas de fatiamento de strings e arrays.

5. Pasta: modulos
Exemplos de como criar, importar e organizar código em múltiplos arquivos, simulando a arquitetura de projetos maiores.

Arquivos de Módulo: math_operations.py (cálculos) e string_utils.py (texto) contêm funções reutilizáveis.

main.py: Script principal que importa e executa as funções definidas nos módulos acima.

Subpasta: modulos nativos
Exploração das bibliotecas padrão ("Built in") do Python.

Collections: Uso de Counter, namedtuple e deque.

Hashlib: Exemplos de criptografia e hashing (SHA256, MD5).

Math e Statistic: Operações matemáticas avançadas e estatísticas descritivas.

OS: Comandos de sistema operacional como listar diretórios e limpar o terminal.

Random: Geração de números aleatórios e jogos de sorteio.

Regex: Expressões regulares para busca de padrões em texto.

Notas de Execução
Alguns scripts, especialmente os que utilizam input(), requerem interação via terminal. Para executar um módulo que está dentro de uma subpasta, certifique se de que o diretório de trabalho do seu terminal está correto ou ajuste os caminhos de importação conforme necessário.
