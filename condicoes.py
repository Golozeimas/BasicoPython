film_name = input("Nome do filme?\n")
year_release = int(input("Data de lançamento?\n"))
rating = float(input("Nota para o filme?\n"))

if rating > 8 and year_release > 2000:
    print(f"o filme {film_name} tem a seguinte nota {rating}")

if not rating:
    print("sem nota")
    
else:
    print("não recomendo esse filme")
