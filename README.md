HW: Sudoku 4
------------

Now that we have the data structures to create CNF sentences, let's translate
our Sudoku formulation from HW: Sudoku 2.

1. In ```sudoku.py```, create a class called SudokuBoard such that we can 
   create a 2x2 sudoku board by typing:
   
           board = SudokuBoard([[0, 0, 0, 3], 
                                [0, 0, 0, 2], 
                                [3, 0, 0, 0], 
                                [4, 0, 0, 0]])

   The digit "0" indicates that the cell has not yet been filled in. In this
   example, cells (1,4) and (3,1) are filled with a "3", cell (2,4) is filled
   with a "2", and cell (4,1) is filled with a "4".
   
   Note that the constructor should accept any kxk board, where k >= 2.
   
   Make sure it supports the following methods:
   
   - ```str(board)``` should return a simple string representation of the 
   board. For the above example, the string representation should 
   be ```"0003\n0002\n3000\n4000"```.
   - ```board.rows()``` should return a list of sets, where each set
   corresponds to the addresses of a single row. For a 2x2 Sudoku board,
   this would be:
   
       [{(1, 1), (1, 2), (1, 3), (1, 4)}, 
        {(2, 1), (2, 2), (2, 3), (2, 4)}, 
        {(3, 1), (3, 2), (3, 3), (3, 4)}, 
        {(4, 1), (4, 2), (4, 3), (4, 4)}]  
        
   The order of the rows in the list should be top-to-bottom.
   - ```board.columns()``` should return a list of sets, where each set
   corresponds to the addresses of a single column. For a 2x2 Sudoku board,
   this would be:
   
       [{(1, 1), (2, 1), (3, 1), (4, 1)}, 
        {(1, 2), (2, 2), (3, 2), (4, 2)}, 
        {(1, 3), (2, 3), (3, 3), (4, 3)}, 
        {(1, 4), (2, 4), (3, 4), (4, 4)}]
                
   Note that the order of the columns in the list should be top-to-bottom.
   - ```board.boxes()``` should return a list of sets, where each set
   corresponds to the addresses of a single box. For a 2x2 Sudoku board,
   this would be:
   
       [{(1, 1), (1, 2), (2, 1), (2, 2)}, 
        {(1, 3), (1, 4), (2, 3), (2, 4)}, 
        {(3, 1), (3, 2), (4, 1), (4, 2)}, 
        {(3, 3), (3, 4), (4, 3), (4, 4)}]
                
   Note that the order of the boxes in the list should be left-to-right, 
   then top-to-bottom.

   Once you have a successful implementation, the following unit tests should
   succeed:
   
       python -m unittest test_sudoku.TestSudokuBoard


2. We are almost ready to create CNF clauses, but in order to unit test them,
   we will want an ability to sort the clauses if they appear in a list (so 
   that we can easily compare results). To do this, we must augment the
   cnf.Clause class to support comparison operators. We'll say that a
   clause is "less than" another clause if it its string representation
   is alphabetically first (according to Python's default string comparison).

   Once you have successfully extended the Clause class, the following unit
   tests should succeed:
   
       python -m unittest test_sudoku.TestClauseComparison   


3. Now we want to create clauses according to our CNF formulation from
   HW: Sudoku 2. First, create clauses for the constraint "each zone must
   contain digit d at least once". In ```sudoku.py```, create a function 
   ```at_least_clause(A, d)``` which takes a set ```A``` of cell addresses
   and a digit ```d```. It should produce a string representation of the 
   clause corresponding to the constraint "digit ```d``` should appear at least
   once among the addresses in ```A```". For instance:
   
       at_least_clause({(1, 3), (1, 4), (2, 3), (2, 4)}, d=2)
       
   should return the string:
   
       'd2_1_3 || d2_1_4 || d2_2_3 || d2_2_4'
       
   For this string, the literals are expected to be listed in alphabetical 
   order (according to a string comparison).

   Once you have successfully implemented the function, the following unit
   tests should succeed:
   
       python -m unittest test_sudoku.TestAtLeastClause   
   
4. Next, create clauses for the constraint "each zone must
   contain digit d at most once". In ```sudoku.py```, create a function 
   ```at_most_clauses(A, d)``` which takes a set ```A``` of cell addresses
   and a digit ```d```. It should produce a list of the string representations
   of the clauses corresponding to the constraint "digit d should appear at most
   once among the addresses in A". For instance:
   
       at_most_clauses({(1, 3), (1, 4), (2, 3), (2, 4)}, d=2)
       
   should return the list:
   
       ['!d2_1_3 || !d2_1_4', 
        '!d2_1_3 || !d2_2_3', 
        '!d2_1_3 || !d2_2_4', 
        '!d2_1_4 || !d2_2_3', 
        '!d2_1_4 || !d2_2_4', 
        '!d2_2_3 || !d2_2_4']

   Once you have successfully implemented the function, the following unit
   tests should succeed:
   
       python -m unittest test_sudoku.TestAtMostClauses   
       
5. Create clauses for the constraint "no cell can be empty". 
   In ```sudoku.py```, create a function 
   ```nonempty_clauses(k)``` where ```k``` is the width of a box on your
   Sudoku board.  It should produce a list of the string representations
   of the clauses corresponding to the constraint "this cell should contain
   a digit". For instance:
   
       nonempty_clauses(2)
       
   should return the list:
   
       ['d1_1_1 || d2_1_1 || d3_1_1 || d4_1_1', 
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

   Once you have successfully implemented the function, the following unit
   tests should succeed:
   
       python -m unittest test_sudoku.TestNonemptyClauses   

       
6. Finally, put this all together into a method .cnf() of SudokuBoard.
   Calling board.cnf() should construct a cnf.Cnf instance containing all
   the clauses that are needed to express the SudokuBoard board. See the
   unit test for an example input/output.

   Once you have successfully implemented the method, the following unit
   tests should succeed:
   
       python -m unittest test_sudoku.TestCnfConversion
   
# proj-sudoku4
