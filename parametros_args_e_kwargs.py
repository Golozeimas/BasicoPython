"""
*args para quando não sabe quantos argumentos irá receber, são passados como tuplas
**kwargs além dos valores podemos passar as respctivas chaves, são passado como dicionário

"""
def sum(*num):
    sum_total = 0
    for x in num:
        sum_total += x
    return sum_total

print(sum(1,1,2,2)) # é passado em formato de tupla, para a função

def apresentacao(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print("Apresentação dos cursos")
apresentacao(name="Python", nivel = "Initial", category="Basic of programming")
apresentacao(name="Java com SpringBoot", nivel="Intermediário", category="API's")
