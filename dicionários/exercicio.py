produto1 = input()
preco_do_produto1 = float(input())
produto2 = input()
preco_do_produto2 = float(input())
produto3 = input()
preco_do_produto3 = float(input())

lista_de_produtos = {
    produto1: preco_do_produto1,
    produto2: preco_do_produto2,
    produto3: preco_do_produto3
}

print(lista_de_produtos)

maior_valor_dos_produtos = max(preco_do_produto1, preco_do_produto2, preco_do_produto3)

for chave, valor in lista_de_produtos.items():
    if valor == maior_valor_dos_produtos:
        print(chave)

media_dos_produtos = ((preco_do_produto1+preco_do_produto2+preco_do_produto3)/3)

print(f"{media_dos_produtos:.2f}")