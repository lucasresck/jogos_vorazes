# coding: utf8

from estrategias.jogadores import Jogador

class MeuJogador(Jogador):
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = ['d' for x in reputacoes_dos_jogadores]
        return escolhas