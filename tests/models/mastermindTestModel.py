import unittest
from game.models.mastermindModel import MasterMindModel

class TestMasterMindModel(unittest.TestCase):
    def test_init(self):
        code = ["Red","Blue","Purple","Orange"]
        mm = MasterMindModel(code)
        self.assertEqual(mm.secretCode,code)
        
    def test_init2(self):
        code = ["Red","Blue","Purple","Orange"]
        mm = MasterMindModel(code)
        self.assertEqual(mm.secretCode,code)
        self.assertEqual(0,mm.turn)
        self.assertEqual(["Red", "Green", "Blue", "Yellow","Orange","Purple"],mm.AVAILABLE_COLORS)
        self.assertEqual(6,mm.MAX_TURN)
        self.assertFalse(mm.gameEnded)
        
    def test_validateSecretCode(self):
        valid_secret_code = ["Red", "Green", "Blue", "Yellow"]
        invalid_secret_code = ["Red", "Cyan", "Blue", "Yellow"]
        
        mm = MasterMindModel(valid_secret_code)
        
        with self.assertRaises(ValueError):
            mm = MasterMindModel(invalid_secret_code)
        
        
    def test_checkGuess(self):
        pass