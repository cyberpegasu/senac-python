soma = 6 + 5
multiplicacao = 2 * 6

# E
if soma > 10 and multiplicacao > 10:
    print("a soma e a multiplicação são maior que 10")
else:
    print("a soma e a multiplicação não são maior que 10")

# OU
if soma > 11 or multiplicacao > 11:
    print("a soma ou multiplicação são maiores que 11")
else:
    print("nem a soma nem a multiplicação são maiores que 11")

# NEGAÇÃO
if not soma > 10:
    print("A soma não é maior que 10")