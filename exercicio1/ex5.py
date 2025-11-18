numero_camisas = int(input('Quantidade de camisas: '))
valor_camisa = 12.5
valor_total = numero_camisas * valor_camisa
if numero_camisas <= 5:
    valor_total = valor_total * 0.97
else:
    if numero_camisas <= 10:
        valor_total = valor_total * 0.95
    else:
        valor_total = valor_total * 0.93
print(f'Valor total da compra: R$ {valor_total:.2f}')