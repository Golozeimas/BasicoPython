# esse import melhora os json's e também os dicionários consequentemente
import pprint

# geralmente um dicionário é assim, lembrando o formato json
film_list = {
    "circulo de fogo":{
        "genres":["action", "sci-fi"],
        "productor":"sony",
        "note": 10
    },
    "Predador":{
        "genres":["suspense", "action"],
        "productor": "paramount",
        "note": 9.5
    },
    "Se beber não case":{
        "genres":["comedy"],
        "productor": "mizaky",
        "note": 7.5
    }
}
print("sem a formatação ideal: ")
print(film_list)
print("com a formatação ideal: ")
pprint.pp(film_list)

# 1 - adicionando em um dicionario de dicionario
film_list["circulo de fogo"]["sells"] = 100000000
pprint.pp(film_list)

# 2 - buscar informação dentro deles
print(film_list["Se beber não case"]["note"])

# 3 - excluir um dicionário
del film_list["Se beber não case"]
pprint.pp(film_list)
