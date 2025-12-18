set_lista = {1,2,3,4,5,3}

# 1 - não aceita elementos repetidos
print(set_lista)

# 2 - formas diferentes de usar o set
banana_sem_repetir_letras = set("banana")
print(banana_sem_repetir_letras)

# 3 - dar update no set (sem repetir elementos)
set_lista.update(banana_sem_repetir_letras)
print(set_lista)

# 4 - remover da lista
set_lista.remove(1)
print(set_lista)

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

numeros_sem_repeticao = {num1, num2, num3, num4 num5}

print(numeros_sem_repeticao)

print(len(numeros_sem_repeticao))

print(max(numeros_sem_repeticao))
