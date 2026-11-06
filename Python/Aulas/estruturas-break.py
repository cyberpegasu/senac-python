# # contador = 1

# # while contador <= 10:
# #     if contador == 3:
# #         contador += 1
# #         continue

# #         contador == 7:
# #         break

# #         print(f"contador {contador}")
# #     contador += 1


# print("usando somente numero final")
# for numero in range(5):
#     print(f"numero {numero}")

# print("usando numero inicial e numero final")
# for numero in range(1, 5):
#     print(f"numero {numero}")

# print("usando numero inicial, final e incremental")
# sequencia = range(0, 11, 2)
# for numero in sequencia:
#     print(f"numero {numero}")

# print("usando numero inicial, final e incremental - contador negativo")
# sequencia = range(10, -1, -1)
# for numero in sequencia:
#     print(f"numero {numero}")



# nome = "Vitor"
for letra in "Vitor":
    print(f"letra {letra}")

    frutas = ["Maçã", "Banana", "Mamão"]

for fruta in frutas:
    print(f"fruta {fruta}")

print("usando enumerate e start")
for indice, fruta in enumerate(frutas, start=1):
    print(f"indice {indice}: {fruta}")

print("usando enumerate")
for indice, fruta in enumerate(frutas):
    print(f"indice {indice}: {fruta}")