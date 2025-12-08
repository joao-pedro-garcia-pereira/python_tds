while True:
    n1 = int(input ('Informe o primeiro número: '))
    n2 = int(input ('Informe o segundo número: '))
    if n1 == 0 or n2 == 0 :
        print ('Média não pode ser realizada. Pois um dos valores é 0')
        break
    print(f"{(n1 + n2) / 2:.1f}")