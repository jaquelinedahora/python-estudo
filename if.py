print("********************")
print("Calculo das Notas:")
print("********************")

nota_1 = str(input("Nota 1: "))
if (nota_1 < 0 or nota_1 > 10):
     print("insira uma nota entre 0 a 10")


nota_2 = str(input("Nota 2: "))
if (nota_2 < 0 or nota_2 > 10):
     print("insira uma nota entre 0 a 10")


soma_notas = (nota_1 + nota_2) / 2

if (soma_notas >=5) and (soma_notas <=10):
    print("\n Aprovado")
if (soma_notas <=0) and (soma_notas >=10):
    print("insira uma nota entre 0 a 10")
if (soma_notas <=5):
    print("\n Reprovado")

print("********************")
print("Dados inválidos, reinicie a operação!")
print("********************")