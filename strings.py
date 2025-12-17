nome1 = "Camaro amarelo"
nome2 = "camaro amarelo"

# retorna falso pois o python é case sensitive
print(nome1 == nome2)

descricao_do_filme = """
                    É um filme de terror muito tenso, e extremamente aterrorizante
                    pessoas desmaiaram assistindo isso
"""



print(descricao_do_filme)

# Multiplicação de strings
# facilita a parte de criação de menus e outras coisas
print("=" * 20)

# Procura a palavra terror na string
if("terror" in descricao_do_filme):
    print("filme de terror!")
else:
    print("não é um filme de terror!")
