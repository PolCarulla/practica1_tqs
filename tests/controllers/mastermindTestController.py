import unittest
from unittest.mock import Mock

from game.controllers.mastermindController import MasterMindController
from game.models.mastermindModel import MasterMindModel

class TestMasterMindController(unittest.TestCase):
    def test_start_menu(self):
        ## First start menu test
        ## View display menu should be called
        mc = MasterMindController()
        mock_view = Mock()

        mc.setView(mock_view)
        mc.start_menu()

        self.assertEqual(mock_view,mc.view)
        self.assertTrue(mock_view.displayMenu.called)
        
    def test_run_game(self):
        pass

    