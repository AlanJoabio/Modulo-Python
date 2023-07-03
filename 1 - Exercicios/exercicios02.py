#Atividade passada do dia 28/06

frutas = ["maçã","banana","laranja","abacaxi","melancia"];

#1)
print(frutas);
print()

#2)
frutas.append("Uva");
print(frutas, "\n");

#3)
frutas.remove("banana")
print(frutas);

#4)
frutas_selecionada = frutas[2];
print("\nFruta selecionada foi: ", frutas_selecionada);

#5)
cores = ("vermelho","azul","verde","amarelo","roxo");
print("\nCores disponíveis:", cores,"\n");

#6)
core_selecionada = cores[2];
print("Cores selecionada é ",cores[0]);
print("Segunda cor selecionada é ", core_selecionada,"\n");

#7)
# O erro ocorre porque as tuplas são imutáveis, ou seja, não podem ser modificadas após a sua criação. Para funcionar tirar o parêntese, trocar por colchetes, que vai vira lista.
#cores.append("laranja"); 
#print("A nova cor adicionada é", cores)

#8)
aluno = {
    "nome" : "Alan Joabio",
    "idade":  90,
    "cidade" : "Salvador-Ba"
}

print(aluno,"\n")

#9)
print("A idade do aluno é ", aluno["idade"],"anos \n");
print(f"A idade do aluno tem {aluno['idade']} anos. \n")
print(f"{aluno['nome']} tem {aluno['idade']} anos e mora em {aluno['cidade']} \n");

#10) 
aluno["gênero"] = "Masculino";
print(aluno,"\n");

#11 
aluno.pop("cidade");
print("Dicionário do aluno atualizada são ", aluno,"\n");
#ou usando o metodo del (aluno["cidade"]); #ou del aluno["cidade"]; print(aluno,"\n");