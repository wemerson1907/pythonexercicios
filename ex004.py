# Escreva um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações possiveis sobre ele.

algo = input('digite algo: ')

print(f'É do tipo: {type(algo)}, '
      f'É alfanumerico? {algo.isalnum()}, '
      f'É numerico? {algo.isnumeric()}, '
      f'É alfabetico? {algo.isalpha()}, '
      f'É maiusculo? {algo.isupper()}, '
      f'É minusculo? {algo.islower()},'
      f'É somente espaços? {algo.isspace()}, '
      f'Esta capitalizada? {algo.istitle()}') # quando a primeira letra esta maiuscula ex: Python
