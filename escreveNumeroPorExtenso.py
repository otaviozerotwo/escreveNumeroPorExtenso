"""
Escreva um número por extenso.

"""

""" Implementação usando if else."""

# num = int(input('Digite um número: '))

# if(num <= 10 and num >= 0):
#     if(num == 10):
#         num_extenso = 'dez'
#     elif(num == 9):
#         num_extenso = 'nove'
#     elif(num == 8):
#         num_extenso = 'oito'
#     elif(num == 7):
#         num_extenso = 'sete'
#     elif(num == 6):
#         num_extenso = 'seis'
#     elif(num == 5):
#         num_extenso = 'cinco'
#     elif(num == 4):
#         num_extenso = 'quatro'
#     elif(num == 3):
#         num_extenso = 'três'
#     elif(num == 2):
#         num_extenso = 'dois'
#     elif(num == 1):
#         num_extenso = 'um'
#     else:
#         num_extenso = 'zero'
# print(num_extenso)

"""Implementação usando um dicionário."""

dict_numeros = {
    'zero': 0,
    'um': 1,
    'dois': 2,
    'três': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
    'sete': 7,
    'oito': 8,
    'nove': 9,
    'dez': 10
}

num_extenso = None

while(num_extenso == None):
    num = int(input('Digite um número: '))
    if(num >= 0 and num <= 10):
        for chave, valor in dict_numeros.items():
            if(num == valor):
                num_extenso = chave
    else:
        print('Número inválido!')

print(num_extenso)
