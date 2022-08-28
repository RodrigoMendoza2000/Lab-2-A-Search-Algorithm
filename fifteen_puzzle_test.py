# File: fifteen_puzzle_test.py

from unittest import TestCase, main
from io import StringIO
import sys
from fifteen_puzzle import solve_puzzle


class TestFifteenPuzzle(TestCase):

    def setUp(self) -> None:
        self.old_stdout = sys.stdout
        sys.stdout = self.buffer = StringIO()

    def tearDown(self) -> None:
        sys.stdout = self.old_stdout

    def test_1(self):
        solve_puzzle(((1, 2, 3, 4),
                      (5, 6, 7, 8),
                      (9, 10, 11, 12),
                      (13, 14, 15, 0)))
        self.assertEqual(
            'Solution requires 0 steps\n',
            self.buffer.getvalue())

    def test_2(self):
        solve_puzzle(((1, 2, 3, 4),
                      (5, 6, 7, 8),
                      (9, 10, 11, 0),
                      (13, 14, 15, 12)))
        self.assertEqual(
            'Solution requires 1 step\n'
            'Step 1: Move 12 up\n',
            self.buffer.getvalue())

    def test_3(self):
        solve_puzzle(((1, 2, 3, 4),
                      (5, 6, 7, 8),
                      (9, 10, 15, 11),
                      (13, 14, 0, 12)))
        self.assertEqual(
            'Solution requires 3 steps\n'
            'Step 1: Move 15 down\n'
            'Step 2: Move 11 left\n'
            'Step 3: Move 12 up\n',
            self.buffer.getvalue())

    def test_4(self):
        solve_puzzle(((2, 3, 4, 8),
                      (1, 5, 7, 11),
                      (9, 6, 12, 15),
                      (13, 14, 10, 0)))
        self.assertEqual(
            'Solution requires 16 steps\n'
            'Step 1: Move 15 down\n'
            'Step 2: Move 12 right\n'
            'Step 3: Move 10 up\n'
            'Step 4: Move 15 left\n'
            'Step 5: Move 12 down\n'
            'Step 6: Move 11 down\n'
            'Step 7: Move 8 down\n'
            'Step 8: Move 4 right\n'
            'Step 9: Move 3 right\n'
            'Step 10: Move 2 right\n'
            'Step 11: Move 1 up\n'
            'Step 12: Move 5 left\n'
            'Step 13: Move 6 up\n'
            'Step 14: Move 10 left\n'
            'Step 15: Move 11 left\n'
            'Step 16: Move 12 up\n',
            self.buffer.getvalue())

    def test_5(self):
        solve_puzzle(((1, 6, 2, 4),
                      (5, 10, 3, 8),
                      (0, 15, 9, 11),
                      (14, 7, 13, 12)))
        self.assertEqual(
            'Solution requires 24 steps\n'
            'Step 1: Move 15 left\n'
            'Step 2: Move 9 left\n'
            'Step 3: Move 13 up\n'
            'Step 4: Move 7 right\n'
            'Step 5: Move 9 down\n'
            'Step 6: Move 15 right\n'
            'Step 7: Move 14 up\n'
            'Step 8: Move 9 left\n'
            'Step 9: Move 15 down\n'
            'Step 10: Move 13 left\n'
            'Step 11: Move 7 up\n'
            'Step 12: Move 15 right\n'
            'Step 13: Move 13 down\n'
            'Step 14: Move 14 right\n'
            'Step 15: Move 9 up\n'
            'Step 16: Move 13 left\n'
            'Step 17: Move 14 down\n'
            'Step 18: Move 10 down\n'
            'Step 19: Move 6 down\n'
            'Step 20: Move 2 left\n'
            'Step 21: Move 3 up\n'
            'Step 22: Move 7 up\n'
            'Step 23: Move 11 left\n'
            'Step 24: Move 12 up\n',
            self.buffer.getvalue())

    def test_6(self):
        solve_puzzle(((5, 1, 6, 2),
                      (9, 10, 3, 0),
                      (13, 14, 4, 7),
                      (15, 8, 11, 12)))
        self.assertEqual(
            'Solution requires 28 steps\n'
            'Step 1: Move 3 right\n'
            'Step 2: Move 4 up\n'
            'Step 3: Move 11 up\n'
            'Step 4: Move 8 right\n'
            'Step 5: Move 15 right\n'
            'Step 6: Move 13 down\n'
            'Step 7: Move 9 down\n'
            'Step 8: Move 5 down\n'
            'Step 9: Move 1 left\n'
            'Step 10: Move 6 left\n'
            'Step 11: Move 2 left\n'
            'Step 12: Move 3 up\n'
            'Step 13: Move 4 right\n'
            'Step 14: Move 11 up\n'
            'Step 15: Move 8 up\n'
            'Step 16: Move 15 right\n'
            'Step 17: Move 14 down\n'
            'Step 18: Move 10 down\n'
            'Step 19: Move 6 down\n'
            'Step 20: Move 2 left\n'
            'Step 21: Move 3 left\n'
            'Step 22: Move 4 up\n'
            'Step 23: Move 7 up\n'
            'Step 24: Move 8 right\n'
            'Step 25: Move 11 down\n'
            'Step 26: Move 7 left\n'
            'Step 27: Move 8 up\n'
            'Step 28: Move 12 up\n',
            self.buffer.getvalue())


if __name__ == '__main__':
    main()