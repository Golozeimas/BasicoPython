name = input("Digite o nome do filme:\n")
ano_de_lancamento = int(input("Digite o ano de lançamento: \n"))
nota = float(input("Digite a nota do filme: \n"))

# Alternativa 1 de concatenação
print("Dados do filme")
print("=" * 10)
print("Este é o nome do filme: ", name)
print("Este é o ano de lançamento: ", ano_de_lancamento)
print("Esta é a nota do filme", nota)

# Alternativa 2 de concatenação
print("Dados do filme")
print("=" * 10)
print("Nome do filme: \n",name,"Ano de lançamento: \n", ano_de_lancamento, 
      "Nota do filme: \n", nota)

# Alternativa 3 de concatenação
print("Dados do filme")
print("=" * 10)
print(f"Nome do filme: {name}\n"
      f"Ano de lançamento: {ano_de_lancamento}\n"
      f"Nota do filme: {nota}"
      )

