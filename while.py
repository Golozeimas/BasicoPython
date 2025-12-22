anime_list = ["naruto", "bleach", "one piece"]

# em uma lista é melhor for do que while
# para o while precisamos do index

# printando de trás pra frente, vale lembrar que o len pega do 1 até o fim, e a lista começa do 0 na posição
index = len(anime_list)

while index > 0:
    index -= 1
    print(anime_list[index])
   
# parando ao chegar em um determinado elemento
index = len(anime_list)
i = 0
while i < index:
    if anime_list[i] == "one piece":
        break
    print(anime_list[i])
    i += 1


# continuando depois de chegar em um determinando elemento, não printa esse elemento
index = len(anime_list)
i = 0
while i < index:
    if anime_list[i] == "naruto":
        continue
    print(anime_list[i])
    i += 1
