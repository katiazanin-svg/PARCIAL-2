# Apresenta as opções de operações
print("Escolha uma operação:")
print("1- Adição")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")
# Pede para escolher a operação
operacao = input("Digite o número da operação desejada: ")
# Pede os dois números para a operação
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
# Calcula a operação conforme a escolha
if operacao == '1':
    resultado = n1 + n2
    print(f"O resultado da adição é: {resultado}")
elif operacao == '2':
    resultado = n1 - n2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == '3':
    resultado = n1 * n2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == '4':
    # Verificando a divisão por zero
    if n2 != 0:
        resultado = n1 / n2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Não é possível dividir por zero!")
else:
    print("Operação inválida!")
