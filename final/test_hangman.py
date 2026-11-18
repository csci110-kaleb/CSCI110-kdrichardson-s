import unittest
from hangman import HangmanBoard


class TestHangmanBoard(unittest.TestCase):





    def test_correct_guess(self):
        board = HangmanBoard("python")
        result = board.guess("p")
        self.assertTrue(result)
        self.assertIn("p", board.guessed)
        self.assertEqual(board.mistakes, 0)
        self.assertEqual(board.display(), "p _ _ _ _ _")

    def test_incorrect_guess(self):
        board = HangmanBoard("python")
        result = board.guess("x")
        self.assertFalse(result)
        self.assertIn("x", board.guessed)
        self.assertEqual(board.mistakes, 1)
        self.assertEqual(board.display(), "_ _ _ _ _ _")
