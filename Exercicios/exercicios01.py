#1) Criar seu nome e a idade
nome = input('Qual é o seu nome? ');
print (nome);

idade = input('Qual é a sua idade? ');
print(idade);
print("Olá meu nome é {}".format(nome), "e a","Minha idade é {}".format(idade), "anos", "\n");
"\n"
#2) Comprimento da frase
frase = 'Eu gosto de programação';
print ('O comprimento do texto é: ', len(frase), "\n");

#3) Criar nome e sobrenome
nome = input("Qual é o seu nome? ");
print(nome);

sobreNome = input("Qual é o seu sobrenome? ");
print(sobreNome);

nome_completo = nome + ' ' + sobreNome;
print ("Seu nome completo é:", nome_completo, "\n");

#4) Criar frase com metodo upper maiúsculas
frase = 'Meu time é Palmeiras!';
print(frase.upper(), "\n");

#5) Criar uma frase e dividir usando split
print("Dividino as palavras: ")
frase = nome_completo.split();
print(frase,"\n");

#6) criar um variavel e usar o metodo replace()
texto = "Eu tenho 8 anos";
novaFrase = texto.replace("8","33");
print(novaFrase, "\n");

#7)Criar variaveis numeros e atribuir valores e mostra o resultados
num1 = 10;
num2 = 5;
resultado = (num1 + num2);
print("Resultado do valor é ",resultado, "\n");


#8 Extra: Solicitar ao usuario digitar os valores 
num3 = int(input("Digite um numero: "));
num4 = int(input("Digite segundo numero: "), "\n");
multi = num3 * num4;
print("Resultado é ",multi);
print("O resultado entre {} e {} é igual a {} ".format(num3,num4,multi), "\n");

#Extra
numero1 = int(input("Digite um número: "));
numero2 =int(input("Digite um número: "), "\n");
soma          = numero1+numero2;
subtracao     = numero1-numero2;
multiplicacao = numero1*numero2;
divisao       = numero1/numero2;
resto         = numero1%numero2;
print("A soma entre {} e {} vale {} ".format(numero1,numero2,soma), "\n");
print("A subtração entre {} e {} vale {} ".format(numero1,numero2,subtracao), "\n");
print("A multiplicaçao entre {} e {} vale {} ".format(numero1,numero2,multiplicacao), "\n");
print("A divisão entre {} e {} vale {} ".format(numero1,numero2,divisao), "\n");
print("O resto da divisão de {} por {} é {}".format(numero1,numero2,resto), "\n");

