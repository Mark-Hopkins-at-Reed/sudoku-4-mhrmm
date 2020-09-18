import unittest
import cnf
from sudoku import SudokuBoard, at_most_clauses, at_least_clause
from sudoku import nonempty_clauses

class TestSudokuBoard(unittest.TestCase):

    def test_board_str(self):
        board = SudokuBoard([[0, 0, 0, 3], 
                             [0, 0, 0, 2], 
                             [3, 0, 0, 0], 
                             [4, 0, 0, 0]])
        expected = "\n".join(["0003",
                              "0002",
                              "3000",
                              "4000"])
        assert str(board) == expected
        
    def test_board_rows(self):
        board = SudokuBoard([[0, 0, 0, 3], 
                             [0, 0, 0, 2], 
                             [3, 0, 0, 0], 
                             [4, 0, 0, 0]])
        expected = [{(1, 1), (1, 2), (1, 3), (1, 4)}, 
                    {(2, 1), (2, 2), (2, 3), (2, 4)}, 
                    {(3, 1), (3, 2), (3, 3), (3, 4)}, 
                    {(4, 1), (4, 2), (4, 3), (4, 4)}]
        assert board.rows() == expected

    def test_board_columns(self):
        board = SudokuBoard([[0, 0, 0, 3], 
                             [0, 0, 0, 2], 
                             [3, 0, 0, 0], 
                             [4, 0, 0, 0]])
        expected = [{(1, 1), (2, 1), (3, 1), (4, 1)}, 
                    {(1, 2), (2, 2), (3, 2), (4, 2)}, 
                    {(1, 3), (2, 3), (3, 3), (4, 3)}, 
                    {(1, 4), (2, 4), (3, 4), (4, 4)}]
        assert board.columns() == expected
        
    def test_board_boxes(self):
        board = SudokuBoard([[0, 0, 0, 3], 
                             [0, 0, 0, 2], 
                             [3, 0, 0, 0], 
                             [4, 0, 0, 0]])
        expected = [{(1, 1), (1, 2), (2, 1), (2, 2)}, 
                    {(1, 3), (1, 4), (2, 3), (2, 4)}, 
                    {(3, 1), (3, 2), (4, 1), (4, 2)}, 
                    {(3, 3), (3, 4), (4, 3), (4, 4)}]
        assert board.boxes() == expected
 
class TestClauseComparison(unittest.TestCase):

    def test_clause_compare1(self):
        assert cnf.c('d2_1_3 || !d2_1_4') < cnf.c('d3_1_3 || !d3_1_4')

    def test_clause_compare2(self):
        assert cnf.c('!d2_1_3 || !d2_1_4') < cnf.c('d3_1_3 || !d3_1_4')

    def test_clause_compare3(self):
        assert cnf.c('!d3_1_3 || !d3_1_4') < cnf.c('d2_1_3 || !d2_1_4')

class TestAtMostClauses(unittest.TestCase):
 
 
    def test_at_most_clauses(self):
        result = at_most_clauses({(1, 3), (1, 4), (2, 3), (2, 4)}, d=2)
        clauses = sorted([str(c) for c in result])  
        expected = ['!d2_1_3 || !d2_1_4', 
                    '!d2_1_3 || !d2_2_3', 
                    '!d2_1_3 || !d2_2_4', 
                    '!d2_1_4 || !d2_2_3', 
                    '!d2_1_4 || !d2_2_4', 
                    '!d2_2_3 || !d2_2_4']
        assert clauses == expected   

class TestAtLeastClause(unittest.TestCase):
    
    def test_at_least_clause(self):
        result = at_least_clause({(1, 3), (1, 4), (2, 3), (2, 4)}, d=2)
        expected = 'd2_1_3 || d2_1_4 || d2_2_3 || d2_2_4'
        assert result == expected   

class TestNonemptyClauses(unittest.TestCase):
    
    def test_nonempty_clauses2(self):
        result = nonempty_clauses(2)
        sent = sorted([str(c) for c in result])  
        expected = ['d1_1_1 || d2_1_1 || d3_1_1 || d4_1_1', 
                    'd1_1_2 || d2_1_2 || d3_1_2 || d4_1_2', 
                    'd1_1_3 || d2_1_3 || d3_1_3 || d4_1_3', 
                    'd1_1_4 || d2_1_4 || d3_1_4 || d4_1_4', 
                    'd1_2_1 || d2_2_1 || d3_2_1 || d4_2_1', 
                    'd1_2_2 || d2_2_2 || d3_2_2 || d4_2_2', 
                    'd1_2_3 || d2_2_3 || d3_2_3 || d4_2_3', 
                    'd1_2_4 || d2_2_4 || d3_2_4 || d4_2_4', 
                    'd1_3_1 || d2_3_1 || d3_3_1 || d4_3_1', 
                    'd1_3_2 || d2_3_2 || d3_3_2 || d4_3_2', 
                    'd1_3_3 || d2_3_3 || d3_3_3 || d4_3_3', 
                    'd1_3_4 || d2_3_4 || d3_3_4 || d4_3_4', 
                    'd1_4_1 || d2_4_1 || d3_4_1 || d4_4_1', 
                    'd1_4_2 || d2_4_2 || d3_4_2 || d4_4_2', 
                    'd1_4_3 || d2_4_3 || d3_4_3 || d4_4_3', 
                    'd1_4_4 || d2_4_4 || d3_4_4 || d4_4_4']
        assert sent == expected
    
    def test_nonempty_clauses3(self):
        result = nonempty_clauses(3)
        sent = sorted([str(c) for c in result])  
        expected = ['d1_1_1 || d2_1_1 || d3_1_1 || d4_1_1 || d5_1_1 || d6_1_1 || d7_1_1 || d8_1_1 || d9_1_1', 
                    'd1_1_2 || d2_1_2 || d3_1_2 || d4_1_2 || d5_1_2 || d6_1_2 || d7_1_2 || d8_1_2 || d9_1_2', 
                    'd1_1_3 || d2_1_3 || d3_1_3 || d4_1_3 || d5_1_3 || d6_1_3 || d7_1_3 || d8_1_3 || d9_1_3', 
                    'd1_1_4 || d2_1_4 || d3_1_4 || d4_1_4 || d5_1_4 || d6_1_4 || d7_1_4 || d8_1_4 || d9_1_4', 
                    'd1_1_5 || d2_1_5 || d3_1_5 || d4_1_5 || d5_1_5 || d6_1_5 || d7_1_5 || d8_1_5 || d9_1_5', 
                    'd1_1_6 || d2_1_6 || d3_1_6 || d4_1_6 || d5_1_6 || d6_1_6 || d7_1_6 || d8_1_6 || d9_1_6', 
                    'd1_1_7 || d2_1_7 || d3_1_7 || d4_1_7 || d5_1_7 || d6_1_7 || d7_1_7 || d8_1_7 || d9_1_7', 
                    'd1_1_8 || d2_1_8 || d3_1_8 || d4_1_8 || d5_1_8 || d6_1_8 || d7_1_8 || d8_1_8 || d9_1_8', 
                    'd1_1_9 || d2_1_9 || d3_1_9 || d4_1_9 || d5_1_9 || d6_1_9 || d7_1_9 || d8_1_9 || d9_1_9']
        assert sent[:9] == expected

class TestCnfConversion(unittest.TestCase):
    
    def test_constraints(self):
        board0 = SudokuBoard([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        expected =  ['!d1_1_1 || !d1_1_2',
                     '!d1_1_1 || !d1_1_3',
                     '!d1_1_1 || !d1_1_4',
                     '!d1_1_1 || !d1_2_1',
                     '!d1_1_1 || !d1_2_2',
                     '!d1_1_1 || !d1_3_1',
                     '!d1_1_1 || !d1_4_1',
                     '!d1_1_2 || !d1_1_3',
                     '!d1_1_2 || !d1_1_4',
                     '!d1_1_2 || !d1_2_1',
                     '!d1_1_2 || !d1_2_2',
                     '!d1_1_2 || !d1_3_2',
                     '!d1_1_2 || !d1_4_2',
                     '!d1_1_3 || !d1_1_4',
                     '!d1_1_3 || !d1_2_3',
                     '!d1_1_3 || !d1_2_4',
                     '!d1_1_3 || !d1_3_3',
                     '!d1_1_3 || !d1_4_3',
                     '!d1_1_4 || !d1_2_3',
                     '!d1_1_4 || !d1_2_4',
                     '!d1_1_4 || !d1_3_4',
                     '!d1_1_4 || !d1_4_4',
                     '!d1_2_1 || !d1_2_2',
                     '!d1_2_1 || !d1_2_3',
                     '!d1_2_1 || !d1_2_4',
                     '!d1_2_1 || !d1_3_1',
                     '!d1_2_1 || !d1_4_1',
                     '!d1_2_2 || !d1_2_3',
                     '!d1_2_2 || !d1_2_4',
                     '!d1_2_2 || !d1_3_2',
                     '!d1_2_2 || !d1_4_2',
                     '!d1_2_3 || !d1_2_4',
                     '!d1_2_3 || !d1_3_3',
                     '!d1_2_3 || !d1_4_3',
                     '!d1_2_4 || !d1_3_4',
                     '!d1_2_4 || !d1_4_4',
                     '!d1_3_1 || !d1_3_2',
                     '!d1_3_1 || !d1_3_3',
                     '!d1_3_1 || !d1_3_4',
                     '!d1_3_1 || !d1_4_1',
                     '!d1_3_1 || !d1_4_2',
                     '!d1_3_2 || !d1_3_3',
                     '!d1_3_2 || !d1_3_4',
                     '!d1_3_2 || !d1_4_1',
                     '!d1_3_2 || !d1_4_2',
                     '!d1_3_3 || !d1_3_4',
                     '!d1_3_3 || !d1_4_3',
                     '!d1_3_3 || !d1_4_4',
                     '!d1_3_4 || !d1_4_3',
                     '!d1_3_4 || !d1_4_4',
                     '!d1_4_1 || !d1_4_2',
                     '!d1_4_1 || !d1_4_3',
                     '!d1_4_1 || !d1_4_4',
                     '!d1_4_2 || !d1_4_3',
                     '!d1_4_2 || !d1_4_4',
                     '!d1_4_3 || !d1_4_4',
                     '!d2_1_1 || !d2_1_2',
                     '!d2_1_1 || !d2_1_3',
                     '!d2_1_1 || !d2_1_4',
                     '!d2_1_1 || !d2_2_1',
                     '!d2_1_1 || !d2_2_2',
                     '!d2_1_1 || !d2_3_1',
                     '!d2_1_1 || !d2_4_1',
                     '!d2_1_2 || !d2_1_3',
                     '!d2_1_2 || !d2_1_4',
                     '!d2_1_2 || !d2_2_1',
                     '!d2_1_2 || !d2_2_2',
                     '!d2_1_2 || !d2_3_2',
                     '!d2_1_2 || !d2_4_2',
                     '!d2_1_3 || !d2_1_4',
                     '!d2_1_3 || !d2_2_3',
                     '!d2_1_3 || !d2_2_4',
                     '!d2_1_3 || !d2_3_3',
                     '!d2_1_3 || !d2_4_3',
                     '!d2_1_4 || !d2_2_3',
                     '!d2_1_4 || !d2_2_4',
                     '!d2_1_4 || !d2_3_4',
                     '!d2_1_4 || !d2_4_4',
                     '!d2_2_1 || !d2_2_2',
                     '!d2_2_1 || !d2_2_3',
                     '!d2_2_1 || !d2_2_4',
                     '!d2_2_1 || !d2_3_1',
                     '!d2_2_1 || !d2_4_1',
                     '!d2_2_2 || !d2_2_3',
                     '!d2_2_2 || !d2_2_4',
                     '!d2_2_2 || !d2_3_2',
                     '!d2_2_2 || !d2_4_2',
                     '!d2_2_3 || !d2_2_4',
                     '!d2_2_3 || !d2_3_3',
                     '!d2_2_3 || !d2_4_3',
                     '!d2_2_4 || !d2_3_4',
                     '!d2_2_4 || !d2_4_4',
                     '!d2_3_1 || !d2_3_2',
                     '!d2_3_1 || !d2_3_3',
                     '!d2_3_1 || !d2_3_4',
                     '!d2_3_1 || !d2_4_1',
                     '!d2_3_1 || !d2_4_2',
                     '!d2_3_2 || !d2_3_3',
                     '!d2_3_2 || !d2_3_4',
                     '!d2_3_2 || !d2_4_1',
                     '!d2_3_2 || !d2_4_2',
                     '!d2_3_3 || !d2_3_4',
                     '!d2_3_3 || !d2_4_3',
                     '!d2_3_3 || !d2_4_4',
                     '!d2_3_4 || !d2_4_3',
                     '!d2_3_4 || !d2_4_4',
                     '!d2_4_1 || !d2_4_2',
                     '!d2_4_1 || !d2_4_3',
                     '!d2_4_1 || !d2_4_4',
                     '!d2_4_2 || !d2_4_3',
                     '!d2_4_2 || !d2_4_4',
                     '!d2_4_3 || !d2_4_4',
                     '!d3_1_1 || !d3_1_2',
                     '!d3_1_1 || !d3_1_3',
                     '!d3_1_1 || !d3_1_4',
                     '!d3_1_1 || !d3_2_1',
                     '!d3_1_1 || !d3_2_2',
                     '!d3_1_1 || !d3_3_1',
                     '!d3_1_1 || !d3_4_1',
                     '!d3_1_2 || !d3_1_3',
                     '!d3_1_2 || !d3_1_4',
                     '!d3_1_2 || !d3_2_1',
                     '!d3_1_2 || !d3_2_2',
                     '!d3_1_2 || !d3_3_2',
                     '!d3_1_2 || !d3_4_2',
                     '!d3_1_3 || !d3_1_4',
                     '!d3_1_3 || !d3_2_3',
                     '!d3_1_3 || !d3_2_4',
                     '!d3_1_3 || !d3_3_3',
                     '!d3_1_3 || !d3_4_3',
                     '!d3_1_4 || !d3_2_3',
                     '!d3_1_4 || !d3_2_4',
                     '!d3_1_4 || !d3_3_4',
                     '!d3_1_4 || !d3_4_4',
                     '!d3_2_1 || !d3_2_2',
                     '!d3_2_1 || !d3_2_3',
                     '!d3_2_1 || !d3_2_4',
                     '!d3_2_1 || !d3_3_1',
                     '!d3_2_1 || !d3_4_1',
                     '!d3_2_2 || !d3_2_3',
                     '!d3_2_2 || !d3_2_4',
                     '!d3_2_2 || !d3_3_2',
                     '!d3_2_2 || !d3_4_2',
                     '!d3_2_3 || !d3_2_4',
                     '!d3_2_3 || !d3_3_3',
                     '!d3_2_3 || !d3_4_3',
                     '!d3_2_4 || !d3_3_4',
                     '!d3_2_4 || !d3_4_4',
                     '!d3_3_1 || !d3_3_2',
                     '!d3_3_1 || !d3_3_3',
                     '!d3_3_1 || !d3_3_4',
                     '!d3_3_1 || !d3_4_1',
                     '!d3_3_1 || !d3_4_2',
                     '!d3_3_2 || !d3_3_3',
                     '!d3_3_2 || !d3_3_4',
                     '!d3_3_2 || !d3_4_1',
                     '!d3_3_2 || !d3_4_2',
                     '!d3_3_3 || !d3_3_4',
                     '!d3_3_3 || !d3_4_3',
                     '!d3_3_3 || !d3_4_4',
                     '!d3_3_4 || !d3_4_3',
                     '!d3_3_4 || !d3_4_4',
                     '!d3_4_1 || !d3_4_2',
                     '!d3_4_1 || !d3_4_3',
                     '!d3_4_1 || !d3_4_4',
                     '!d3_4_2 || !d3_4_3',
                     '!d3_4_2 || !d3_4_4',
                     '!d3_4_3 || !d3_4_4',
                     '!d4_1_1 || !d4_1_2',
                     '!d4_1_1 || !d4_1_3',
                     '!d4_1_1 || !d4_1_4',
                     '!d4_1_1 || !d4_2_1',
                     '!d4_1_1 || !d4_2_2',
                     '!d4_1_1 || !d4_3_1',
                     '!d4_1_1 || !d4_4_1',
                     '!d4_1_2 || !d4_1_3',
                     '!d4_1_2 || !d4_1_4',
                     '!d4_1_2 || !d4_2_1',
                     '!d4_1_2 || !d4_2_2',
                     '!d4_1_2 || !d4_3_2',
                     '!d4_1_2 || !d4_4_2',
                     '!d4_1_3 || !d4_1_4',
                     '!d4_1_3 || !d4_2_3',
                     '!d4_1_3 || !d4_2_4',
                     '!d4_1_3 || !d4_3_3',
                     '!d4_1_3 || !d4_4_3',
                     '!d4_1_4 || !d4_2_3',
                     '!d4_1_4 || !d4_2_4',
                     '!d4_1_4 || !d4_3_4',
                     '!d4_1_4 || !d4_4_4',
                     '!d4_2_1 || !d4_2_2',
                     '!d4_2_1 || !d4_2_3',
                     '!d4_2_1 || !d4_2_4',
                     '!d4_2_1 || !d4_3_1',
                     '!d4_2_1 || !d4_4_1',
                     '!d4_2_2 || !d4_2_3',
                     '!d4_2_2 || !d4_2_4',
                     '!d4_2_2 || !d4_3_2',
                     '!d4_2_2 || !d4_4_2',
                     '!d4_2_3 || !d4_2_4',
                     '!d4_2_3 || !d4_3_3',
                     '!d4_2_3 || !d4_4_3',
                     '!d4_2_4 || !d4_3_4',
                     '!d4_2_4 || !d4_4_4',
                     '!d4_3_1 || !d4_3_2',
                     '!d4_3_1 || !d4_3_3',
                     '!d4_3_1 || !d4_3_4',
                     '!d4_3_1 || !d4_4_1',
                     '!d4_3_1 || !d4_4_2',
                     '!d4_3_2 || !d4_3_3',
                     '!d4_3_2 || !d4_3_4',
                     '!d4_3_2 || !d4_4_1',
                     '!d4_3_2 || !d4_4_2',
                     '!d4_3_3 || !d4_3_4',
                     '!d4_3_3 || !d4_4_3',
                     '!d4_3_3 || !d4_4_4',
                     '!d4_3_4 || !d4_4_3',
                     '!d4_3_4 || !d4_4_4',
                     '!d4_4_1 || !d4_4_2',
                     '!d4_4_1 || !d4_4_3',
                     '!d4_4_1 || !d4_4_4',
                     '!d4_4_2 || !d4_4_3',
                     '!d4_4_2 || !d4_4_4',
                     '!d4_4_3 || !d4_4_4',
                    "d1_1_1 || d1_1_2 || d1_1_3 || d1_1_4",
                    "d1_1_1 || d1_1_2 || d1_2_1 || d1_2_2",
                    "d1_1_1 || d1_2_1 || d1_3_1 || d1_4_1",
                    "d1_1_1 || d2_1_1 || d3_1_1 || d4_1_1",
                    "d1_1_2 || d1_2_2 || d1_3_2 || d1_4_2",
                    "d1_1_2 || d2_1_2 || d3_1_2 || d4_1_2",
                    "d1_1_3 || d1_1_4 || d1_2_3 || d1_2_4",
                    "d1_1_3 || d1_2_3 || d1_3_3 || d1_4_3",
                    "d1_1_3 || d2_1_3 || d3_1_3 || d4_1_3",
                    "d1_1_4 || d1_2_4 || d1_3_4 || d1_4_4",
                    "d1_1_4 || d2_1_4 || d3_1_4 || d4_1_4",
                    "d1_2_1 || d1_2_2 || d1_2_3 || d1_2_4",
                    "d1_2_1 || d2_2_1 || d3_2_1 || d4_2_1",
                    "d1_2_2 || d2_2_2 || d3_2_2 || d4_2_2",
                    "d1_2_3 || d2_2_3 || d3_2_3 || d4_2_3",
                    "d1_2_4 || d2_2_4 || d3_2_4 || d4_2_4",
                    "d1_3_1 || d1_3_2 || d1_3_3 || d1_3_4",
                    "d1_3_1 || d1_3_2 || d1_4_1 || d1_4_2",
                    "d1_3_1 || d2_3_1 || d3_3_1 || d4_3_1",
                    "d1_3_2 || d2_3_2 || d3_3_2 || d4_3_2",
                    "d1_3_3 || d1_3_4 || d1_4_3 || d1_4_4",
                    "d1_3_3 || d2_3_3 || d3_3_3 || d4_3_3",
                    "d1_3_4 || d2_3_4 || d3_3_4 || d4_3_4",
                    "d1_4_1 || d1_4_2 || d1_4_3 || d1_4_4",
                    "d1_4_1 || d2_4_1 || d3_4_1 || d4_4_1",
                    "d1_4_2 || d2_4_2 || d3_4_2 || d4_4_2",
                    "d1_4_3 || d2_4_3 || d3_4_3 || d4_4_3",
                    "d1_4_4 || d2_4_4 || d3_4_4 || d4_4_4",
                    "d2_1_1 || d2_1_2 || d2_1_3 || d2_1_4",
                    "d2_1_1 || d2_1_2 || d2_2_1 || d2_2_2",
                    "d2_1_1 || d2_2_1 || d2_3_1 || d2_4_1",
                    "d2_1_2 || d2_2_2 || d2_3_2 || d2_4_2",
                    "d2_1_3 || d2_1_4 || d2_2_3 || d2_2_4",
                    "d2_1_3 || d2_2_3 || d2_3_3 || d2_4_3",
                    "d2_1_4 || d2_2_4 || d2_3_4 || d2_4_4",
                    "d2_2_1 || d2_2_2 || d2_2_3 || d2_2_4",
                    "d2_3_1 || d2_3_2 || d2_3_3 || d2_3_4",
                    "d2_3_1 || d2_3_2 || d2_4_1 || d2_4_2",
                    "d2_3_3 || d2_3_4 || d2_4_3 || d2_4_4",
                    "d2_4_1 || d2_4_2 || d2_4_3 || d2_4_4",
                    "d3_1_1 || d3_1_2 || d3_1_3 || d3_1_4",
                    "d3_1_1 || d3_1_2 || d3_2_1 || d3_2_2",
                    "d3_1_1 || d3_2_1 || d3_3_1 || d3_4_1",
                    "d3_1_2 || d3_2_2 || d3_3_2 || d3_4_2",
                    "d3_1_3 || d3_1_4 || d3_2_3 || d3_2_4",
                    "d3_1_3 || d3_2_3 || d3_3_3 || d3_4_3",
                    "d3_1_4 || d3_2_4 || d3_3_4 || d3_4_4",
                    "d3_2_1 || d3_2_2 || d3_2_3 || d3_2_4",
                    "d3_3_1 || d3_3_2 || d3_3_3 || d3_3_4",
                    "d3_3_1 || d3_3_2 || d3_4_1 || d3_4_2",
                    "d3_3_3 || d3_3_4 || d3_4_3 || d3_4_4",
                    "d3_4_1 || d3_4_2 || d3_4_3 || d3_4_4",
                    "d4_1_1 || d4_1_2 || d4_1_3 || d4_1_4",
                    "d4_1_1 || d4_1_2 || d4_2_1 || d4_2_2",
                    "d4_1_1 || d4_2_1 || d4_3_1 || d4_4_1",
                    "d4_1_2 || d4_2_2 || d4_3_2 || d4_4_2",
                    "d4_1_3 || d4_1_4 || d4_2_3 || d4_2_4",
                    "d4_1_3 || d4_2_3 || d4_3_3 || d4_4_3",
                    "d4_1_4 || d4_2_4 || d4_3_4 || d4_4_4",
                    "d4_2_1 || d4_2_2 || d4_2_3 || d4_2_4",
                    "d4_3_1 || d4_3_2 || d4_3_3 || d4_3_4",
                    "d4_3_1 || d4_3_2 || d4_4_1 || d4_4_2",
                    "d4_3_3 || d4_3_4 || d4_4_3 || d4_4_4",
                    "d4_4_1 || d4_4_2 || d4_4_3 || d4_4_4"]  
        assert '\n'.join(expected) == str(board0.cnf())
    
    
    
