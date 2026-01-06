def sum(x, y):
    return x + y

def substraction(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divider(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Não se pode dividir por zero, never!")