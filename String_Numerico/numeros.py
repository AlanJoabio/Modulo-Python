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

print("Operação matemática básicas: ");
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
