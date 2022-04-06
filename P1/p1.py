# -*- coding: utf-8 -*-
class Game:
    def __init__(self, NomePlayer1, NomePlayer2):
        self.NomePlayer1 = NomePlayer1
        self.NomePlayer2 = NomePlayer2
        self.pontosp1 = 0
        self.pontosp2 = 0
        
    def won_point(self, NomePlayer):
        if NomePlayer == self.NomePlayer1:
            self.P1Score()
        else:
            self.P2Score()
    
    def score(self):
        resultado = ""
        if (self.pontosp1 == self.pontosp2 and self.pontosp1 < 3):
            if (self.pontosp1==0):
                resultado = "Love"
            if (self.pontosp1==1):
                resultado = "Fifteen"
            if (self.pontosp1==2):
                resultado = "Thirty"
            resultado += "-All"
        if (self.pontosp1==self.pontosp2 and self.pontosp1>2):
            resultado = "Deuce"
        
        P1res = ""
        P2res = ""
        if (self.pontosp1 > 0 and self.pontosp2==0):
            if (self.pontosp1==1):
                P1res = "Fifteen"
            if (self.pontosp1==2):
                P1res = "Thirty"
            if (self.pontosp1==3):
                P1res = "Forty"
            
            P2res = "Love"
            resultado = P1res + "-" + P2res
        if (self.pontosp2 > 0 and self.pontosp1==0):
            if (self.pontosp2==1):
                P2res = "Fifteen"
            if (self.pontosp2==2):
                P2res = "Thirty"
            if (self.pontosp2==3):
                P2res = "Forty"
            
            P1res = "Love"
            resultado = P1res + "-" + P2res
        
        
        if (self.pontosp1>self.pontosp2 and self.pontosp1 < 4):
            if (self.pontosp1==2):
                P1res="Thirty"
            if (self.pontosp1==3):
                P1res="Forty"
            if (self.pontosp2==1):
                P2res="Fifteen"
            if (self.pontosp2==2):
                P2res="Thirty"
            resultado = P1res + "-" + P2res
        if (self.pontosp2>self.pontosp1 and self.pontosp2 < 4):
            if (self.pontosp2==2):
                P2res="Thirty"
            if (self.pontosp2==3):
                P2res="Forty"
            if (self.pontosp1==1):
                P1res="Fifteen"
            if (self.pontosp1==2):
                P1res="Thirty"
            resultado = P1res + "-" + P2res
        
        if (self.pontosp1 > self.pontosp2 and self.pontosp2 >= 3):
            resultado = "Advantage " + self.NomePlayer1
        
        if (self.pontosp2 > self.pontosp1 and self.pontosp1 >= 3):
            resultado = "Advantage " + self.NomePlayer2
        
        if (self.pontosp1>=4 and self.pontosp2>=0 and (self.pontosp1-self.pontosp2)>=2):
            resultado = "Win for " + self.NomePlayer1
        if (self.pontosp2>=4 and self.pontosp1>=0 and (self.pontosp2-self.pontosp1)>=2):
            resultado = "Win for " + self.NomePlayer2
        return resultado
    
    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()
    
    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()
    
    def P1Score(self):
        self.pontosp1 +=1
    
    
    def P2Score(self):
        self.pontosp2 +=1