
from random import randint



class Funcionario:
    funcionarios = []

    nomeFuncionario = ''
    idadeFuncionario = 0
    sexoFuncionario = ''
    funcaoFuncionario = ''
    dataAdmissao = 0
    salarioFuncionario = 0
    ligadoFuncinario = False
    
    
    def __init__(self,nomeFuncionario, idadeFuncionario,sexoFuncionario, funcaoFuncionario, salararioFuncionario,ligadoFuncionario,dataAdmissao):
        self.nomeFuncionario = nomeFuncionario
        self.idadeFuncionario = idadeFuncionario
        self.sexoFuncionario = sexoFuncionario
        self.funcaoFuncionario = funcaoFuncionario
        self.salarioFuncionario = salararioFuncionario
        self.ligadoFuncinario = ligadoFuncionario
        self.dataAdmissao = dataAdmissao
        self.idFuncionario = randint(1,999)
       
    def desligado(self):
        if self.ligadoFuncinario == False:
            print('Funcionario desligado')
    def ligado(self):
        if self.ligadoFuncinario == True:
            print('Funcionario ativo na empresa')
    def tostring(self):
        print('Informações sobres os funcionarios')
        print(f'Nome do Funcionario.......{self.nomeFuncionario}')
        print(f'Idade do Funcionario......{self.idadeFuncionario}')
        print(f'Sexo do Funcionario.......{self.sexoFuncionario}')
        print(f'Data de Admissão..........{self.dataAdmissao}')
        print(f'Salario Funcionario.......{self.salarioFuncionario} ')
        print(f'Id do Funcionario.........{self.idFuncionario}')
        print(f'Funcionario Ativo.........{"Sim" if self.ligadoFuncinario == True else "Não" }') 
    def __str__(self):
        return f'{self.nomeFuncionario}', f'{self.idFuncionario}'
        



