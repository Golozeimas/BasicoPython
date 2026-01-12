import hashlib

# 1 - Verifica quantos algoritmos são disponíveis
print(hashlib.algorithms_available)

print("\n")

# 2 - Verifica os algoritmos de acordo com SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o SHA256
algoritmo = hashlib.sha256()
senha = "1234".encode()
algoritmo.update(senha)
print(algoritmo.hexdigest())

# outra forma de utilizar
senha2 = "Sigma"
hash_obj = hashlib.sha256(senha2.encode()) # o encode se faz necessário pois o hash só processa bytes e não texto
hash_hex = hash_obj.hexdigest() # transforma tudo em hexadecimal
print(hash_hex)

# 4 - Utilizando o MD5 (NÃO É RECOMENDADO, MUITO FRACO PARA SEGURANÇA)
senha3 = "1234"
hash_obj = hashlib.md5(senha3.encode())
hash_hex = hash_obj.hexdigest()
print(hash_hex)