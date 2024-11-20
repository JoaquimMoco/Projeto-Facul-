# Variável de controle para o loop
saida = ''

# Funções de cálculo
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por 0"
    return a / b

def calculadora(num1, num2, operacao):
    resultado = None
    if operacao in ['+', 'soma']:
        resultado = adicao(num1, num2)
    elif operacao in ['-', 'subtracao', 'subtração']:
        resultado = subtracao(num1, num2)
    elif operacao in ['*', 'multiplicacao', 'multiplicação']:
        resultado = multiplicacao(num1, num2)
    elif operacao in ['/', 'divisao', 'divisão']:
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação não reconhecida"
    return resultado

# Loop principal
while saida.lower() != 'n':
    try:
        # Solicitando os números ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, / ou o nome dela): ").lower()
        
        # Chamando a função calculadora
        resultado = calculadora(num1, num2, operacao)
        print(f"Resultado da operação: {resultado}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
    
    # Perguntando se o usuário quer continuar
    saida = input("Deseja continuar? (S/N): ").strip()
    if saida.lower() == 'n':
        print("Obrigado por usar a calculadora!")

