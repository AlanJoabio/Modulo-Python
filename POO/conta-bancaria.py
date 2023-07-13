
class Conta:
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero;
        self.titular = titular;
        self.saldo = saldo;

    def depositar(self, valor):
        self.saldo += valor;

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor;
        else:
            print("saldo insuficiente");

    def extrato(self):
        print(f"Numero: {self.numero}\nTitular: {self.titular}\nSaldo: {self.saldo}");

#Criação de uma conta e realização de operações

conta1 = Conta(1234, "Alan");
conta1.depositar(100);
conta1.sacar(35);
conta1.extrato();