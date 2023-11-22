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
        secret_code = ["Red", "Green", "Blue", "Yellow"]

        invalid_guess = ["Yellow","Blue","Green","Red"]
        valid_guess = ["Red", "Green", "Blue", "Yellow"]

        mm = MasterMindModel(secret_code)
        for element in mm.checkGuess(valid_guess):
            self.assertTrue(element)
        
        for element in mm.checkGuess(invalid_guess):
            self.assertFalse(element)
        