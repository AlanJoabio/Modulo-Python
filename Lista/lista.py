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

#