import locale
from datetime import date

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

dia = date.today().strftime("%A").lower()

print("=== CINEMA ===")
print("D039 - O Poderoso Chefão")
print("B678 - Matrix")
print("D889 - O Senhor dos Anéis")
print("M912 - Interestelar")
print("G007 - O Resgate do Soldado Ryan")

codigo = input("Código do filme: ")

if codigo == "D039":
    filme = "O Poderoso Chefão"
elif codigo == "B678":
    filme = "Matrix"
elif codigo == "D889":
    filme = "O Senhor dos Anéis"
elif codigo == "M912":
    filme = "Interestelar"
elif codigo == "G007":
    filme = "O Resgate do Soldado Ryan"
else:
    print("Código inválido!")
    exit()

if dia == "segunda-feira" or dia == "quarta-feira" or dia == "sexta-feira":
    ingresso = 32.50
else:
    ingresso = 36.00

qtd = int(input("Quantidade de ingressos: "))
total = qtd * ingresso

print("\n1 - Combo 005 - Doritos + Refri Lata (15.90)")
print("2 - Combo 072 - Pipoca Salgada + Copo de Coca Cola (17.90)")
print("3 - Combo 777 - Pipoca Doce + Copo de Suco (14.90)")
print("4 - Combo 215 -  Refil de Pipoca Salgada + 2 Recargas de Refri (25.90)")
print("0 - Nenhum")

combo = int(input("Escolha: "))

if combo == 1:
    total += 15.90
elif combo == 2:
    total += 17.90
elif combo == 3:
    total += 14.90
elif combo == 4:
    total += 25.90

print("\n===== RESUMO =====")
print("Filme:", filme)
print("Dia:", dia)
print("Total: R$ {:.2f}".format(total))