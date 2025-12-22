def cadastrar_filme():
    list_films = []
    while True:
        filme = input("Digite o filme que deseja cadastrar: ('q' para sair) \n")
        list_films.append(filme)
        if filme == "q":
            break
        print("Essa é a lista de filmes cadastrados: ")
        for filme in list_films:
            print(filme.capitalize())
cadastrar_filme()