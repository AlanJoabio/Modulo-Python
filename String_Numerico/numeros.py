#Praticando da aula sobre o tipo de dado numericos

#Operação matemática básicas
num1 = 10;
num2 = 5;

soma            = num1 + num2;
subtracao       = num1 - num2;
multiplicacao   = num1 * num2;
divisao         = num1 / num2;
resto_da_divisa = num1 % num2; #Restante da divisão, ou seja, quantos restam para completar uma divisão inteira.
potencia        = num1 ** num2;

print("Operação matemática básicas: "," \n");
print("Soma: ",soma);
print("Subtração: ", subtracao);
print("Multiplicação: ", multiplicacao);
print("Divisão: ", divisao);
print("Resto: ",resto_da_divisa);
print("Potência: ", potencia, " \n");

#Arrendodamento de número
numeroFloat = 3.14;
#float é um numero com casas decimais, ex.:
numeroArrendodado = round(numeroFloat);
print ("O arredondamento do float foi:", numeroArrendodado," \n")


#Função matématica da biblioteca math
import math

num = 4.7;
print("Funções matemáticas: ", "\n");
print("Raiz quadrada: ",math.sqrt(num), "\n"); #raiz quadrada
print("Exponencial: ",math.exp(num), "\n");    #expoente
print("Valor absoluto: ", abs(-4.7), "\n");
print("Logaritmo natural: ", math.log(num), "\n");
print("Trigonométrica (sin):", math.sin(num), "\n");
print("Trigonométrica (cos)", math.cos(num)," \n");
print("Trigonométrica (tan) :", math.tan(num), " \n");
print("Trigonométrica (atan) :", math.atan(num), " \n");
print("Arredondamento pra cima", math.ceil(num), "\n");
print("Arredondamento pra baixo",math.floor(num), "\n");

#Geração número aleatórios 
import random

aleatorio = random.randint(1,10);
print("Número gerado aletoriamente entre 1 e 10: ",aleatorio,"\n");#Conversões de tipos string = 'Python';
inteiro = int('3')
print("Inteiro convertido para tipo inteiro: ",inteiro,"\n");
real = float('8.9');
print("Real convertido para real: ",real,"\n");
booleano = bool('True');
print("Booleano convertido para booleano: ",booleano,"\n");

print("Numero float aleatória entre 0 a 1: ", random.random(),"\n")

#Formatação de números

numeroFormatado = 1234.56789;
print("Numeros formatados: ", "\n");
print(f"Número com 2 casa decimais {numeroFormatado:.2f}", "\n");
print("Número formatado com 2 casas decimais {:.2f}".format(numeroFormatado), "\n");
