# String: Lista de Letras

nome= input("insira seu nome: ")

for letra in nome:
    print(letra)
        
print("\nFIM\n")

input("> Pressione <enter> para continuar...")

lista = []
for letra in nome:
    lista.append(letra)

# Exibe a lista de caracteres

print("Lista: ", lista)
        
for i in range(len(nome)):
    print(lista[i],end='')
    
print("\n")

# Obtem o código do caracter

cod=ord(lista[0])
print("Lista[0]: ",lista[0]," Código: ",cod)

# Soma 1 ao código do caracter

lista[0] = chr ( ord(lista[0])+1 )
cod=ord(lista[0])
print("Lista[0]: ",lista[0]," Código: ",cod)

