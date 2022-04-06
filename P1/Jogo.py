from .Jogador import Jogador

class Jogo:

    def __init__(self, score, jogadorOne, jogadorTwo):
        self._jogador = Jogador 
        self._jogadorOne = Jogador 
        self._jogadorTwo = Jogador 
        self._score = score

    def score(self):
        self.getAdvantageWinner()
        self.getjogadorWithTheMostPoints()
        self.getjogadorWithTheMostSets()
        

    def getScoreName(self):
    
        switch(self._jogador.getjogadorSets()){
            case 2:
                return "Fifteen"
            case 3:
                return "Thirthy"
            case 4:
                return "All"
            default:
                return "Love"
        }

    def getjogadorWithTheMostPoints(self):
        return self._jogadorOne if self._jogadorOne.getjogadorPoints()>self._jogadorTwo.getjogadorPoints() else self._jogadorTwo

    def getjogadorWithTheMostSets(self):
        return self._jogadorOne if self._jogadorOne.getjogadorSets()>self._jogadorTwo.getjogadorSets() else self._jogadorTwo

    def getAdvantageWinner(self):
        return "Vantagem" + self.getjogadorWithTheMostSets if self._jogador.getjogadorSets()>=4 else "Não é o vencedor"

    def getWinner(self):
        return "Vitória para " + self.getjogadorWithTheMostSets()
