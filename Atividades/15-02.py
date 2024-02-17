#1 Escreva um programa que pergunte a velocidade do carro de um usuário e diga se este foi ou não multado.

print("\t ----Multa----")

max = int(input("Digite o limite de velocidade: "))

velo = float(input("Informe a velocidade do carro: "))

if velo <= max:
  print("Você está dentro do limite de velocidade")
elif velo > max:
  print("Você recebeu uma multa de R$950,00")
else:
  print("Error 404")




#2 Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário

print("\t ----Km percorridos----")

km = float(input("Digite quilometragem deslocada por seu carro alugado: "))

print('A quilometragem deslocada foi:',km)



print("\t ----Multa----")


#3 Faça um programa que diga a média de um aluno em 3 trimestres sendo a média = 6.

notax = float(input("Digite a primeira nota: "))
notay = float(input("Digite a segunda nota: "))
notaz = float(input("Digite a terceira nota: "))

media = (notax+notay+notaz)/3

if media >= 6:
  print("Passou de ano com média", media)
elif media == 4:
  print('O aluno está de recuperação')
elif media < 4:
  print('Aluno não passou de ano')
else:
  print('Inválido')



#4 Faça um programa que exiba seu nome, sobrenome e último nome na tela.

print("\t ----Nome----")

nome = "João Victor"
Sobrenome = "Da Silva"
last_name = "De Sousa"

print("Nome completo",nome,Sobrenome,last_name)




#5 Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

print("\t ----Metros em milímetros----")

x = float(input ("Digite uma distância em metros:"))

convers = x*1000
print("\n")
print("Sua distância em milímetros é de:", convers,"mm")




#6 Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar

print("\t ----operação com dois números----")

x = float(input("Insira o primeiro número: "))
print("Seu primeiro número é:", x)
y = float(input("Insira o segundo número: "))
print("Seu segundo número é:",y)

operacao = input("Qual operação você deseja realizar (soma, subtração, divisão, multiplicação, potenciação)? ")

if operacao == "soma":
  resultado = x + y
elif operacao == "subtração":
  resultado = x - y
elif operacao == "divisão":
  resultado = x / y
elif operacao == "multiplicação":
  resultado = x * y
elif operacao == "potenciação":
  resultado = x ** y
else:
  print("Inválido!")

print("Resultado =", resultado)