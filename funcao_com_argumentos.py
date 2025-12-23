def nome_completo(firstname, lastname):
    print(f"{firstname} {lastname}")

nome_completo("João", "Matheus")

def sum (a, b):
    return a + b

print(sum(10,5))

# parâmetro com default (valor padrão pra caso eu chame a função e não coloque nada)
def address(address = "Brazil"):
    print(f"Eu moro em {address}")

address()
address("chile")

def rate_movie(ratings, movie_name):
    total = 0
    for i in range(ratings):
        note = float(input("Digite a(s) nota(s):"))
        total += note
    average = total / ratings
    print(f"Essa é a média: {average:.2f}, e esse é o nome do filme: {movie_name}")

rate_movie(3, "sexta feira 13")