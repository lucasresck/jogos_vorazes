__author__ = 'fccoelho'

from jogadores import Jogador
import random

class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = ['c'  for x in reputacoes_dos_jogadores]
        return escolhas


