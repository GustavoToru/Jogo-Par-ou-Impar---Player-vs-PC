# -*- coding: utf-8 -*-
"""Jogo: Par ou Ímpar - Player X PC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vvQxECKriGEbELKFvvJ5u_k6AOK7NDVG
"""

print("~Jogo Par ou Ímpar~")
jogador1 = input('-> Digite o nome do jogador:')
jogador2 = (f'Computador')
print(f'{jogador1}, você vai jogar contra o {jogador2}')

primeiro_jogador = jogador1
segundo_jogador = (f'Computador')

if primeiro_jogador == "1":
  primeiro_jogador = jogador1
  segundo_jogador = jogador2
elif primeiro_jogador == "2":
  primeiro_jogador = jogador2
  segundo_jogador = jogador1

print(f'// {primeiro_jogador}, digite 0 para escolhar PAR ou 1 para escolher ÍMPAR')
escolha = input(f'-> {primeiro_jogador}, Você quer par ou ímpar?')
escolha2 = None

if escolha == 'ímpar' or escolha == 'impar' or escolha == '1':
 escolha  = 'ímpar'
 escolha2 = 'par'
elif escolha == 'par' or escolha == '0':
  escolha = 'par'
  escolha2 = 'ímpar'

print(f'//{primeiro_jogador}, você ficou com {escolha} e o {segundo_jogador} ficou com {escolha2}.')

from random import randint

numero1 = int(input(f'-> {primeiro_jogador}, escolha um número:'))
numero2 = randint(0,10)

print(f'{primeiro_jogador} escolheu o número {numero1}. Já o {segundo_jogador} escolheu o número {numero2}.')

soma = numero1 + numero2

if soma % 2 == 0:
  vencedor = 'par'
else:
  vencedor = 'ímpar'

if vencedor == escolha:
  print(f'// {primeiro_jogador} VENCEU!')
else:
  print(f'{segundo_jogador} VENCEU!')

