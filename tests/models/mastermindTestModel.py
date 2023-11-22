import unittest
from game.models.mastermindModel import MasterMindModel

class TestMasterMindModel(unittest.TestCase):
    def test_init(self):
        ## Starting init test funcion
        ## Testing if model init with code as an argument stores it correctly
        code = ["Red","Blue","Purple","Orange"]
        mm = MasterMindModel(code)
        self.assertEqual(mm.secretCode,code)
        
    def test_init2(self):
        ## Second version of init funcion
        ## Added QoL variables such as starting turn to keep track of the game, available colors, max game turns and a bool to check if the game has ended 
        code = ["Red","Blue","Purple","Orange"]
        mm = MasterMindModel(code)
        self.assertEqual(0,mm.turn)
        self.assertEqual(["Red", "Green", "Blue", "Yellow","Orange","Purple"],mm.AVAILABLE_COLORS)
        self.assertEqual(6,mm.MAX_TURN)
        self.assertFalse(mm.gameEnded)
    
    def test_init3(self):
        ## Third version of init function
        ## Available colors can now be passed as an argument to the init function, default colors should be kept if not used
        ## Secret code can be ommitted during object init, setting it's value to None and skipping validateSecretCode
        available_colors = ["Red", "Green", "Blue", "Yellow","Black","White"]

        mm = MasterMindModel()
        self.assertIsNone(mm.secretCode)
        self.assertEqual(["Red", "Green", "Blue", "Yellow","Orange","Purple"],mm.AVAILABLE_COLORS)

        mm = MasterMindModel(available_colors=available_colors)
        self.assertEqual(available_colors,mm.AVAILABLE_COLORS)

    def test_validateSecretCode(self):

        valid_secret_code = ["Red", "Green", "Blue", "Yellow"]
        invalid_secret_code = ["Red", "Cyan", "Blue", "Yellow"]
        
        mm = MasterMindModel(valid_secret_code)
        
        with self.assertRaises(ValueError):
            mm = MasterMindModel(invalid_secret_code)
        
        
    def test_checkGuess(self):
        ## First version of checkGuess function
        ## In this version it only checks if the guess values are correct
        secret_code = ["Red", "Green", "Blue", "Yellow"]

        invalid_guess = ["Yellow","Blue","Green","Red"]
        valid_guess = ["Red", "Green", "Blue", "Yellow"]

        mm = MasterMindModel(secret_code)
        for element in mm.checkGuess(valid_guess):
            self.assertTrue(element)
        
        for element in mm.checkGuess(invalid_guess):
            self.assertFalse(element)
    
    def test_checkGuess2(self):
        ## Second version of checkGuess function
        ## Added individual check for the values
        ## gameEnded variable should change to True if the correct code is passed
        secret_code = ["Red", "Green", "Blue", "Yellow"]
        mm = MasterMindModel(secret_code)

        invalid_guess2 = ["Yellow","Green","Blue","Red"]
        result_invalid_guess2 = [False,True,True,False]
        self.assertEqual(mm.checkGuess(invalid_guess2),result_invalid_guess2)
        self.assertFalse(mm.gameEnded)

        valid_guess = ["Red", "Green", "Blue", "Yellow"]
        for element in mm.checkGuess(valid_guess):
            self.assertTrue(element)
        
        self.assertTrue(mm.gameEnded)
    
    def test_checkGuess3(self):
        ## Third version of checkGuess function
        ## Every time a check is done the turn variable needs to be updated, unless the game ended.
        ## Error control for incorrect lenghts
        ## If turn equals MAX TURN it needs to set gameEnded to True
        secret_code = ["Red", "Green", "Blue", "Yellow"]
        invalid_guess = ["Yellow","Green","Blue","Red"]
        invalid_lenght = ["Blue","Red","Yellow"]

        mm = MasterMindModel(secret_code)

        self.assertEqual(0,mm.turn)

        mm.checkGuess(invalid_guess)

        self.assertEqual(1,mm.turn)

        with self.assertRaises(ValueError):
            mm.checkGuess(invalid_lenght)
        
        self.assertEqual(1,mm.turn)

        mm.MAX_TURN = 2

        mm.checkGuess(invalid_guess)
        
        self.assertTrue(mm.gameEnded)