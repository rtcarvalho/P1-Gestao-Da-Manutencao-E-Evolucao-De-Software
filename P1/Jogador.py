class Jogador:

    def __init__(self, nome, pontos, score):
        self._nome = nome
        self._pontos = pontos
        self._score = score

    def setNomeJogador (self,nome):
        self._nome = nome

    def setScoreJogador(self):
        self._score += 1

    def getScoreJogador(self):
        return self._score
    
    def setPontosJogador (self,pontos):
        self._points = pontos
    
    def getNomeJogador (self):
        return self._nome

    def getPontosJogador (self):
        return self._pontos

    def getSetsJogador(self):
        return round(self._pontos/15) if round(self._pontos/15)>0 else 0   
