# soma com lambda
soma = lambda a,b: print("Soma dos números usando lambda: ", a+b)

soma(20,30)
soma(100, 200)

# verifica se é par
is_even = lambda num : num % 2 == 0

print(is_even(2))
print(is_even(3))

# faz potencia com 2
potency_with_two = lambda num: num ** 2

print(potency_with_two(20))

# inverte uma string
reverse_string = lambda string: string[::-1]

print(reverse_string("Stand"))
print(reverse_string("People"))

# Com exemplos de filmes
movie_list = ["Titanic", "The batman", "Karâte kid", "Jumanji"]

ratings = {
    "Titanic" : [10, 6, 9],
    "The batman" : [8, 9, 10],
    "Karâte kid": [6, 8, 9],
    "Jumanji":[7, 8, 6]
}

# lambda para média dos filmes
average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

print("Essas é média das notas de titanic: ", round(average_rating("Titanic"), 2))

# lambda para ver se existe na lista
is_movie_real = lambda movie_name: movie_name in movie_list

print(f"Existe o filme The batman? {is_movie_real("The batman")}")
print(f"Existe o filme hora do rush? {is_movie_real("hora do rush")}")