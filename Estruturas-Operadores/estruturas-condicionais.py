"""
Estruturas Condicionais
"""

# #Verificação de idade para entrada em clube noturno
# idade = int(input("Digite sua idade: "));

# if idade >= 18:
#     print ("Você pode entrar no club Noturno!!");
# else:
#     print ("Infelizmente você não tem permissão para entrar.");
# print();

# #Verificar se um numero está dentro de um intervalo entre 10 e 20
# numero = 21;

# if (numero >= 10) and (numero <= 30):
#     print ("O número", numero, "está dentro do intervalor [10-20]");
# else:
#     print ("O número", numero, "não está dentro do intervalor [10-20].");
# print();

#Comparar o tamanho de duas listas
# lista1 = [1,2,3,4,5];
# lista2 = [5,4,3,2,'a'];

# if len(lista1) >= len(lista2):
#     print ('A primeira lista é maior que a segunda.');
# elif len(lista2) >= len(lista1):
#     print('A segunda lista é maior que a primeira.') ;
# else :
#     print('As listas são iguais');

#Verificação de acesso um sistema
# senha = input("Digite sua senha: ");

# senha_correta = "123456";
# if senha == senha_correta:
#     print("Bem vindo ao Sistema!");
# else:
#     print("Senha incorreta. Tente novamente.");

#Verificação de acesso um sistema com login e senha
usuario = input("Digite o seu usuário: ");
senha   = input("Digite sua senha: ");
usuario_correto = "admin";
senha_correta    ="123456";
# if usuario==usuario_correto and senha==senha_correta:
#     print("Login efetuado com sucesso!");
# else:
#     print("Usuário ou Senha inválidos.");
# print();
if(usuario != usuario_correto and senha != senha_correta):
    print("Usuário e senha incorretos!");
elif usuario != usuario_correto:
    print("Usuario Incorreto! Verifique os dados digitados.");
elif not (senha == senha_correta):
    print("Senha Inválida!");
else:
    print("Login Efetuado Com Sucesso!");

