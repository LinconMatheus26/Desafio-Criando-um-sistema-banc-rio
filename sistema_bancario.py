class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.saque_diario = 0
        self.limite_saque = 500.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito realizado: R$ {valor:.2f}")
        else:
            print("Valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saque_diario < 3 and valor <= self.limite_saque:
            if valor <= self.saldo:
                self.saldo -= valor
                self.saques.append(valor)
                self.saque_diario += 1
                print(f"Saque realizado: R$ {valor:.2f}")
            else:
                print("Não foi possível sacar o dinheiro por falta de saldo.")
        else:
            print("Limite de saques diários atingido ou valor de saque excede o limite.")

    def extrato(self):
        print("=== Extrato ===")
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
            return

        if self.depositos:
            print("Depósitos:")
            for d in self.depositos:
                print(f"R$ {d:.2f}")

        if self.saques:
            print("Saques:")
            for s in self.saques:
                print(f"R$ {s:.2f}")

        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def menu(self):
        while True:
            print("\n=== Menu ===")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Extrato")
            print("4. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                valor = float(input("Informe o valor para depósito: R$ "))
                self.depositar(valor)
            elif opcao == '2':
                valor = float(input("Informe o valor para saque: R$ "))
                self.sacar(valor)
            elif opcao == '3':
                self.extrato()
            elif opcao == '4':
                print("Saindo do sistema. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Exemplo de uso
conta = ContaBancaria()
conta.menu()
