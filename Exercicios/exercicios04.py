#1
num = 1
while num <= 10:
    print(num);
    num += 1

#2
for num in range(1, 11):
    print(num);

#3
num = 1
soma = 0
while num <= 100:
    soma += num
    num += 1

print("A soma dos números de 1 a 100 é:", soma);

#4
soma = 0
for num in range(1, 101):
    soma += num

print("A soma dos números de 1 a 100 é:", soma);

#5
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num);
    num += 1

#6
for num in range(2, 21, 2):
    print(num);

#7
string = input("Digite uma string: ");
inversa = ""
indice = len(string) - 1

while indice >= 0:
    inversa += string[indice]
    indice -= 1

print("String invertida:", inversa);

#8
palavra = input("Digite uma palavra: ");
palindromo = True

for i in range(len(palavra)):
    if palavra[i] != palavra[-i - 1]:
        palindromo = False
        break

if palindromo:
    print("A palavra é um palíndromo.");
else:
    print("A palavra não é um palíndromo.");


#9
numero = 1

while numero**2 <= 1000:
    numero += 1

print("O menor número cujo quadrado é maior do que 1000 é:", numero);

#10
lista = [1, 2, 3, 4, 5]
tamanho = len(lista);

for i in range(tamanho - 1, -1, -1):
    print(lista[i]);



