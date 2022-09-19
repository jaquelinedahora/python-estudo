altura = float(input())
largura = float(input())
num_parede = float(input())

total_m2_obra = altura*largura*num_parede

valor_tinta = 20
valor_metro_tinta = valor_tinta/5

valor_hora = 30
valor_hora_pintada = valor_hora/10

hora_trabalho = valor_hora*total_m2_obra
horastrabalhadas_hora = total_m2_obra / 10


custos_tinta = total_m2_obra * valor_metro_tinta
custo_mao_obra = horastrabalhadas_hora * valor_hora

print(custos_tinta + custo_mao_obra)


