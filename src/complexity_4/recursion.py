def n_queens_recursive(n):
    """Рекурсивное решение с возвратом"""

    def backtrack(row, cols, diag1, diag2):
        nonlocal count
        if row == n:
            count += 1
            return

        for col in range(n):
            if cols[col] or diag1[row + col] or diag2[row - col + n - 1]:
                continue

            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
            backtrack(row + 1, cols, diag1, diag2)

            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

    count = 0

    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    backtrack(0, cols, diag1, diag2)
    return count
