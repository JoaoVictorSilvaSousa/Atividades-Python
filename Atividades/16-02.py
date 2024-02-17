# Atividade 1 Python

#1
print ("Olá Mundo")

#2

x = float(input ("Digite um número:"))
print("\n")
print("O Número Informado foi:", x)

#3

x = float(input ("Digite um número:"))
print("\n")
y = float(input ("Digite o segundo número:"))

soma = x+y
print("\n")
print("A soma foi:",soma)

#4

w = float(input ("Digite a primeira nota:"))
print("\n")
x = float(input ("Digite a segunda nota:"))
print("\n")
y = float(input ("Digite a terceira nota:"))
print("\n")
z = float(input ("Digite a quarta nota:"))

soma = w+x+y+z

media = soma/4
print("\n")
print("Sua media foi:",media)

#5

x = float(input ("Digite uma distância em metros:"))

convers = x*100
print("\n")
print("Sua distância em centimetros é de:", convers,"cm")

#6

x = float(input ("Digite o raio do circulo:"))

r = x**2

a = r*3.14
print("\n")
print("A área do círculo é:",a)

#7

x = float(input ("Digite o valor de um dos lados:"))

a = x**2
d = a*2
print("\n")
print("O dobro da área do seu quadrado é:",d)

#8

x = float(input ("Digite o valor ganho por hora:"))
print("\n")
y = float(input ("Digite o número de horas trabalhadas no mês:"))
print("\n")
sal = x*y

print("Salario total do referido Mês:",sal)

#9

x = float(input ("Digite a temperatura em graus Fahrenheit:"))

y = x-32
z= y/1.8
print("\n")
print("Em graus Celsius são:", z,"Graus")

#10

x = float(input ("Digite a temperatura em graus Celsius:"))

y = x*1.8
z = y+32
print("\n")
print("Temperatura em Fahrenheit:",z, "Graus")
print("Temperatura em Celsius:",x, "Graus")

#11

w = int(input ("Digite o primeiro número inteiro:"))
print("\n")
x = int(input ("Digite o segundo número inteiro:"))
print("\n")
y = float(input ("Digite um número real:"))
print("\n")
print("Resultados:")
print("\n")
dob = w*2
met = x/2
prod = dob*met

trip = w*3
som = trip+y

cub = y**3

print("O produto do dobro do primeiro com metade do segundo é:",prod)
print("\n")
print("A soma do triplo do primeiro com o terceiro é:",som)
print("\n")
print("O terceiro elevado ao cubo é:",cub)

#12

x = float(input ("Digite uma altura:"))

p1 = x*72.7
p2 = p1-58
print("\n")
print("O peso ideal para uma pessoa com essa altura deve ser de:",p2)

#13

x = float(input ("Digite uma altura:"))
y = input ("Seu sexo é masculino[M] ou feminino[F]?:")

p1 = x*72.7
pmasc = p1-58

p2 = x*62.1
pfem= p2-44.7

print("\n")
if y == "M":
  print("Seu peso ideal deve ser de:", pmasc, "Kg")
elif y == "F":
  print("Seu peso ideal deve ser de:", pfem,"Kg" )
else:
  print("Desconheço seu peso ideal")

#14

x = float(input ("Digite o peso dos peixes:"))

y = x-50
multa = y*4

print("\n")

if x<= 50:
  print("O peso de peixes está dentro do regulamento")
elif x > 50:
  print("Peso está acima do limite permitido pela regulamentação, excedendo",y, "Kg, terá que ser pago uma multa no valor de: R$",multa)

#Atividade 2 Python

#1 Faça um programa que imforme a versão python que você está utilizando
  
print("\t ----Versão do Python----")
import sys
print(sys.version)

#2 Faça um programa em linguagem Python que converta metros para centímetros.

print("\t ----Conversão de medida----")
m = float(input("Insira uma distância em metros:"))
c = m*100
print("Sua distância em cm é:", c)

#3 Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.

print("\t ----Tabuada até 10----")

x=int(input("Digite um número:"))

x1 = x*1
x2 = x*2
x3 = x*3
x4 = x*4
x5 = x*5
x6 = x*6
x7 = x*7
x8 = x*8
x9 = x*9
x10 = x*10


print("Tabuada do número:",x)
print("O valor da multiplicação do seu número por 1 é:",x1)
print("O valor da multiplicação do seu número por 2 é:", x2)
print("O valor da multiplicação do seu número por 3 é:", x3)
print("O valor da multiplicação do seu número por 4 é:", x4)
print("O valor da multiplicação do seu número por 5 é:", x5)
print("O valor da multiplicação do seu número por 6 é:", x6)
print("O valor da multiplicação do seu número por 7 é:", x7)
print("O valor da multiplicação do seu número por 8 é:", x8)
print("O valor da multiplicação do seu número por 9 é:", x9)
print("O valor da multiplicação do seu número por 10 é:",x10)

#4 Faça um algoritmo em linguagem Python que receba duas notas e calcule a média aritmética e mostre o resultado.

print("\t ----Média Aritimética----")
x = float(input("Digite a primeira nota:"))
y = float(input("Digite a segunda nota:"))
med = (x+y)/2
print("Sua média aritimética das notas foi:", med)

#5 Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor do novo salário reajustado de acordo com a tabela abaixo:

#Salario Atual\Reajuste
#<500         \15%
#>=500 e <=1000\10%
#>1000          \5%

print("\t ----Reajuste Salarial----")
sal = float(input("Digite seu salario antes do reajuste:"))
if sal <500:
  print("Seu salario após o reajuste é:", (sal*0.15)+sal)
elif sal >= 500 <= 1000:
  print("Seu salario após o reajuste é:",  (sal*0.10)+sal)
elif sal > 1000:
  print("Seu salario após o reajuste é:", (sal*0.05)+sal)

#6 Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis por 7, mas não são múltiplos de 5. Os números obtidos devem ser impressos em sequência.

print("\t ----Números não multiplos de 5 divisiveis por 7----")
n = []
for i in range (5,101):
  if i % 7 ==0 and i % 5 != 0:
    n.append(i)
    print(n)

#7 Faça um programa que receba um número digitado pelo usuário e calcule a soma de todos os números de 1 até ao número digitado. Por exemplo, se o usuário digitou o número 4, a saída deve ser 10 (1+2+3+4=10).
    
print("\t ----Soma de todos os números até o digitado---")
soma = 0
x = int(input("Digite um número:"))
for i in range(1,x+1):
  soma += i
print("A Soma é =",soma)

#8 Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro.

print("\t ----Neutro, Negativo e Positivo---")

x = int(input("Digite um valor inteiro:"))
if x>=1:
  print("Seu número é positivo")
elif x<0:
  print('Seu número é negativo')
else:
  print("Seu número é neutro")

#9 Crie um algoritmo que receba um número, conte o número total de dígitos e mostre o resultado. Por exemplo, se o número é 2021 , então a saída deve ser 40

print("\t ----Contagem de Digitos---")
digitos = int(input("Digite um número para contar seus dÍgitos:"))
contador = 0
while digitos !=0:
  digitos //= 10
  contador += 1
print("Total de digitos =", contador)

#10 Faça um programa em linguagem Python, que lê um número n e imprime os n primeiros números da sequência de Fibonacci.

print("\t ----Sequência de Fibonacci---")
termos = int(input("Digite a quantidade de termos para calcular:"))
#começando com 0 e 1
num1, num2 = 0, 1
contador = 0
while contador < termos:
  num3= num1 + num2
  # Atualizando valores
  num1=num2
  num2=num3
  contador += 1
  print (num1)

#11 Analise o código Python a seguir.
x = [11,12,13,14,15]
print(x[-1])

#Atividade 3 Python


#1 questão
#Digamos que você tenha um dicionario com preços, se você rodar o comando "For" item "in" "preços" e "printar (item)"Qual será o resultado? String ou númerico

print("\t ----Lista de preços----")
n = {"carrinho": 10, "bola": 20, "Boneca":15}

for item in n:
 print(item) #R:String

#2 Questão
#Como fazer para transformar o número 1500 em formato de moeda, de forma correta em python, para enviar em um texto? número = 1500
 
print("\t ----Transformando valor em Moeda----")

numero = 1500
numero = f"R${numero:,.2f}"
print(numero)

#3 Questão
#Nessa questão temos a variável vendas recebendo o valor de, 5000.

#O codigo diz que:

#Se (if) as vendas forem maiores que 1000, print "Parabéns, bateu a 1º meta"
#Se(elif) as vendas forem maiores que 3000, print "Parabéns, bateu a 2º meta, bonus de R$200 para o vendedor"
#Se (elif) as vendas forem maiores que, 4500, print "Parabéns, bateu a 3º meta, bonus de R$ 500 para o vendedor"

print("\t ----Vendas----")

vendas = 5000

if vendas > 1000:
    print("Parabéns, bateu a 1ª meta")
elif vendas > 3000:
    print("Parabéns, bateu a 2ª meta, bônus de R$200 para o vendedor")
elif vendas > 4500:
    print("Parabéns, bateu a 3ª meta, bônus de R$500 para o vendedor")

#4 Questão
#Neste exercicio temos uma pegadinha, temos umna lista com o iphone, ipad, notebook e vamos criar uma lista que recebe a lista anterior e acrescenta o (append) o airpod

print("\t ----Lista de Aparelhos Apple----")
lista = ["iphone", "ipad", "notebook"]
list = lista
list.append("airpod")
print(list)