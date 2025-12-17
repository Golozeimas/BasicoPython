movieName = "Um sonho de liberdade"; # string de 20 posições

# string[inicio : fim] -> índice começa na posição a 0 / índice final - 1 é assim que conta string e matrizes

# 1 - Buscar toda a string a partir da posição 0
print(movieName[0:])

# 2 - Buscar toda a string até a ultima posição
print(movieName[:21])

# 3 - Buscar da terceira posição até a ultima posição
print(movieName[2:])

# 4 - Inversão de um array
array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(array[::-1])

# 5 - Usando o passo
print(array[0:10:2])

# 6 - Buscar todos os números ímpares
numeros_impares = [0,1,2,3,4,5,6,7,8,9]

print(numeros_impares[1::2])