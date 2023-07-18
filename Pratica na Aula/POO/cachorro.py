
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome;
        self.idade = idade;

    def latir(self):
        print(f"{self.nome} está latindo, Au Au Au, e tem {self.idade} anos!!");

#Criação de objetos da classe "Cachorro"

cachorro1 = Cachorro("Felipe", 2);
cachorro2 = Cachorro("Maria", 3);
cachorro3 = Cachorro("João", 4);

#Chamada da função "latir"

cachorro1.latir();
cachorro2.latir();
cachorro3.latir();

letras = {
    "A": r"""
        AAA        LL           AAA       NN        NN
       AAAAA       LL          AAAAA      NNNN      NN
      AAAAAAA      LL         AAAAAAA     NN NN     NN
     AA     AA     LL        AA     AA    NN   NN   NN
    AA       AA    LLLLLL   AA       AA   NN     NN NN
       
    """
    
}

nome = "Alan"

for letra in nome:
    if letra.upper() in letras:
        print(letras[letra.upper()])
    else:
        print("\n")



