# -*- coding: utf-8 -*-
"""casetecnicoQ1: DataSprints-HL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FCFDnfi56IcTpt0ptW1ib2xH5I9DX-of

Pergunta da Questão: 

"1 - Desenvolva um script em python para retornar o primeiro valor não repetido de uma string.

Exemplo:

input -> 'teste'

output -> 's'

input -> 'engenharia de dados'

output -> 'g'"

# **Construção da Resposta**
"""

frase = input("Digite uma frase: ")

print(frase)

"""No caso, iremos criar duas novas listas, uma para transformar a string em lista e uma outra para adicionar as letras que só aparecem uma vez na lista criada. 

Dessa forma, poderemos usar as propriedades das listas e tornar a questão mais facil de ser resolvida.
"""

lista_add = []
indice = []

for i in range(len(frase)):
  lista_add.append(frase[i])

for j in range(len(frase)):
  if (lista_add.count(frase[j]) == 1):
    indice.append(frase[j])

print(indice[0])

print(indice) #caso seja necessario analisar a lista "indice"
print("\nO primeiro valor não repetido é:", indice[0]) #para demonstrar melhor

"""Então, basicamente, a lista "indice" retorna as letras (ou valores) que só apareceram uma vez na frase digitada.

Portanto, como ela é adicionada em ordem, então a primeira letra na lista "indice" será a primeira(o) letra/valor não repetida.
"""