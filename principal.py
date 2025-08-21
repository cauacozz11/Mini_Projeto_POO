from time import sleep
class Banco:
    Dados = []
    def __init__(self, titular, saldo, senha):
        self._titular = titular
        self._saldo = saldo
        self.__senha = senha
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
                decisao = str(input("Você deseja Sacar ou Depositar algum valor do seu saldo? [S/N]")).strip().upper()[0]
                if decisao in "SN":
                    break
                else:
                    print("Essa opção não é válida...")
                    
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
            while True:      
                if objetivo == 1:
                    valor = float(input('Digite o valor que deseja sacar: '))
                    if valor < self._saldo:
                        self._saldo = self._saldo - valor
                    else:
                        print('Não é possível sacar esse valor...')                      
    
    def alterar_senha(self):
        senha = str(input('Digite a sua senha atual: '))
        if senha == self.__senha:
            senha = str(input('Digite a sua nova senha: '))
            senha2 = str(input('Digite novamente para a validação: '))
            if senha2 == senha:
                self.__senha = senha
        else:
            print("Senha incorreta...")        
        
    
    
    def vizualizacao(self):
        print('Você está na área de vizualização de informações da conta:')
        while True:
            print()
            print("1 - Ver nome do titular\n2 - Ver saldo\n3 - Ver senha / Alterar senha\n4 - Sair do programa'")
            print()
            while True:
                escolha  = input('Digite a sua opção: ')
                try:
                    escolha = int(escolha)
                    if escolha in (1,2,3,4):
                        break
                    else:
                        print('Esse valor não está nas opções...')
                except Exception as erro:
                    print(erro.__class__)    
                
            if escolha == 4:
                sleep(1 )
                print('PROGRAMA FINALIZANDO...')
                sleep(1)
                break
            elif escolha == 1:
               self.mostrar_titular()
            elif escolha == 2:
                self.mostrar_saldo()
                self.operacao_saldo()
            elif escolha == 3:
                self.alterar_senha()       
        
    

usuario1 = Banco('Marcos', 1567, "Cauaadri7006@")

   

usuario1.vizualizacao()