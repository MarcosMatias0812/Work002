#ATIVIDADES
#1
num01 = int(input("Digite o primeiro número: "))
num02 = int(input("Digite o segundo número: "))
num03 = int(input("Digite o terceiro número: "))

num04 = (num01 + num02)

if num04 < num03:
    print("A soma de A + B e menor que C.")

else:
    print("A soma de A + B é maior que C.")

#2
num01 =  int(input("Digite um número: "))

if num01 %2 == 0:
    print("O número é par.")
else:
    print("O número é impar.")

#3
num01 = int(input("Digite o primeiro número: "))
num02 = int(input("Digite o segundo número: "))

if num01 == num02:
    print("O resultado será: " ,(num01 + num02))

else:
    print("O resultado será: " (num01 * num02))

#4
num01 = float(input("Digite o seu número: "))

if num01 >= 0:
    print("O resultado será: " ,num01 * 2)

elif num01 <= 0:
    print("O resultado será: " ,num01 * 3)
else:
    print("Valor não encontrado.")

#5
num01 = int(input("NÚMERO: "))

if num01 %2 == 0:
    print(num01 + 5)
    print("O seu número é par.")
elif num01 %3 == 1:
    print(num01 + 8)
    print("O seu número é impar.")

#6
num01 = int(input("NÚMERO 01: "))
num02 = int(input("NÚMERO 02: "))
num03 = int(input("NÚMERO 03: "))
total = [num01, num02, num03]

total.sort(reverse=True)

print("Ordem decrescente: " ,total)

#7
sexo01 = input("Digite o seu sexo: ")
altura = float(input("Digite a sua altura: "))

if sexo01 == "masculino":
    print("O seu peso será" ,(72.7 * altura - 58), "kg")

elif sexo01 =="feminino":
    print("O seu peso será" ,(62.1 * altura - 44.7), "kg")

else:
    print("Valores não coincidem.")

#8
peso = int(input("PESO: "))
altura = float(input("ALTURA: "))
calculo01 = (peso/altura**2)

if calculo01 <= 18.5:
    print("Abaixo do peso.")

elif calculo01 >= 18.6 and calculo01 <= 25:
    print("Peso normal.")

elif calculo01 >= 26 and calculo01 <= 30:
    print("Acima do peso.")

elif calculo01 >= 31:
    print("Obeso.")

#9
preço = float(input("preço: "))
cod = int(input("Digite o código do produto de 1 a 4: "))

if cod == 1
    print()




#10
