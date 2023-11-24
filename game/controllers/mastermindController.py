from enum import Enum

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    CRAZY = 4

class MasterMindController:
    model = None
    view = None
    difficulty = Difficulty.EASY
    def setView(self,view):
        self.view = view
    
    def setModel(self,model):
        self.model = model
        
    def start_menu(self):
        while True:
            self.view.displayMenu(self.difficulty)
            user_input = self.view.userInput()
            if user_input == "start_game":
                self.run_game()
            elif user_input == "exit":
                break
            elif user_input == "difficulty_up":
                current_difficulty_index = list(Difficulty).index(self.difficulty)
                next_difficulty_index = (current_difficulty_index + 1) % len(Difficulty)
                self.difficulty = list(Difficulty)[next_difficulty_index]
            elif user_input == "difficulty_down":
                current_difficulty_index = list(Difficulty).index(self.difficulty)
                next_difficulty_index = (current_difficulty_index - 1) % len(Difficulty)
                self.difficulty = list(Difficulty)[next_difficulty_index]
            else:
                raise KeyError(f"Unexpected input {user_input}")

    def runGame(self):
        result = None
        while True:
            self.view.displayBoard(self.model.turn,self.difficulty,result)
            user_input = self.view.userInput()
            if type(user_input) == list:
                result = self.model.checkGuess(user_input)
            elif type(user_input) == str:
                if user_input == "exit":
                    break