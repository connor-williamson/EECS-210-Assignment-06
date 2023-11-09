from sudoku import *


class Executive:
    """
        Orchestrates the Sudoku puzzle solving process.

        This class is responsible for the flow of operations required to solve Sudoku puzzles. It reads
        the puzzles from text files, solves them, and handles the output of the solutions both to the
        console and to the text files.

        Attributes:
            None explicitly defined.

        Methods:
            __init__: Constructs the Executive object and starts the solving process.
    """

    def __init__(self):
        """
            Initializes the Executive object and begins the puzzle solving process.

            Upon instantiation, it loops through a predefined set of puzzle files, reads the puzzle,
            attempts to solve it, prints the solution, and writes the solution to a file.

            Parameters:
                None

            Returns:
                None
        """
        for i in range(1, 6):
            file_name = f'puzzle{i}.txt'
            board = read_puzzle(file_name)
            print_solution(board, i)
            write_solution(board, i)
