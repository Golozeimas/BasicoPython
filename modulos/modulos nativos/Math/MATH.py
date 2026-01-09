import math

# 1 - o número PI
print(math.pi)
print(f"{math.pi:.2f}")

# 2 - Número de euler
print(math.e)
print(f"{math.e:.2f}")

# 3 - Arredondamento de números
num = 10.3
print(math.ceil(num)) # arredonda pra cima
print(math.floor(num)) # arredonda pra baixo

# 4 - Fatorial de um número
n = 5
print(f"{math.factorial(n)} esse é o fatorial")

# 5 - Potência de números
n2 = 5
print(math.pow(n2, n))

# 6 - MDC
print(math.gcd(6,2)) # isso faz o MDC de n números, só multiplica o que dividir os dois ao mesmo tempo
# enquanto o mmmc seria 6 = 2 . 3

# 7 - Logaritmos
print(math.log(10))