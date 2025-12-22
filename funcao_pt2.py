def avaliador_de_notas():
    avaliacoes = int(input("Digite quantas avaliações deseja fazer: \n"))
    avaliacoes += 1
    total = 0
    i = 1
    while i < avaliacoes:
        nota = float(input(f"Digite a {i} nota: \n"))
        total += nota
        i += 1
    media = total / (avaliacoes - 1)
    
    print(f"Essa é a média dessas notas: {media:.2f}")

avaliador_de_notas()