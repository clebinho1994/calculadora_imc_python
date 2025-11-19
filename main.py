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

    match imc:
        case valor if valor < 18.5:
            print("Você está abaixo do peso\n"
                  "Situação: Magreza")
        case valor if 18.5 <= valor < 25:
            print("Você está no peso ideal\n"
                  "Situação: Saudável")
        case valor if 25 <= valor < 30:
            print("Você está com Sobrepeso\n"
                  "Situação: Atenção")
        case valor if 30 <= valor < 35:
            print("Você está com Obesidade Grau I\n"
                  "Situação: Moderado")
        case valor if 35 <= valor < 40:
            print("Você está com Obesidade Grau II\n"
                  "Situação: Severo")
        case _:
            print("Você está com Obesidade Grau II (Mórbida)\n"
                  "Situação: Muito severo")

    print("----------------------------------")

    continuar = input("Deseja calcular novamente? (s/n): ").strip().lower()
    if continuar != "s":
        print("Programa finalizado!\n"
              "----------------------------------")
        break

