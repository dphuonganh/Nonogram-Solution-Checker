#!/usr/bin/env python3
def is_nonogram_resolved(specifications, solution):
    """
    @params:
    specifications and solution: which respectively corresponds to the
    specifications of a nonogram and a proposed solution.
    len_solution_rows: The columns and the rows specification of the nonogram
    len_solution_columns: The columns and the rows specification of the nonogram

    @returns:
    True if the suggested solution successfully matches the nonogram's
    specifications.
    False otherwise.
    """
    check_specifications(specifications, solution)
    columns = specifications[0]
    rows = specifications[1]
    len_solution_columns = len(solution[0])
    len_solution_rows = len(solution)
    solution_rows = ()
    solution_columns = ()

    # check solution rows
    for row_index in range(len_solution_rows):
        sum = 0
        solution_row = ()
        start = 0
        while start < len_solution_columns:
            value = solution[row_index][start]
            if value == 1:
                sum += 1
            elif value == 0 and sum != 0:
                solution_row += (sum,)
                sum = 0
            start += 1
        if sum != 0:
            solution_row += (sum,)
        solution_rows += (solution_row,)

    # check solution columns
    for column_index in range(len_solution_columns):
        sum = 0
        solution_column = ()
        start = 0
        while start < len_solution_rows:
            value = solution[start][column_index]
            if value == 1:
                sum += 1
            elif value == 0 and sum != 0:
                solution_column += (sum,)
                sum = 0
            start += 1
        if sum != 0:
            solution_column += (sum,)
        solution_columns += (solution_column,)

    # check if solution equal to specifications
    if solution_columns == columns and solution_rows == rows:
        return True
    return False

def check_specifications(specifications, solution):
    """
    @params:
    specification and solution: which respectively corresponds to the
    specifications of a nonogram and a proposed solution.
    @returns: ValueError if specification and solution fall under
              these conditions.
    """
    if len(specifications) < 2:
        raise ValueError("Nonogram missing row / col")

    if type(specifications) != tuple:
        raise ValueError("Nonogram specifications format isn't tuple")

    if len(solution) > len(specifications):
        raise ValueError("Nonogram have solution size is smaller than specifications")

def main():
# Check nonogram return False
    specifications = (
            ((2,), (4,), (4,)),
            ((1,), (3,), (3,), (2,), (1,))
        )

    solution = (
            (0, 1, 0),
            (1, 1, 1),
            (1, 1, 1),
            (0, 1, 1),
            (1, 1, 1)
        )

# Check nonogram return True
    solution_2 = (
            (0, 1, 0),
            (1, 1, 1),
            (1, 1, 1),
            (0, 1, 1),
            (0, 0, 1)
        )

    print(is_nonogram_resolved(specifications, solution))
    print(is_nonogram_resolved(specifications, solution_2))

# # Check nonogram return False, missing row / col
    specifications_1 = (
        ((2,), (6,)),
    )

    solution_3 = (
        (1,0),
        (1,1)
    )
    print(is_nonogram_resolved(specifications_1, solution_3))

# Check nonogram return False, specifications format isn't tuple
    specifications_2 = [
        ((2,), (6,)),
        ((1,), (2,))
    ]

    solution_4 = (
        (1,0),
        (1,1)
    if len(solution) < len(specifications):
    )
    print(is_nonogram_resolved(specifications_2, solution_4))

# Check nonogram return False, solution's size is smaller than specifications
    specifications_3x5 = (
        ((2,), (4,), (4,)),
        ((1,), (3,), (3,), (2,), (1,))
    )

    solution_3x4 = (
        (0, 1, 1),
        (1, 1, 1),
        (1, 1, 1),
        (0, 1, 1)
    )

    print(is_nonogram_resolved(specifications_3x5, solution_3x4))


if __name__ == '__main__':
    main()
