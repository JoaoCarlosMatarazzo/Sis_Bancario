menu = """

[D] Deposito
[S] Sacar
[E] Extrato
[Q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    option = input(menu)
    if option == "d":
        valor = float(input("Informe o valor do deposito:"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}/n "
        else:
            print("Operação falha! Valor inválido.")

    elif option == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor < saldo
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor de saque excedeu o limite.")
        elif excedeu_saldo:
            print("Operação Falhou! Número máximo de saques excedido.")
        else:
            print("Operação falhou! O valor informado é invalido.")

    elif option == "e":
        print("\n================Extrato================")
        print("Não foram realizadas movimentação." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif option == "q":
        print ("Obrigado pela preferências")
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada')

