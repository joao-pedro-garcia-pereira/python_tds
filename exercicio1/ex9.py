import getpass 
import os
tentativa = 0
nome = input ("qual seu nome: ")
senha =  getpass.getpass ("Digite sua senha: ")
escolha = 0

saldo = 0


while True:
    if escolha == 4:
        break
    tentativa += 1
    if tentativa <= 3:
        senha2 = getpass.getpass ("Digite sua senha: ")
        if senha2 == senha:
            while True:
                print(f'Olá  {nome}')
                escolha = int(input('Numero 1 (deposito)/n Numero 2 (saque)/n Numero 3 (extrato)/n Numero 4 (sair)'))
                if escolha == 1:
                    os.system('cls')
                    print('Quanto deseja depositar? ')
                    deposito = int(input('Digite o valor que será depositado:'))
                    saldo += deposito
                if escolha == 2:
                    os.system('cls')
                    print('Quanto deseja sacar? ')
                    saque = int(input('Digite o valor que ira sacar: '))
                    saldo -= saque
                if escolha == 3:
                    os.system('cls')
                    print('Extrato ')
                    print(f'Seu saldo atual é de: {saldo}')
                if escolha == 4:
                    os.system('cls')
                    break
            
        else: 

            if tentativa == 1:
                os.system('cls')
                print('Só tem mais duas tentativas')
            if tentativa == 2:
                os.system('cls')
                print('Só tem mais uma tentativas')
                
            
    else:
        os.system('cls')
        print('Muitas tentativas acesso bloqueado⚠️')
        break


  
