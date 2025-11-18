horas = float(input("Quantas horas assistidas por semana?"))
valor_mensal = float(input("Qual o valor o mensal??"))

conta1 = horas * 4
conta2 = valor_mensal / conta1

print(f"o valor por hora é de {conta2:.2f}horas")