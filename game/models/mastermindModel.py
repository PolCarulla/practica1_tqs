
class MasterMindModel:
    AVAILABLE_COLORS = ["Red", "Green", "Blue", "Yellow","Orange","Purple"]
    MAX_TURN = 6
    def __init__(self,code=None,available_colors=None):
        if available_colors != None:
            self.AVAILABLE_COLORS = available_colors
        
        if code != None:
            self.validateSecretCode(code)
        self.secretCode = code

        self.turn = 0
        self.gameEnded = False

    def validateSecretCode(self,code:list):
        if len(code) != 4:
            raise IndexError(f"Invalid lenght of secret code. Expected 4 and got {len(code)}")
        for color in code:
            if color not in self.AVAILABLE_COLORS:
                raise ValueError(f"Invalid color in secret code: {color}. Available colors: {self.AVAILABLE_COLORS}")
        
            
    def checkGuess(self,guess):
        result = []
        for index,element in enumerate(guess):
            result.append(self.secretCode[index] == element)
        
        return result