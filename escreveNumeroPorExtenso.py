num = int(input('Digite um número:' ))

if(num <= 10 and num >= 0):
    if(num == 10):
        num_extenso = 'dez'
    elif(num == 9):
        num_extenso = 'nove'
    elif(num == 8):
        num_extenso = 'oito'
    elif(num == 7):
        num_extenso = 'sete'
    elif(num == 6):
        num_extenso = 'seis'
    elif(num == 5):
        num_extenso = 'cinco'
    elif(num == 4):
        num_extenso = 'quatro'
    elif(num == 3):
        num_extenso = 'três'
    elif(num == 2):
        num_extenso = 'dois'
    elif(num == 1):
        num_extenso = 'um'
    else:
        num_extenso = 'zero'

print(num_extenso)
