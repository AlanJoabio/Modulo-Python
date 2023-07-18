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

#Tamanho da String
tamanho = len(frase);
print('O tamanho do texto é:', tamanho);
print()

#Dividindo uma String em sub strings
print("Dividindo a string: ");
palavras = fraseCompleta.split();
print(palavras);

#Substituuindo partes das string
print("Substituindo parte da string: ");
novaFrase = frase.replace("Mundo", "Python");
print(novaFrase);

#Convertendo para letras maiúscilas e minúsculas
print("Converte para Letra Minuscula e Maiuscula: ")
print("Minúsculas: ", frase.lower());
print("Maiúscula: ", frase.upper());