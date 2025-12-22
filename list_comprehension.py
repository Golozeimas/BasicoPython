# [nova_expressao for item in iteravel]

for i in range(10): # o range começa do 0
    if i < 4:
        print(i)

# lista de compressão
list_numbers = [i for i in range(10) if i < 4] # retorna uma lista

print(list_numbers)


film_list = [
        "O Poderoso Chefão",
        "Batman: O Cavaleiro das Trevas",
        "A Lista de Schindler",
        "Pulp Fiction: Tempo de Violência",
        "O Senhor dos Anéis: O Retorno do Rei",
        "Forrest Gump: O Contador de Histórias",
        "Clube da Luta",
        "A Origem",
        "Matrix",
        "Star Wars: O Império Contra-Ataca",
        "Cidade de Deus",
        "O Silêncio dos Inocentes",
        "Interestelar",
        "Parasita",
        "Gladiador",
        "O Rei Leão",
        "Vingadores: Ultimato",
        "Blade Runner 2049",
        "O Labirinto do Fauno",
        "Psicose",
        "O Show de Truman",
        "De Volta para o Futuro",
        "O Resgate do Soldado Ryan",
        "Um Sonho de Liberdade",
        "Os Infiltrados"
    ]

# 1 - filtrar pela a primeira letra "e"

# a função do in no python é verificar se estar dentro da variavel o segundo
# o primeiro verifica com o segundo

e_in_movie = [movie for movie in film_list if "e" in movie.lower()]

print(e_in_movie)

# o .lower() transforma em minúsculos

verificador_de_s = [movie for movie in film_list if "s" in movie.lower()]

print(verificador_de_s)

# 3 - filmes que eu assiti

movie_watched = [movie for movie in film_list if movie != "The godfather"]

print(movie_watched) # filmes que eu assisti

# 4 - números ao quadradado que são pares
quadradado = [x**2 if x % 2 == 0 else "impar" for x in range(10)]
print(quadradado)

# 5 - procurando o filme pelo o nome
# a gente colocar em lower() para tentar encontrar nas letras minúsculas mesmo estando em maiúsculas
# coloquei q para sair do programa
while True:
    seacher = input("Digite o nome do filme (ou saia do programa digitando 'q'):\n")
    if seacher == "q":
        print("saindo do programa...")
        break
    procurar_filme = [movie for movie in film_list if seacher.lower() == movie.lower()]
    if procurar_filme != []:
        print(f"Encontramos o filme, começaremos a reprodução de {seacher.capitalize()} em alguns segundos")
    else:
        print("Nenhum filme com esse nome foi encontrado, tente novamente!")