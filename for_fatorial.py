# Fatorial: Lê um números e calcula o fatorial
x=int(input("Valor: "))
if x >= 0:
    f=1.0
for i in range(x,1,-1):
    f=f*i

print("Fatorial de ",x," = ",f)