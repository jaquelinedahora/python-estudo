dias_esquecidos = 0  # Variável para armazenar a quantidade de dias de matéria esquecidos
materia_estudada = 0  # Armazena a quantidade de matéria estudada
energia = 10  # Variável para armazenar a energia em dias do jogador, a quantidade de dias é escolhido conforme necessidade

while True:  # Loop do jogo
    print("Escolha sua ação:")
    print("1. Jogar videogame")
    print("2. Estudar")
    print("3. Beber cerveja")

    escolha = input("Digite o que deseja fazer hoje: ")  # Solicita ao jogador que digite o comando

    if escolha == "1":
        energia -= 1  # Reduz a energia em 1
        dias_esquecidos += 1  # Acrescenta a quantidade de dias de matéria esquecidos
        materia_estudada *= 3  # Multiplica a quantidade de matéria estudada por 3
        print("Você escolheu jogar videogame. Esqueceu a materia que estudou ontem, só que hoje voce vai absorveu 3x mais matéria.")
    elif escolha == "2":
        energia -= 1  # Reduz a energia em 1
        materia_estudada += 1  # acrescenta a quantidade de matéria estudada em 1
        print("Você escolheu estudar. Que bom, absorveu mais matéria.")
    elif escolha == "3":
        energia -= 1  # Reduz a energia em 1
        dias_esquecidos += 1  # acrescenta a quantidade de dias de matéria esquecidos
        print("Você escolheu beber cerveja. Bebeu muito e o esqueceu a ultima materia estudada.")
    else:
        print("Não tem essa opção, digite uma ação valida.")

    if energia <= 0:
        print("Sua energia acabou. Você está cansado demais para estudar, melhor descansar um pouco.")
        break  # Para o loop do while se a energia for menor que zero

    elif dias_esquecidos >= 3:
        print("Você esqueceu muitos dias de matéria, Cuidado para não ter Anmesia. REPROVADO!")
        break  # Sai do loop do while se a quantidade de dias de matéria esquecidos for maior ou igual a três

if materia_estudada >= 10:
    print("Parabéns! Você estudou o bastante esses dias e passou na materia UHUUULLL !!")
