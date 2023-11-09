from executive import Executive


def main():
    """
    The main function of the driver script.

    This function serves as the entry point of the script. It creates an instance of the Executive
    class and invokes its constructor, which in turn initializes the Sudoku solving process by
    reading puzzles from files, solving them, and printing and writing the solutions.

    No parameters or return values since it's the script's entry point.
    """
    Executive()


if __name__ == "__main__":
    main()
