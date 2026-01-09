import statistics

# 1 - média - soma e divide pelos elementos
n = statistics.mean([5,6,7,8]) # é passado como uma lista, para tirar a média dos itens
print(n)

# 2 - mediana - núemro do meio, em caso de par, soma e depois dividi por 2
mediana = statistics.median([1,3,5,7]) # faz a mediana de uma lista de números
print(mediana)

# 3 - moda - número que mais se repete, pode ser string também
moda = statistics.mode([3,4,3,2,3,4,3,5,3,5,2,1,3])
print(moda)

# 4 - desvio padrão
"""
 - Quanto mais próximo de zero for, significa que os dados estão menos dispersos
"""
desvio_padrao = statistics.stdev([4.5,3.2,1,2.3])
print(desvio_padrao)


"""
def mean (*n):
    if len(n) == 1:
        for i in n: # esse for funciona muito bem com lista e tals
            return i
    if len(n) > 1:
        return sum(n)/len(n)

print(mean(10))
"""