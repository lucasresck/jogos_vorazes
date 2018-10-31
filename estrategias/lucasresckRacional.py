# coding: utf8

from estrategias.jogadores import Jogador
import random
import math

#A ideia desse jogador é sempre caçar com mais do que a metade de pessoas, pra manter boa reputação. Porém, as caças ocorrem com quem tem alta probabilidade de caçar: jogadores com alta reputação.

class MeuJogador(Jogador):
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        reputacoes_dos_jogadores = [float(reputacao) for reputacao in reputacoes_dos_jogadores]
        if sum(reputacoes_dos_jogadores) == 0: #Primeira rodada
            escolhas = [random.choice(['c', 'd']) for x in reputacoes_dos_jogadores]
            #print(reputacoes_dos_jogadores)
            #print(escolhas)
            return escolhas
        #if len(reputacoes_dos_jogadores) == 1: #Se há só um adversário
            #return ["d"]
        #if len(reputacoes_dos_jogadores) == 2:
        #    return ["d","d"]
        elif len(reputacoes_dos_jogadores) > 10:
            sequencia = list(range(len(reputacoes_dos_jogadores)))
            reputacao_sequencia = list(zip(reputacoes_dos_jogadores, sequencia))
            reputacao_sequencia_ordenada = sorted(reputacao_sequencia, key = lambda elemento: elemento[0], reverse = 1)
            if reputacao_atual <= 0.55:
                n_de_cacadas = math.ceil(len(reputacoes_dos_jogadores) * 0.55)
            else:
                n_de_cacadas = math.floor(len(reputacoes_dos_jogadores) * 0.55)

            indices_caca = list(zip(*reputacao_sequencia_ordenada))[1][0:n_de_cacadas]

            #reputacoes_ordenadas = sorted(reputacoes_dos_jogadores, reverse = 1)
            #reputacao_limite = reputacoes_ordenadas[n_de_cacadas - 1]
            escolhas = []
            for indice in range(len(reputacoes_dos_jogadores)):
                if indice in indices_caca:
                    escolhas.append("c")
                else:
                    escolhas.append("d")

            #print(reputacao_atual)
            #print(comida_atual)
            #print(sorted(reputacoes_dos_jogadores))
            #print(escolhas)
            #print("\n")

            return escolhas
        
        else:
            escolhas = ['d' for x in reputacoes_dos_jogadores]
            return escolhas