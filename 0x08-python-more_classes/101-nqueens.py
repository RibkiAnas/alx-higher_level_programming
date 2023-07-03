#!/usr/bin/python3
import sys


def is_valid_position(board, row, col):
    """Check if a given position on the
    chessboard is valid for placing a queen.

    A position is considered valid if there are
    no other queens in the same row, column
    or diagonal.

    Args:
        board: A two-dimensional list representing
        the current state of the chessboard.
        row: The row of the position to check.
        col: The column of the position to check.
    Returns:
        True if the position is valid, False otherwise.
    """
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

        # Check if there is a queen in the lower left diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

        # If there are no queens in the same
        # row or diagonals, the position is valid
    return True


def solve_nqueens(board, col):
    """Find all solutions to the N queens
    problem using a recursive backtracking
    algorithm.

    This function places a queen in a valid
    position in the current column and then
    recursively calls itself with the next
    column. If all columns have been considered,
    a solution has been found and it is printed
    to the console.

    Args:
        board: A two-dimensional list
        representing the current state of the
        chessboard.
        col: The current column being
        considered.

    Returns:
        None.
    """
    # If all columns have been considered, a solution has been found
    if col == len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    # Try placing a queen in each row of the current column
    for i in range(len(board)):
        if is_valid_position(board, i, col):
            # Place a queen in a valid position
            board[i][col] = 1
            # Recursively call solve_nqueens with the next column
            solve_nqueens(board, col + 1)
            # Backtrack and remove the queen from the current position
            board[i][col] = 0


if __name__ == "__main__":
    # Check if the user provided the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater than or equal to 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty chessboard
    board = [[0 for j in range(n)] for i in range(n)]
    # Call solve_nqueens with the first column
    solve_nqueens(board, 0)
