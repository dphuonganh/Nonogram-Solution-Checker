#!/usr/bin/env python3

def check_value(solution, len_rows, len_columns):
    result = ()
    for index in range(len_rows):
        sum = 0
        solution_row = ()
        start = 0
        while start < len_columns:
            value = solution[index][start]
            if value == 1:
                sum += 1
            elif value == 0 and sum != 0:
                solution_row += (sum,)
                sum = 0
            start += 1
        if sum != 0:
            solution_row += (sum,)
        result += (solution_row,)
    print(result)

def is_nonogram_resolved(specifications, solution):
    columns = specifications[0]
    rows = specifications[1]
    len_solution_columns = len(solution[0])
    len_solution_rows = len(solution)
    solution_rows = ()
    solution_columns = ()

    check_value(solution, len_solution_rows, len_solution_columns)

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
    # print(solution_rows)

    

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
    # print(solution_columns)

    # check if solution equal to specifications
    if solution_columns == columns and solution_rows == rows:
        return True
    return False

def main():
    specifications = (
            ((2,), (4,), (4,)),
            ((1,), (3,), (3,), (2,), (1,))
        )

    solution1 = (
            (0, 1, 0),
            (1, 1, 1),
            (1, 1, 1),
            (0, 1, 1),
            (1, 1, 1)
        )

    solution2 = (
            (0, 1, 0),
            (1, 1, 1),
            (1, 1, 1),
            (0, 1, 1),
            (0, 0, 1)
        )

    print(is_nonogram_resolved(specifications, solution1))
    # print(is_nonogram_resolved(specifications, solution2))

if __name__ == '__main__':
    main()
