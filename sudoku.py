def is_valid(board, row, col, num):
    """
        Checks if a number can be placed in a specific position without violating Sudoku rules.

        Parameters:
            board (list of list of int): The current Sudoku board.
            row (int): The row index where the number is to be placed.
            col (int): The column index where the number is to be placed.
            num (int): The number to place on the Sudoku board.

        Returns:
            bool: True if the placement is valid, False otherwise.
    """
    for j in range(9):
        if board[row][j] == num:
            return False
    for i in range(9):
        if board[i][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True


def solve_sudoku(board):
    """
        Solves a Sudoku puzzle using a recursive backtracking algorithm.

        Parameters:
            board (list of list of int): The Sudoku board to solve.

        Returns:
            bool: True if the Sudoku puzzle is solvable and has been solved, False otherwise.
    """
    empty = find_empty(board)
    if not empty:
        return True
    else:
        row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False #Trigger for recursive backtrack


def find_empty(board):
    """
        Finds the next empty spot on the board, represented by 0.

        Parameters:
            board (list of list of int): The Sudoku board to check for empty spots.

        Returns:
            tuple: A tuple (row, col) representing the next empty spot on the board. None if no empty spots are available.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j


def print_board(board, i):
    """
        Prints the Sudoku board in a formatted way to the console.

        Parameters:
            board (list of list of int): The Sudoku board to print.
            i (int): The puzzle index, used for identifying the puzzle file.

        Returns:
            None
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('-' * 23)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')


def read_puzzle(file_path):
    """
       Reads a Sudoku puzzle from a text file and represents it as a 2D list.

       Parameters:
           file_path (str): The path to the puzzle text file.

       Returns:
           list of list of int: The read Sudoku puzzle represented as a 2D list.
    """
    with open(file_path, 'r') as f:
        puzzle = [[0 if num == '_' else int(num) for num in line.split()] for line in f]
    return puzzle


def write_solution(board, i):
    """
        Writes the Sudoku solution to a text file in a semi-formatted way if the puzzle is solvable.

        Parameters:
            board (list of list of int): The Sudoku board that contains the solution.
            i (int): The puzzle index, used for identifying the solution file.

        Returns:
            None
    """
    f = open(f'solution{i}.txt', 'w+')
    if solve_sudoku(board):
        for i in range(len(board)):
            for j in range(len(board)):
                if j == 8:
                    f.write(str(board[i][j]))
                else:
                    f.write(str(board[i][j]) + ' ')
            f.write('\n')
        f.write('\nSolutions Found: 1')
    else:
        f.write('No Solutions Found')


def print_solution(board, i):
    """
        Prints the Sudoku solution to the console and calls functions to print and write the solution.

        Parameters:
            board (list of list of int): The Sudoku board that contains the solution.
            i (int): The puzzle index, used for the solution output.

        Returns:
            None
    """
    print(f'solution{i}.txt:')
    if solve_sudoku(board):
        print_board(board, i)
        print(f'\nSolutions Found: 1')
    else:
        print('No solution found')
    print('\n' + '=' * 23 + '\n')
