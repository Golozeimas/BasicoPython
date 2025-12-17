films_list = ["harry potter", "donnie darko", "homem aranha", "superman"]

nome = "matheus"

print(len(nome)) # o len pode ser usado tanto em strings (saber número de letras) 
                 # quanto em arrays para saber o número de elementos
# 1- tamanho da lista
print(len(films_list))

# 2 - busca pelo o nome do elemento
print(films_list.index("harry potter")) # retorna 0

# 3 - adiciona elemento no final da lista
films_list.append("todo mundo em pânico!")
print(films_list)

# 4 - Ordena a lista
films_list.sort()
print(films_list)

# 5 - copiar e remover um elemento da lista
copy_list = films_list.copy()
copy_list.remove("superman")
print(copy_list)

# 6 - remove todos os elementos da lista
films_list.clear()
print(films_list)