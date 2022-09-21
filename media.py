nome = (input('Qual o nome do aluno: '))
nota_1 = float(input('Entre com a nota 1: '))
nota_2 = float(input('Entre com a nota 2: '))
nota_3 = float(input('Entre com a nota 3: '))

peso1 = float(input('peso nota 1: '))
peso2 = float(input('peso nota 2: '))
peso3 = float(input('peso nota 3: '))

média = (nota_1 * peso1) + (nota_2 * peso2) + (nota_3 * peso3) / peso2 + peso1 + peso3

print(média)
