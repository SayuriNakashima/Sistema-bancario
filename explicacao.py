# Menu de opções que será mostrado para o usuário a cada interação
menu  = """

[1]Depositar
[2]Sacar
[3]Extrato
[4]Sair

=>"""

# Inicializa o saldo da conta com 0
saldo = 0
# Limite máximo permitido para cada saque
limite = 500
# String para armazenar o histórico das operações (extrato)
extrato = ""
# Contador para o número de saques realizados
numero_saque = 0
# Limite máximo de saques permitidos por dia
LIMITE_SAQUES = 3

# Loop infinito para manter o sistema funcionando até o usuário optar por sair
while True:
    # Solicita que o usuário escolha uma opção do menu
    opcao = input(menu)

    # Caso o usuário escolha a opção 1 - Depositar
    if opcao == "1":
        # Pede para o usuário informar o valor do depósito
        valor = float(input("Digite o valor do depósito:"))

        # Verifica se o valor informado é maior que zero (depósito válido)
        if valor > 0:
            saldo += valor  # Adiciona o valor ao saldo
            # Registra o depósito no extrato com formatação em reais e duas casas decimais
            extrato += f"Depósito : R$ {valor:.2f}\n"
        else:
            # Se o valor for zero ou negativo, avisa que a operação falhou
            print("Operação falhou! O valor informado é inválido.")

    # Caso o usuário escolha a opção 2 - Sacar
    elif opcao == "2":
        # Pede para o usuário informar o valor do saque
        valor = float(input("Digite o valor do saque:"))

        # Verifica se o valor do saque é maior que o saldo disponível
        excedeu_saldo = valor > saldo
        # Verifica se o valor do saque ultrapassa o limite máximo por saque
        excedeu_limite = valor > limite
        # Verifica se o número de saques já atingiu o limite permitido
        excedeu_saques = numero_saque >= LIMITE_SAQUES
        
        # Se não tem saldo suficiente
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        # Se ultrapassou o limite por saque
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        # Se ultrapassou o limite de saques diários
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        # Se o valor do saque é válido (positivo) e não excedeu nenhuma regra
        elif valor > 0:
            saldo -= valor  # Deduz o valor do saldo
            # Registra o saque no extrato
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1  # Incrementa o contador de saques feitos
        else:
            # Caso o valor informado seja inválido (zero ou negativo)
            print("Operação falhou! O valor informado é inválido.")
    
    # Caso o usuário escolha a opção 3 - Mostrar extrato
    elif opcao == "3":
        print("\n========= EXTRATO ========")
        # Se não houver movimentações, informa que nada foi realizado
        print("Não foram realizadas movimentações." if not extrato else extrato)
        # Mostra o saldo atual formatado
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================")
    
    # Caso o usuário escolha a opção 4 - Sair do sistema
    elif opcao == "4":
        break  # Sai do loop e finaliza o programa

    else:
        # Caso o usuário digite uma opção inválida (não está no menu)
        print("Operação inválida, por favor selecione novamente a operação desejada")
