# meuDicionario = {
#     'nome' : 'Alan',
#     'sobrenome' : 'Joabio',
#     'anos' : 33
# }

# print(meuDicionario);

# frutaDicionario = {
#     'maçã'   : 3,
#     'banana' : 6,
#     'uva'    : 8,
# };

# print("Significado encontrado no dicionário: ", frutaDicionario['maçã']);
# print();

# frutaDicionario["maçã"] = 5;
# frutaDicionario["laranja"] = 10;

# print("Nova quantidade de maça: ", frutaDicionario["maçã"]);
# print();
# print(frutaDicionario)


# animaisDicionario = {};
# animaisDicionario["cachorro"] = "Melissa";
# print(animaisDicionario);


# aluno = {
#     'nome' : 'Alan Joanio' ,
#     'idade': 33 ,
#     'hobbies' : ['jogar csgo','esportes']
# }

# print(aluno);

frutaDicionario = {
    'maça'   : 3,
    'banana' : 6,
    'uva'    : 8,
    'laranja': 10
};

print();
print("Quantidade de maçãs: ", frutaDicionario.get("maçã"));
print("Quantidade de bananas: ", frutaDicionario.get("banana"));

print("Quantidade de morangos: ", frutaDicionario.get("morangos","Não foi encontrado a definição de morangos"));
print();

elementoRemovido = frutaDicionario.pop("laranja");

print(elementoRemovido);
print();
print("Dicionário atualizado: ", frutaDicionario)

frutaDicionario = {
    'maçã'   : 3,
    'banana' : 6,
    'uva'    : 8,
    'laranja': 10
};

print();
print("Chaves encontradas no dicionário: ", frutaDicionario.keys());
print("Valores encontrados no dicionário: ",frutaDicionario.values());
print(frutaDicionario.items());
