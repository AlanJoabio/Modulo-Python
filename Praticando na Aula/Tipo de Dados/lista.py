#Exemplox de declaração de listas
listaNumeros = [1,2,3,4,5];
listaStrings = ["e","f","c","d"];
listaMista = [1, "a", 3.14, True];
print(listaNumeros);
print(listaStrings);
print(listaMista);

frutas = ["maça", "banana","morango"];

#Acessando a lista por indices
print(frutas[2]);

#Alterando um item especifico da lista
frutas[2] = "Uva"; 
print(frutas[2]);

#Imprimindo o tamanho da lista
print("Tamanho 1: ", len(frutas));

#Adicionando um item ao final da lista
frutas.append("abacaxi");
print(frutas); 

#Imprimindo o tamanho da lista
print("Tamanho 2: ",len(frutas),"\n");

#Acessando Sublistas
listaNova = [1,["a","b"]];
print(listaNova[1][0],"\n");

#Concatenando listas
lista1 = [1,2,3];
lista2 = [4,5,6];
listaFinal = lista1 + lista2; #concatena as duas listas e retorna uma nova lista com os itens concatenados
print (listaFinal,"\n");

#Declarando um valor repetido nas listas
listaRepetida = [0] * 4;
print(listaRepetida);

#Fatiamento de listas
lista = ['a','b','c','d'];
sublista = lista [1:4];
print(sublista);

#Adicionando um item ao final da lista
frutas = ["maça", "banana", "laranja"];
frutas.append("abacaxi");
print(frutas);

#Inserindo um item em um indíce específico da lista
frutas.insert(1, "morango");
print(frutas);
print();

#Removando um item da lista com o metodo remove
frutaRemovida = frutas.remove("banana");

#Removendo um elemento da lista pelo seu índice
frutaRemovida = frutas.pop(2);
print (frutas);
print ("Fruta removida:", frutaRemovida);

#Ordenando uma lista
frutas.sort();
print("Ordenando: ", frutas);

#Embaralhando uma lista
from random import shuffle

shuffle(frutas);
print("\nLista embaralhada: ", frutas)


