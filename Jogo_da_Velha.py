# -*- coding: utf-8 -*-
"""
JOGO DA VELHA
Created on Mar 05 2020
@repo: https://gist.github.com/reisarthur/5b1132590b174374de48a4fd116e67f4
@author: reisarthur e bernardo
"""

Njogos = 10000            # Número de jogos a serem jogados em sequência
jogadores = [False,False] # True para jogador humano, falso para jogador computador
import random
import matplotlib.pyplot as plt

# Função imprime um tabuleiro de jogo da velha; A variável 't' é uma lista com 9 elementos (de 0 a 8)
def mostraTabuleiro(t):
    if jogadores[0] or jogadores[1]:
        print()
        print('',t[0],'|',t[1],'|',t[2])
        print('',t[3],'|',t[4],'|',t[5])
        print('',t[6],'|',t[7],'|',t[8])

# Essa função atualiza o tabuleiro: recebe o tabuleiro antigo, o número do jogador, e a posição que ele escolheu; e retorna com o tabuleiro novo
def atualizaTabuleiro(t, j, p):
    if   j==1: t[p] = 'X'          
    elif j==2: t[p] = 'O'
    else: t[p] = 'E'
    mostraTabuleiro(t)
    return t

# Essa função troca a vez do jogador: Se o última a jogar foi o 2, agora é a vez do 1, e vice-versa
def trocaVez(j):
    if   j==1: return 2
    elif j==2: return 1
    else:      return 'ERRO'

# Essa função recebe o tabuleiro, e confere se houve vencedor. Retorna 3 em caso de empate (todas as posições preenchidas)
def confereVencedor(t):
    venc = ''
    if t[0]==t[1] and t[0]==t[2] and t[0]!=' ': venc = t[0]
    if t[3]==t[4] and t[3]==t[5] and t[3]!=' ': venc = t[3]
    if t[6]==t[7] and t[6]==t[8] and t[6]!=' ': venc = t[6]
    if t[0]==t[3] and t[0]==t[6] and t[0]!=' ': venc = t[0]
    if t[1]==t[4] and t[1]==t[7] and t[1]!=' ': venc = t[1]
    if t[2]==t[5] and t[2]==t[8] and t[2]!=' ': venc = t[2]
    if t[0]==t[4] and t[0]==t[8] and t[0]!=' ': venc = t[0]
    if t[2]==t[4] and t[2]==t[6] and t[2]!=' ': venc = t[2]
    if venc=='X': 
        if jogadores[0] or jogadores[1]: print('Jogador 1 venceu o jogo!')
        return 1
    elif venc=='O':
        if jogadores[0] or jogadores[1]: print('Jogador 2 venceu o jogo!')
        return 2
    if not ' ' in t: 
        if jogadores[0] or jogadores[1]: print('Empate!')
        return 3
    return 0

# Essa função transforma um caracter 'r' em uma posição de 0 a 8 (no caso, os números na posição do numpad)
def posicaoTabuleiro(r):
    if   r=='7': return 0
    elif r=='8': return 1
    elif r=='9': return 2
    elif r=='4': return 3
    elif r=='5': return 4
    elif r=='6': return 5
    elif r=='1': return 6
    elif r=='2': return 7
    elif r=='3': return 8
    else: return -1

# Confere se posição ainda não está ocupada
def conferePosicao(t, p):
    if t[p]==' ': return p
    else:         return -1

# Faz a jogada. Se for jogador, pede por input. Se for computador, sorteia aleatoriamente de 1 a 9
def jogada(j):
    if (j==1 and not jogadores[0]) or (j==2 and not jogadores[1]):
        return random.choice(['1','2','3','4','5','6','7','8','9'])
    else:
        return input('Jogador ' + str(j) + ', escolha uma posição:')

resultados = [0,0,0]
for i in range(Njogos):
    jogador = 1
    tabuleiro = [' ']*9
    mostraTabuleiro(tabuleiro)
    while True:
        while True:
            resposta = jogada(jogador)
            posicao  = posicaoTabuleiro(resposta)
            posicao  = conferePosicao(tabuleiro, posicao)
            if posicao>=0: break
        tabuleiro = atualizaTabuleiro(tabuleiro, jogador, posicao)
        jogador   = trocaVez(jogador)
        vencedor  = confereVencedor(tabuleiro)
        if vencedor>0: break
    resultados[vencedor-1] += 1

plt.pie(resultados, labels=['Jogador 1', 'Jogador 2', 'Empate'], autopct='%1.1f%%')