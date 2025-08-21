from time import sleep
from avaliação import Avaliação
class Banco:
    Dados = []
    def __init__(self, titular, saldo, senha):
        self._titular = titular
        self._saldo = saldo
        self.__senha = senha
        self._avaliacoes = []
        Banco.Dados.append(self)
    
    def __str__(self):
        return f"Titular: {self._titular} | Saldo: {self._saldo}" 
    
    @staticmethod
    def linhas():
        print("=-"*15)
        
    def mostrar_titular(self):
            sleep(1)
            Banco.linhas()
            print(f"NOME DO TITULAR: {self._titular}")
            Banco.linhas()
            sleep(1)
            
            
    def mostrar_saldo(self):
            sleep(1)
            Banco.linhas()
            print(f"SALDO: R${self._saldo}")
            Banco.linhas()
            while True:
                decisao = str(input("Você deseja Sacar ou Depositar algum valor do seu saldo? [S/N]: ")).strip().upper()[0]
                if decisao in "S":
                    self.operacao_saldo()
                    break
                if decisao in "N":
                    break
                else:
                    print("Essa opção não é válida...")
                    
    def sacar(self):
        while True:
            valor = float(input('Digite o valor que deseja sacar: '))
            if valor <= self._saldo:
                self._saldo -= valor
                Banco.linhas()
                print(f'SALDO ATUAL: R${self._saldo}')
                Banco.linhas()
                sleep(1)
                break
            else:
                print('Não é possível sacar esse valor...')          
   
    def depositar(self):
        while True:
            valor = float(input('Digite o valor que deseja depositar: '))
            if valor > 0:
                self._saldo += valor
                Banco.linhas()
                print(f'SALDO ATUAL: R${self._saldo}')
                Banco.linhas()
                sleep(1)
                break   
            else:
                print('Não é possível depositar esse valor...')              
                    
    def operacao_saldo(self):                
            while True:
                objetivo = (input('1 - Sacar\n2 - Depositar\nDigite uma opção: '))
                try:
                    objetivo = int(objetivo)
                    if objetivo in (1,2):
                        break
                    else:
                        print('Esse valor não é válido')
                except Exception as erro:
                    print(erro.__class__)                                         
                Banco.linhas()
                sleep(1)
            if objetivo == 1:
                self.sacar()
            if objetivo == 2:
                self.depositar()    
    
    def alterar_senha(self):
        while True:
            print()
            senha = str(input('Digite a sua senha atual: '))
            print()
            if senha == self.__senha:               
                print('Senha validade com sucesso!')
                sleep(1)
                print()
                cont = 0
                senha = str(input('Digite a sua nova senha: '))
                while cont < 3:
                    print()
                    senha2 = str(input('Digite novamente para a validação: '))
                    if senha2 != senha:
                        cont +=1 
                        print('Senha digitada incorretamente...')
                    elif senha2 == senha:
                        self.__senha = senha
                        break
                if senha == self.__senha:
                    print()
                    print('Senha alterada com sucesso!')
                    break    
                if cont == 3:
                    print("Você errou sua nova senha 3 vezes, refaça todo o processo...")
                    continue        
            else:
                print("Senha incorreta...")        
        
    
    def receber_avaliacao(self):
        nome = str(input('Digite seu nome: '))
        while True:
            nota = (input('Digite uma nota de 1 a 5: '))
            try:  
              nota = int(nota)
              if 1 <= nota <= 5:
                avaliacao = Avaliação(nome, nota)
                print('Avaliação registrada')
                self._avaliacoes.append(avaliacao)
                break
              else:
               print('Opção inválida...')
            except Exception as erro:
                print(f"{erro.__class__}... Digite um número inteiro válido")   
          
            
          
            

        
        
    def mostrar_avaliaçao(self):
        if not self._avaliacoes:
            print('Nenhuma avaliação foi registrada...')
        else:
            for i in self._avaliacoes:
                print(f"Nome: {i._nome} | Nota: {i._nota}")        
        
    
    
    def vizualizacao(self):
        print('Você está na área de vizualização de informações da conta:')
        while True:
            print()
            print("1 - Ver nome do titular\n2 - Ver saldo\n3 - Ver senha / Alterar senha\n4 - Registrar avaliação\n5 - Mostrar avaliações\n6 - Sair do programa'")
            print()
            while True:
                escolha  = input('Digite a sua opção: ')
                try:
                    escolha = int(escolha)
                    if escolha in (1,2,3,4,5,6):
                        break
                    else:
                        print('Esse valor não está nas opções...')
                except Exception as erro:
                    print(erro.__class__)    
                
            if escolha == 6:
                sleep(1 )
                print('PROGRAMA FINALIZANDO...')
                sleep(1)
                break
            elif escolha == 1:
               self.mostrar_titular()
            elif escolha == 2:
                self.mostrar_saldo()
            elif escolha == 3:
                self.alterar_senha()
            elif escolha == 4:
                self.receber_avaliacao()
            elif escolha == 5:
                self.mostrar_avaliaçao()
    

