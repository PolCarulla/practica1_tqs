from enum import Enum
  
    
class MasterMindModel:
    AVAILABLE_COLORS = ["Red", "Green", "Blue", "Yellow","Orange","Purple"]
    MAX_TURN = 6
    
    def __init__(self,code):
        self.validateSecretCode(code)
        self.secretCode = code
        self.turn = 0
        self.gameEnded = False

    def validateSecretCode(self,code:list):
        for color in code:
            if color not in self.AVAILABLE_COLORS:
                raise ValueError(f"Invalid color in secret code: {color}. Available colors: {self.AVAILABLE_COLORS}")
            
    def checkGuess(self,guess):
        pass