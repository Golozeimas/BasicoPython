import re

text = "Cursos de python são bons demais"

# 1 - Índice inicial e final de um texto
# o 'r' significa raw string ou string bruta, sem tratamento
match = re.search(r"python", text) # a search serve para procurar no texto original, e utilizar completamente
print(f"índice inicial: {match.start()}") # com o match pesquisado conseguimos usar para procurar o ind. inical e final
print(f"índice final: {match.end()}")


# 2 - Buscando o índice que possui ponto
site = "https://www.com"
# re.search(r -> usado no serch 'regra de descoberta', texto)
match = re.search(r"\.", site) # quero descobrir o índice do ponto
print(match) # se printamos só o match, conseguimos ver entre onde estar

# 3 - Buscando uma lista de caracteres em um texto
text1 = "crash bandicoot"
pattern = "[a-c]" # busca tem que ser feita em colchetes e com o delimitador
result = re.findall(pattern, text1) # re.findall(regra de busca para achar todos os caracterers desejados, texto)
print(result) # tenta achar os caracteres entre a e c e retorna uma lista com a's e c's

# 4 - Verificando o ínicio de uma string
rule = r'^A'
phrases = ["A liberdade absoluta é odiosa", "O ser humano é o lobo dele mesmo", "A vida é díficil", "Bitch makes me cry"]
for f in phrases:
    if re.match(rule, f) != None: # re.match (regra, texto)
        print(f"Corresponde a regra absoluta: {f}")
    else:
        print(f"Não corresponde a regra absoluta: {f}")

# 5 - Verificando o final de uma string
rule_end = r"!$" # o r no ínicio da sentido para o regex, se não seria solto
phrase2 = "O dia está ensolarado!"
match = re.search(rule_end, phrase2)
if match:
    print("Sim, a frase está correta!")
else:
    print("Não, a frase está incorreta")