# while True:
#     n1 = int(input ('Digite o 1° numero: '))
#     n2 = int(input ('Digite o 2° numero: '))
#     n3 = int(input ('Digite o 3° numero: '))
#     n4 = int(input ('Digite o 4° numero: '))
#     n5 = int(input ('Digite o 5° numero: '))
#     if n1 == 0 :
#         print ('O seu 1° numero tem 0 Por isso não podemos proceguir')
#         break
#     if n2 == 0 :
#         print ('O seu 2° numero tem 0 Por isso não podemos proceguir')
#         break
#     if n3 == 0 :
#         print ('O seu 3° numero tem 0 Por isso não podemos proceguir')
#         break
#     if n4 == 0 :
#         print ('O seu 4° numero tem 0 Por isso não podemos proceguir')
#         break
#     if n5 == 0 :
#         print ('O seu 5° numero tem 0 Por isso não podemos proceguir')
#         break
#     if n1 % 2 == 0 :
#         print ('1° numero é par ')
#     else:
#         print ('1° numero é  impar')
#     if n2 % 2 == 0 :
#         print ('2° numero é  par')
#     else:
#         print ('2° numero é  impar')
#     if n3 % 2 == 0 :
#         print ('3° numero é  par')
#     else:
#         print ('3° numero é  impar')
#     if n4 % 2 == 0 :
#         print ('4° numero é  par')
#     else:
#         print ('4° numero é  impar')
#     if n5 % 2 == 0 :
#         print ('5° numero é  par')
#     else:
#         print ('5° numero é  impar')
numeroPar = 0
while True:
    numeroPar += 1
    if numeroPar <= 5:
        N = int(input('Digite os 5 numeros: '))
        if N % 2 ==0:
            print({numeroPar})
            print('É par')
        else:
            print('É impar')
    else:
        print('Ja deu os 5 Numeros')   
        break    