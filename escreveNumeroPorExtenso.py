"""
Escreva um número por extenso.

"""

"""
Implementação usando num2words.

Documentação da biblioteca: https://pypi.org/project/num2words/

"""

from num2words import num2words

while(True):
    num = int(input('Digite um número: '))

    num_extenso = num2words(num, lang='pt-BR')

    print(num_extenso)
    print('-------------------')
