'''Saque, deposito e extrato'''


opcao = -1
saldo = 500.0
deposito = 0.0
controle_de_saque = 0
extrato_1 = 0
extrato_saque = list()
extrato_deposito = list()


while opcao != 0:

    print('''-------------------- BANCO FICTÍCIO --------------------
          
                [1] SAQUE
                [2] DEPÓSITO
                [3] EXTRATO
                
                
                [0] SAIR DA CONTA
--------------------------------------------------------          
    ''')
    opcao = int(input('Qual procedimento gostaria de realizar: '))

    # saque
    if opcao == 1:

        if controle_de_saque >= 3: # 3 saques por dia
            print('\n\nVocê não pode realizar essa operação. O limite de saques diários é de 3 vezes\n')
        else:
            saque = float(input('\n\nQual valor gostaria de retirar: '))
            if saque > saldo: # não saca valor acima do saldo
                print('\nNão foi possível realizar o saque. Você não possui saldo!')
            elif saque > 500: # valor máximo de saque por vez
                print('\nO valor máximo que pode ser sacado por vez é de R$ 500.0')
            elif saque < 0:
                print('Valor não existe. Tente novamente!')
            else: 
                controle_de_saque += 1
                saldo -= saque
                extrato_saque.append(saque)
                print(f'Valor retirado de R$ {saque}\n\n')
                #print(f'{extrato_saque}')

    elif opcao == 2:

        deposito = int(input('\n\nQual valor gostaria de depositar: '))
        if deposito < 0:
            print('\n\nValor incorreto. Tente de novamente!')
        else:
            saldo += deposito
            extrato_deposito.append(deposito)

    elif opcao == 3:

        print('''-------------------- EXTRATO DA CONTA --------------------
            
                    [1] EXTRATO DO SAQUE
                    [2] EXTRATO DO DEPÓSITO
                    [3] EXTRATO COMPLETO
                    
    --------------------------------------------------------          
    ''')
        extrato_1 = int(input('Qual procedimento do extrato gostaria de realizar: '))


        if extrato_1 == 1:
            print(f'\nSeus saques do dia foram: R${extrato_saque}\n')
            print(f'\n\nSeu saldo atualmente é de: R$ {saldo}\n')

        elif extrato_1 == 2:
            print(f'\nSeus depositos do dia foram: R${extrato_deposito}\n')
            print(f'\n\nSeu saldo atualmente é de: R$ {saldo}\n')

        elif extrato_1 == 3:
            if len(extrato_saque) == 0 and len(extrato_deposito) == 0:
                print('\n\nNenhuma movimentação\n\n')
            else:
                print('------------ Este é seu extrato completo! ------------')
                print(f'\n\nSeus saques do dia foram: R${extrato_saque}\n\ne seus depositos do dia foram: R${extrato_deposito}')
                print(f'\nSeu saldo atualmente é de: R$ {saldo}\n')
                print('------------------------------------------------------')
        else:
            print('\n\nValor incorreto. Tente novamente!\n')
        
    elif opcao == 0:
            exit('-------------- OBRIGADA E VOLTE SEMPRE! --------------')
    
    else:
        print('ERRO! ESSA OPÇÃO NÃO EXISTE. TENTE NOVAMENTE!')