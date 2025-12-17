nomes = ("matheus", "lucas", "gabriel")

print(type(nomes))

# 1 - buscar os dois primeiros elementos da tupla
print(nomes[0:2])

# 2 - buscar o ultimo elemento da tupla
print(nomes[-1])

# 3 - buscar algum elemento no meio
print(nomes[:3]) # todos os elementos :fim - 1 (começando do 0)

# 4 - buscar filmes de uma posição em diante
print(nomes[2:])

# 5 - buscar por index
print(nomes.index("matheus")) # posição 0