#Calculadora IMC em Python
print("----------------------------------")
print("Calculadora IMC")
while True:
    print("----------------------------------")
    peso = float(input("Digite o seu peso: "))
    print("----------------------------------")
    altura = float(input("Digite sua altura: "))
    print("----------------------------------")

    imc = float(peso / (altura ** 2))
    print(f"Seu indice de massa corporal é: {round(imc, 2)}")


    if imc < 18.5:
        print("Você está abaixo do peso\n"
              "Situação: Magreza")
    elif imc > 18.5 and imc < 25:
        print("Você está no peso ideal\n"
              "Situação: Saudável")
    elif imc > 25 and imc < 30:
        print("Você está com Sobrepeso\n"
              "Situação: Atenção")
    elif imc > 30 and imc < 35:
        print("Você está com Obesidade Grau I\n"
              "Situação: Moderado")
    elif imc > 35 and imc < 40:
        print("Você está com Obesidade Grau II\n"
              "Situação: Severo")
    else:
        print("Você está com Obesidade Grau II (Mórbida)\n"
              "Situação: Muito severo")

    print("----------------------------------")

    continuar = input("Deseja calcular novamente? (s/n): ").strip().lower()
    if continuar != "s":
        print("Programa finalizado!\n"
              "----------------------------------")
        break

