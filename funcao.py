def impressao_de_mensagens_apenas_string(mensagem):
    if type(mensagem) == str:
        print(mensagem)
    else:
        print("não é uma string!")

impressao_de_mensagens_apenas_string("como estar?")
impressao_de_mensagens_apenas_string(1)
impressao_de_mensagens_apenas_string(True)
impressao_de_mensagens_apenas_string(12.13)

for i in range(10):
    impressao_de_mensagens_apenas_string("Gol!")

def calcular_media_de_tres_notas():
    nota1 = float(input("Digite a primeira nota: \n"))
    nota2 = float(input("Digite a segunda nota: \n"))
    nota3 = float(input("Digite a terceira nota: \n"))
    media = (nota1 + nota2 + nota3) / 3
    return media


print(f"média: {calcular_media_de_tres_notas():.2f}")