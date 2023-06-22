"""
fruta = 'banana';

print (fruta);
"""
"""
nome = "Alan" ;
sobrenome = "Joabio";

print (nome, sobrenome);
"""

frase = "Olá Mundo!!"
#Declarando uma string
print("String original");
print(frase);
print();


#Acessando caracteres individuais
print ("Acessando caracteres individuais: ");
print ("Primeiro caractere: ", frase[0]);
print ("Ultimo caracter: ", frase[-1]);

#Utilizando o input para pegar um nome informado pelo usuário
nome = input("Nome: ");
print (nome);
print();

#Inserindo as variáveis no print com f
sobreNome = input("Sobrenome: ");
print(f"Bem-vindo, {nome} {sobreNome}");
print("Bem-vindo, {} {}".format(nome, sobreNome));

#Concatenando strings
print("Concatenação de Strings: ");
outroFrase = "Bem-vindo";
fraseCompleta = frase + ' ' + outroFrase;
print(fraseCompleta);
print()


