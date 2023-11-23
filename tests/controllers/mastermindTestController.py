import unittest
from unittest.mock import Mock,call

from game.controllers.mastermindController import MasterMindController
from game.models.mastermindModel import MasterMindModel
from game.controllers.mastermindController import Difficulty

class TestMasterMindController(unittest.TestCase):
    @unittest.skip("Changed start_menu, using start_menu2")
    def test_start_menu(self):
        ## First start menu test
        ## View display menu should be called
        mc = MasterMindController()
        mock_view = Mock()

        mc.setView(mock_view)
        mc.start_menu()

        self.assertEqual(mock_view,mc.view)
        self.assertTrue(mock_view.displayMenu.called)
    
    def test_start_menu2(self):
        ## Second version start menu
        ## Start menu needs to be called passing the difficulty level, starting always at easy
        ## Waits for a user input:
        ### If input is "start_game" function run_game should be called
        ### If input is "exit" game should be closed
        ### Any other input needs to raise a keyValue error
        ## The function needs to stay in a loop waiting for "start_game" or "exit" calls.
        mc = MasterMindController()
        mock_view = Mock()
        mock_view.userInput.return_value = "exit"
        mc.setView(mock_view)
        mc.start_menu()

        expected_arguments = Difficulty.EASY

        mock_view.displayMenu.assert_has_calls([call(expected_arguments)])
        mock_view.userInput.assert_called_once()

        mock_view.userInput.side_effect = ["aaaa",KeyError("Unexpected input aaaa")]
        with self.assertRaises(KeyError):
            mc.start_menu()
    
    def test_run_game(self):
        pass

    