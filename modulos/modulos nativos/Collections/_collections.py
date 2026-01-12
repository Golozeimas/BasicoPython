from collections import Counter,namedtuple,deque
from operator import itemgetter

# 1 - lista de frutas e eu quero contar as repetidas
lista_de_frutas = ["Maçã", "Mamão", "Uva", "Uva", "Pêra", "Abacate", "Banana", "Banana", "Banana"]
contador = Counter(lista_de_frutas) # Conta elementos de forma automática, ideal para frequências e repetições
print(contador)

# 2 - tuplas nomeadas
games = namedtuple("Games", ["nome", "nota", "genero"]) # serve para separar por chave e valor como se fosse um dicionário
g1 = games("Resident evil 4 remake", 10.0, "Survival horror")
g2 = games("The witcher 3", 9.5, "Action/Adventure")
print(g1)
print(g2)

# 3 - ordenando dicionários
nome_e_idade = {"Pedro": 35, "Matheus": 20, "Maria": 18, "Beatriz": 16}

ordernados = sorted(nome_e_idade.items(), key = itemgetter(0)) # ordene as chaves e valores, e o key = itemgetter(0), siginifica para ordenar
                                                               # pela a chave, se fossse itemgetter(1) era pelo o valor

print(ordernados)

# 4 formato de fila
fila_de_numeros = deque([1,2,4,6,7,5,3])

fila_de_numeros.append(7) # adiciona na direita, ultimo elemento

print(fila_de_numeros)

fila_de_numeros.appendleft(10) # adiciona na esquerda

print(fila_de_numeros)

fila_de_numeros.pop() # retira na direita

fila_de_numeros.popleft() # retira na esquerda

print(fila_de_numeros)