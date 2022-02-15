"""
Escreva um número por extenso.

"""

"""
Implementação usando num2words.

Documentação da biblioteca: https://pypi.org/project/num2words/

"""

from num2words import num2words

num = None

while(num != 'q'):
    try:
        num = input('Digite um número (ou "q" para sair): ')

        if(num == 'q'):
            break
        else:
            num = int(num)
            num_extenso = num2words(num, lang='pt-BR')

            print(num_extenso)
            print('------------------------------------')

    except ValueError:
        print('Digite apenas números! (ou "q" para sair)')
