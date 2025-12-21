num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo númeoro: \n"))
operation = input("Digite a operação desejada: \n")

if operation == "+":
    temp = num1 + num2
    print(temp)
elif operation == "-":
    temp = num1 - num2
    print(temp)
elif operation == "*":
    temp = num1 * num2
    print(temp)
elif operation == "/":
    if num2 == 0:
        print("não é possivel dividir por zero\n")
        exit()
    temp = num1 / num2
    print(temp)
else:
    print("operação inválida!")