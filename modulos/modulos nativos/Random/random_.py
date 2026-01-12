import random
import time

# 1 - selecionar valor aleatório com base em uma lista
lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
sorteio = random.choice(lista_de_numeros)
print(sorteio)

# 2 - selecionar valor com base num vão de listas
r1 = random.randint(10,100)
print(r1)

# programa de sorteio de uma ganhador de uma moto
lista_de_sorteados = ["Ana", "Gabi", "Lucas", "Matheus", "Luiza"]
print("Começando o sorteio...")
time.sleep(5)
sorteado = random.choice(lista_de_sorteados)
print(f"Parabéns a(o) {sorteado}!")

# 3 - seleciona caractere aleatório, usamos o mesmo choice
nome = "matheus"
s = random.choice(nome)
print(s)

# 4 - corta uma parte de uma lista e a sorteia
# random.sample(lista, quantidade de partes que sobra)
r2 = random.sample(lista_de_numeros, 2)
r3 = random.sample(lista_de_numeros, 3)
print(r2)
print(r3)

# 5 - programa de adivinhação
done = False
while not done:
    print("======= Jogo de adivinhação =======")
    print("1 - Adivinhar número")
    print("2 - Sair")
    seletor = int(input(">"))
    if seletor == 1:
        print("===== Número entre 1 a 10 =====")
        num_sorteado = random.randint(1,10)
        num_escolhido = int(input(">"))
        if num_sorteado == num_escolhido:
            print("Parabéns! você acertou")
        else:
            print("Errou, tente novamente!")
    elif seletor == 2:
        print("Saindo...")
        time.sleep(3)
        done = True

# 6 - embaralha os elementos da própria lista
print("Embaralha os elemento da lista de números:\n")
random.shuffle(lista_de_numeros) # não podemos printar diretamente só depois acredito por se tratar de um algoritmo de percorrimento mais complexo
print(lista_de_numeros)