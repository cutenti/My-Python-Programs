def n_queens_fast(n):
    """Оптимизированное решение с использованием битовых операций"""

    def solve(row, cols, diag1, diag2):
        nonlocal count
        if row == n:
            count += 1
            return

        available = ((1 << n) - 1) & ~(cols | diag1 | diag2)

        while available:
            pos = available & -available
            available -= pos

            solve(row + 1, cols | pos, (diag1 | pos) << 1, (diag2 | pos) >> 1)

    count = 0
    solve(0, 0, 0, 0)
    return count
