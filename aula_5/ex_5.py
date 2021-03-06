
class ContaBancaria:

    def __init__(self, cliente):
        self.saldo = 0.0
        self.rendimento = 1.01
        self.cliente = cliente

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor

    def render(self):
        self.saldo *= self.rendimento

class ContaCorrente(ContaBancaria):
    
    def __init__(self, cliente):
        super().__init__(cliente)
        self.rendimento = 1.10
    
class ContaDaVo(ContaBancaria):

    def __init__(self, cliente):
        super().__init__(cliente)
        self.rendimento = 1.50
    
    def depositar(self, valor):
        super().depositar(valor + 0.15)
    
    def sacar(self, valor):
        if valor > 10.0:
            super().depositar(10.0)
        super().sacar(valor)
        
def simular(conta_bancaria):
    conta_bancaria.depositar(100.00)
    for i in range(12):
        conta_bancaria.render()
    conta_bancaria.sacar(110.00)
    print(conta_bancaria.saldo)

conta_bancaria = ContaBancaria('Lucas')
simular(conta_bancaria)

conta_corrente = ContaCorrente('Lucas')
simular(conta_corrente)

conta_da_vo = ContaDaVo('Lucas')
simular(conta_da_vo)
