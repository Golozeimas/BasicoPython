# fatorial de um numero
def fatorial(numero):
        if numero == 1:
                return numero
        return numero * fatorial(numero-1)

'''
Para fazer o fatorial temos que usar
'''
input_do_numero = int(input("Digite o número fatorial: \n"))

print(f"Esse é o número: {input_do_numero}, e o seu fatorial: {fatorial(input_do_numero)}")

def soma_total_de_um_numero(numero):
        if numero == 1:
            return numero
        else:
            return soma_total_de_um_numero(numero - 1) + numero

soma_total = int(input("Digite o número que quer fazer a soma total: \n"))
print(f"Este é o número escolhido: {soma_total}, e essa é a soma total: {soma_total_de_um_numero(soma_total)}")