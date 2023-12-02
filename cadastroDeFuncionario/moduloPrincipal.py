
import sys
import os 
diretorio_atual = os.path.abspath(os.path.dirname(__file__))
sys.path.append(diretorio_atual)
from moduloClasse import Funcionario
funcionarios = []

def main():
    while True:
            print('Plataforma do colaborador')
            print('1)cadastrar colaborador')
            print('2)Consultar colaborador')
            print('3)Retirar o colaborador')
            print('4)listar colaboradores')
            print('5)Encerrar programa')
            print(f'{len(funcionarios)}')
            try:
                opc = int(input('Entre com a opição desejada: '))
                if opc not in [1,2,3,4,5]:
                    print('Somente permitido os números da opição do menu ')
                if opc == 1:
                    cadastro()
                if opc == 2:
                    consultar()
                    
            except ValueError:
                print('O valor inserido não é permitido, entre somente com as opições do painel')
def cadastro():
    print('Bem vindo ao cadastro de funcionarios ')
    while True:
        nome = str(input('Entre com o nome do funcionario: '))
        idade = int(input('Entre com a idade: '))
        sexo = str(input('Entre com o sexo do funcionario (M/F): ')).upper()
        while sexo not in 'MF':
            print('Somente permitido sexo MASCULINO ou FEMININO. Tente Novamente!')
            sexo = str(input('Entre com o sexo do funcionario (M/F): ')).upper()
            
        if sexo == 'M':
            print('Sexo Masculino')
        elif sexo == 'F':
            print('Sexo Feminino')
        funcao = str(input('Entre com a função do funcionario: '))
        salario = float(input('Entre com o salario do funcionario: '))
        atividade = str(input('Funcionario esta ativo na empresa')).upper()
        while atividade not in 'SN':
            print('Entre somente com valores SIM ou NÃO')
            atividade = str(input('Funcionario esta ativo na empresa')).upper()
            
        if atividade == 'S':
            print('Funcionario ja esta trabalhando')
            atividade = True
        elif atividade == 'N':
            print('Funcionario ainda não inicio na empresa')
            atividade = False
        data = int(input('Entre com a data de admissão (DD-MM-YYYY): '))
        
            
        try:
            Ofuncionario = Funcionario(nome,idade,sexo,funcao,salario,atividade, data)
        
       
            funcionarios.append(Ofuncionario)
            print('Funcionario Adicionado com sucesso')
            
        except:
            print('Funcionario não cadastrado ')
        Ofuncionario.infosfuncionario()   
        continuar = str(input('Deseja cadastrar outro colaborador[SIM/NÃO]?: ')).upper()
        while continuar not in  'SIMNÃO':
            print('Entre somente com SIM ou Não')
            continuar = str(input('Deseja cadastrar outro colaborador[SIM/NÃO]?: ')).upper()
        if continuar == 'SIM':
            cadastro()
        elif continuar == 'NÃO':
            main()
            
def consultar():
    while True:
        print('1)consultar por nome')
        print('2)Consultar por id')
        print('3)Listar colaboradores')
        print('4)Retornar ao menu')
        try:
            opc = int(input('Entre com o a opição desejada: ')) 
            while opc not in [1,2,3,4]:
                print('Entre somente com opições disponiveis no menu. Tente Novamente!')
                opc = int(input('Entre com o a opição desejada: ')) 
            if opc == 1:
                try:
                    nome = str(input('Entre com o nome do colaborador: '))
                    funcionarios(nome).infosfuncionario()
                except:
                    print('O funcionario não foi econtrado no sistema')
            elif opc == 2:
                try:
                    id = int(input('Entre com o id do fucionario: '))
                    funcionarios[id].infosfuncionario()
                except:
                    print('O funcionario não foi econtrado no sistema')
            elif opc == 3:
                p = 0
                for colaborador in funcionarios:
                    p += 1
                    print(p + colaborador)
            elif opc == 4:
                main()
        except ValueError:
            print('Insira somente valos que estão disponeiveis no menu. Tente Novamente!')
            
                        
if __name__ == '__main__':
    main()
    Funcionario()