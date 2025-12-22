film_name = input("Digite o nome do filme: \n")
ratings = int(input("Digite quantas avaliações temos do filme:\n"))

total = 0

for i in range(ratings):
    note = int(input("Avaliação:\n"))
    total += note

average = total/ratings

print(f"Esta é média do {film_name}, média: {average}")