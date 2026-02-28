# Prodigy Infotech Internship - Task 04
# Sudoku Solver using Backtracking Algorithm


# Function to print Sudoku grid
def print_grid(grid, title):

    print("\n" + title + "\n")

    for row in grid:
        for num in row:
            print(num, end=" ")
        print()


# Function to check if a number is valid
def is_valid(grid, row, col, num):

    # Check row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[start_row+i][start_col+j] == num:
                return False

    return True


# Backtracking algorithm
def solve_sudoku(grid):

    for row in range(9):
        for col in range(9):

            if grid[row][col] == 0:

                for num in range(1, 10):

                    if is_valid(grid, row, col, num):

                        grid[row][col] = num

                        if solve_sudoku(grid):
                            return True

                        # Backtrack
                        grid[row][col] = 0

                return False

    return True


# Example Sudoku Puzzle (Unsolved)
example = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]


# Menu
print("Sudoku Solver")
print("1. Load Example Puzzle")
print("2. Enter Puzzle Manually")

choice = input("Enter choice (1 or 2): ")


# Load Example Puzzle
if choice == "1":

    sudoku = [row[:] for row in example]

    # Show Unsolved Puzzle
    print_grid(sudoku, "Unsolved Sudoku:")


# Manual Input
elif choice == "2":

    print("\nEnter Sudoku Grid (Use 0 for empty cells):")

    sudoku = []

    for i in range(9):
        row = list(map(int, input().split()))
        sudoku.append(row)

    print_grid(sudoku, "Unsolved Sudoku:")

else:
    print("Invalid choice")
    exit()


# Solve Sudoku
if solve_sudoku(sudoku):

    print_grid(sudoku, "Solved Sudoku:")

else:
    print("No solution exists")
