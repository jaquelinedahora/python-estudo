# Somatório: Lê 10 números inteiros e soma todos eles

soma=0
for i in range(10):
    valor = int(input("Valor: "))

soma = soma+valor
print("Total= ",soma)
# Somatório: Lê 3 números float e acumula todos eles

soma = 0.0
for i in range(3):
    print("Valor[",i,"] = ",end='')
valor = float(input())
soma=soma+valor
print("Total = ",soma)