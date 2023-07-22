#Exemplo 1: Impressao números 1 a 10

for i in range(1, 11):
    print(i)

print()

#Exemplo 2: Impressao de frutas de uma lista de frutas

frutas1 = ['Manga', 'Morango', 'Laranja']

for fruto in frutas1:
    print(fruto);

print()

frutas = ['Banana', 'Maçã', 'Uva']

for fruta in frutas:
    print(fruta)

print()

#Exemplo 2.1
for fruta in frutas:
    if fruta == 'Maçã':
        continue;
    print(fruta);

print()

#Exemplo 2.2

for fruta in frutas:
    if (fruta == 'Maçã'):
        print('Encontrou maçã!');
        break;
    print(fruta);

print()

#Exemplo 3: Cálculo da média de uma lista de notas

notas = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

media = 0;

for nota in notas:
    media += nota;

media /= len(notas);

print(media)

print()

notas1 = [7.5, 8.0, 6.5, 9.0, 7.0];

media1 = 0;

for nota in notas1:
    media1 += nota;

media2 = media1 / len(notas1);
print("A média é: ",media2);
print()

#Exemplo 4: Contando as vogais de uma string

frase = 'Eu gosto de correr'

vogais = ['a', 'e', 'i', 'o', 'u']

for letra in frase:
    if letra in vogais:
        print(letra)

print()

palavra = 'python';
vogais1 = 0;

for letra in palavra:
    if letra in 'aeiou':
        vogais1 += 1;

print(f'A palavra {palavra} possui {vogais1} vogal');
print();

#Exemplo 5: Iteração sobre os itens de uma lista

lista = ['a','b','c','d','e'];

for indice in range(len(lista)):
    if indice == 0:
        lista[indice] = 'z';
    print(f'O elemento no índice {indice} é {lista[indice]}');

print()

#Exemplo 6: Iteração sobre os itens de uma tupla

# tupla = ['a','b','c','d','e'];

# for indice in range(len(tupla)):
#     if indice == 0:
#         tupla[indice] = 'z';
#     print(f'O elemento no índice {indice} é {tupla[indice]}');

# print()

#Exemplo 7: Iteração sobre os itens de um dicionário

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5};

for chave in dicionario:
    if chave == 'a':
        dicionario[chave] = 'z';
    print(f'O elemento no índice {chave} é {dicionario[chave]}');

print()

# Exemplo 8 : Iteração sobre um elemento numero com incremento
for numero in range(2, 11, 2):
    print(numero);

print()

# Exemplo 9 : Iteração sobre um elemento numero com decremento

for numero in range(10, 0, -1):
    print(numero);

print()

#Exemplo 10
palavra1 = 'python';
for letra in reversed(palavra1):
    print(letra);

print()

#Exemplo 11: Iteração sobre duas listas simultaneamente usando a função zip()
lista1 = [1,2,3];
lista2 = ['a','b','c'];
for elemento1, elemento2 in zip(lista1,lista2):
    print(elemento1, elemento2);

print()

#Exemplo 12: Iteração sobre duas tuplas simultaneamente usando a função zip()

tupla1 = (1,2,3);
tupla2 = ('a','b','c');
for elemento1, elemento2 in zip(tupla1,tupla2):
    print(elemento1, elemento2);

print()

#Exemplo 13: Iteração com a função enumerate para acessar índice e elemento simultaneamente
lista = ['a','b','c'];
for indice, elemento in enumerate(lista):
    print(f'O elemento no índice {indice} é {elemento}');

print()

#Exemplo 14: Iteração com a função enumerate para acessar índice e elemento simultaneamente
dicionario = {'chave':5,'valor':'abc'};

for indice, elemento in enumerate(dicionario):
    if isinstance(elemento, str) and len(elemento)>6:
        print(f'O elemento no índice {indice} é {elemento}');

print()

#Exemplo 15: Iteração sobre um dicionario para acessar chaves e valores

dicionario = {
    'chave1':'valor1',
    'chave2':'valor2',
    'chave3':'valor3'
}

for chave, valor in dicionario.items():
    print(f'A chave é {chave} e o valor é {valor}.');

print()

