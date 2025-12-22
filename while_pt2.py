
# avaliacao de animes com while
anime_name = input("Digite o nome do anime:\n")
ratings = int(input("Digite o número de avaliações do anime:\n"))

total = 0
count = 0
while count < ratings:
    note = int(input("Digite a nota do anime:\n"))
    total += note
    count += 1

average = total/ratings 

print(f"no anime: {anime_name}, a média de notas é {average}")