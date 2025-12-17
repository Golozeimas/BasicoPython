nota1 = float(input("Digite a primeira nota: \n"))
nota2 = float(input("Digite a segunda nota: \n"))

# Aritméticos
sum = nota1 + nota2
sub = nota1 - nota2
div = nota1 / nota2
mult = nota1 * nota2
# o resultado é o resto da divisão
mod = nota1 % nota2
# o resultado é uma exponencial
exp = nota1 ** nota2

print(f"Soma das notas: {sum}\n"
      f"Resto das notas: {mod}\n"
      f"Exponencial das notas: {exp}"
      )

print(f"Só divisão: {div} e multiplicação: {mult}")