dias_esquecidos = 0  # Variável para armazenar a quantidade de dias de matéria esquecidos
materia_estudada = 0  # Variável para armazenar a quantidade de matéria estudada

while True:  # Loop principal do jogo
    escolha = input("Escolha sua ação: (1 - Jogar videogame, 2 - Estudar, 3 - Beber cerveja): ")

    if escolha == "1":
        dias_esquecidos += 1
        materia_estudada *= 3
    elif escolha == "2":
        materia_estudada += 1
    elif escolha == "3":
        dias_esquecidos += 1
    else:
        print("Escolha inválida. Digite um número válido.")

    if dias_esquecidos >= 3:
        print("Você esqueceu muitos dias de matéria. Reprovado!")
        break

print("\n--- Resultado Final ---")
print("Matéria estudada:", materia_estudada)

if materia_estudada >= 10:
    print("Parabéns! Você estudou o suficiente para passar em Cálculo!")
else:
    print("Você não estudou o suficiente para passar em Cálculo.")
