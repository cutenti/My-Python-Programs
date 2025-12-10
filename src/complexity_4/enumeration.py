import itertools


def is_valid(board):
    """Проверяет, является ли расстановка корректной"""
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                return False

            if abs(board[i] - board[j]) == abs(i - j):
                return False
    return True


def n_queens_bruteforce(n):
    """Перебор всех возможных расстановок"""
    if n < 1 or n > 10:
        return 0

    count = 0

    for permutation in itertools.permutations(range(n)):
        if is_valid(permutation):
            count += 1
    return count
