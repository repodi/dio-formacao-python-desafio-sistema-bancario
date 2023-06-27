menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

opcao = ""
while True:
    print(menu)
    opcao = input()
    if opcao == "d":
        print("Depósito")
        valor_deposito = float(input("Informe o valor a depositar: "))
        saldo += valor_deposito
        linha_extrato = f" +R$ {valor_deposito:.2f}"
        extrato += linha_extrato
    elif opcao == "s":
        print("Saque")
        if numero_saques < LIMITE_SAQUES :
            valor_saque = float(input("Informe o valor do saque: "))
            if valor_saque <= limite and saldo >= valor_saque :
                numero_saques += 1
                saldo -= valor_saque
                linha_extrato = f" -R$ {valor_saque:.2f}"
                extrato += linha_extrato
            else: 
                print("Saldo insuficiente ou ultrapassou o limite de saque diário de R$ 500")
        else:
            print("Número limite de saques diários alcançados, tente novamente amanhã.")
    elif opcao == "e":
        print("Extrato")
        if (extrato) : 
             print(f"Saldo: {saldo:.2f}")
             print(extrato)
        else: 
            print("Não foram realizadas movimentações")
    elif opcao == "q":
        break;
    else: 
        print("Operação inválida, por favor selecione uma opção novamente a operação desejada.")
print("Obrigado por utilizar nosso banco!")
    

