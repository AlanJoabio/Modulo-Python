#Exercicio da aula 03/07

#1)
numero1 = int(input("Digite o primeiro número: "));
numero2 = int(input("Digite o segundo número: "));

soma = numero1 + numero2 ;
subtracao = numero1 - numero2;
multiplicacao = numero1 * numero2;
divisao = numero1 / numero2 ;

print("Soma: ",soma);
print("Subtração: ",subtracao);
print("Multiplicação: ", multiplicacao );
print("Divisão: ", divisao );

#2)
temperatura = float(input("Digite a temperatura em graus Celsius: "));

if temperatura > 100:
    print("A água está fervendo!");

#3)
numero = int(input("Digite um número interiro: "));

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


#4)
senha = input("Digite a senha: ");

if senha == "123456":
    print("Senha correta!")
else:
    print("Senha incorreta! Tente novamente...");


#5)
idade = int(input("Qual a sua idade? "));

if idade >= 18 and idade <=30:
    print ("A idade está entre 18 a 30 anos.");

else:
    print ("A idade não está entre 18 a 30 anos.")


#6)
numero01 = int(input("Digite o primeiro número: "));
numero02 = int(input("Digite o segundo número: "));
numero03 = int(input("Digite o terceiro número: "));

if numero01 > 0 or numero02 > 0 or numero03 > 0:
    print("Pelo menos um dos número é positivo.")
else:
    print("Nenhum dos números é positivos>")
