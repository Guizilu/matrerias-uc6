# Precisamos converter para float (numero com vírgula)
salario_atual = float(input("Digite seu salario atual: "))

# Calculando o imposto e a gratificação
# 1 - 0.1 = 90% ou 0.9
salario_final = salario_atual * 0.9 + 50

print("O seu salário liquido será: ", salario_final)


