import unittest
from game.models.mastermindModel import MasterMindModel

class TestMasterMindModel(unittest.TestCase):
    def test_init(self):
        code = ["Red","Blue","Purple","Orange"]
        mm = MasterMindModel(code)
        self.assertEqual(mm.secretCode,code)
        
        
        
        
    def test_checkGuess(self):
        pass