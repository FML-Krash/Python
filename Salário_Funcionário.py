class Funcionario:
    def __init__(self, nome, cargo, valor_por_hora):
        self.nome = nome
        self.cargo = cargo
        self.valor_por_hora = valor_por_hora
        self.__salario = 0
        self.__horas_trabalhadas = 0

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        raise ValueError("Impossivel alterar salario diretamente. Use a funcao calcula_salario().")

    def registar_horas(self):
        while True:
            try:
                self.__horas_trabalhadas = (int(input("Quantas horas Trabalhou: ")))
                break
            except:
                linha()
                print("\nHoras Trabalhadas deve um valor Inteiro.\n")
                linha()

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_por_hora
        print("Funcionario:\nNome: {}\nCargo: {}\nSalario: {}".format(Funcionario_1.nome, Funcionario_1.cargo, Funcionario_1.__salario))


def linha():
    print("#=========================================#")


linha()
while True:
    try:
        Funcionario_1 = Funcionario((input("Qual o Nome do Funcionario: ")), (input("Qual o Cargo: ")), (int(input("O Valor por hora de Trabalho: "))))
        break
    except:
        linha()
        print("\nIntroduza um Numero Inteiro no Valor por hora de Trabalho.\n")
        linha()

Funcionario_1.registar_horas()
linha()
Funcionario_1.calcula_salario()
linha()
