# criando um dicionário
pessoa= {
    "nome": "Gabriel",
    "idade": 20,
    "cor_dos_olhos": "azuis",
    "altura": 1.80,
    "hobbys":["videogame", "filmes", "animes"] # dicionários aceitam também listas
}

# 1 - printando um dicionário
print(pessoa["nome"])
print(pessoa["idade"])

# 2 - alteração e adição no dicionário
pessoa["nome"] = "matheus"
pessoa["profissao"] = "dev" # adiciona no dicionario "pessoa", mesmo não existindo essa chave lá

print(pessoa["nome"])
print(pessoa["profissao"])

# 3 - percorrendo um dicionário (comum em api's e banco de dados)
for chave,valor in pessoa.items():
    print(chave, "->", valor)

# 4 - algumas funções importantes
print(pessoa.items()) # retorna chave + valor
print(pessoa.keys()) # retorna as chaves
print(pessoa.values()) # retorna os valores
print(pessoa.get("cpf","não encontrado, tente novamente")) # serve para encontrar chaves nos dicionários, 
                                                           # se não encontrado assume o segundo valor, geralmente aviso de erro