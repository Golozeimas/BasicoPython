movie_list = ["Superman", "The batman", "Homem aranha de volta ao lar"]

# para cada filme em lista de filmes, ler assim
for movie in movie_list:
    print(movie)

print("="*20)

# se queremos encerrar a repetição
for movie in movie_list:
    if movie == "The batman":
        break
    print(movie)

print("="*20)

# se queremos continuar apenas pulando o que estar no momento
for movie in movie_list:
    if movie == "The batman":
        continue
    print(movie)

num = [2, 3, 4 , 5 , 4 ,3 ,9]

for i in num:
    if i % 2 == 0:
        print("par")
    else:
        print('impar')

