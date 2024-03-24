# EECS-210-Assignment-06

# Sudoku Solver

This project consists of a Python script that automates the process of solving Sudoku puzzles. It reads puzzles from text files, solves them using a backtracking algorithm, and outputs the solutions to the console and writes them to text files.

## Files in the Project

- `driver.py`: The entry point of the script. It creates an instance of the `Executive` class.
- `executive.py`: Contains the `Executive` class that orchestrates the solving process.
- `sudoku.py`: Includes functions for checking the validity of the Sudoku board, finding empty spots, solving the Sudoku puzzle, and handling file input/output.

## How to Run

Make sure you have Python installed on your system. You can run the script from the command line:

```bash
python driver.py
```
This will start the solving process, and the solutions (if found) will be printed to the console and written to the respective solution#.txt files.
## Sudoku Puzzle Format
The Sudoku puzzles should be text files named puzzle#.txt, for example:

puzzle1.txt, puzzle2.txt, etc. 

Each puzzle file should contain a 9x9 grid of numbers separated by spaces, where unsolved spots are represented by an underscore _.

Example of a puzzle file:

```txt
5 _ _ _ _ _ _ _ _
_ _ _ _ 2 _ _ _ _
_ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ 3 _
_ _ _ 1 _ _ _ _ _
_ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ 4

```
