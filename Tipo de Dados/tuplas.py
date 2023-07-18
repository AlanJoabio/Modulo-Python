tupla1 = (1,2,3,4,5);
tupla2 = ("a","b","c");
tupla3 = (1, "Hello", True);
tupla4 = 1,2,3,4;
#tupla5 = ["a","b","c"]
print(tupla1)
print(tupla2)

print(type(tupla3));
print(type(tupla4));

#Acessando itens individualmente em tuplas
print("A tupla é: ", tupla2[1]);

#Exemplo de uma forma errada de acessar um item da tupla
print(tupla2[2]);
print(tupla2[0]);

#Conceito principal de tuplas; "Imutável!!"
#tupla5 [1] = "d";
#print(tupla5 [1]);

#Fatiamento de itens na tupla
print(tupla1[1:4]);

#Concatenando Tuplas
tupla5 = 1,2,3;
tupla6 = 4,5,6;
tupla7 = tupla5 + tupla6; #concatena as duas tuplas
print(tupla7);

#Criando variaveis novas com os calores de uma tupla
a, b, c = tupla6;
a = tupla6[0];

print()
print("Valores das variáveis: ")
print(a);
print(b);
print(c);