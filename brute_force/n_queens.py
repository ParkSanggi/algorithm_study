n = 5
cols = [0 for i in range(n+1)]


def promising(level):

    for i in range(1, level):
        if cols[i] == cols[level]:
            return False
        elif level - i == abs(cols[level] - cols[i]):
            return False
    return True


def queens(level):
    if not promising(level):
        return False
    elif level == n:
        for i in range(1, n+1):
            print(f"({i}, {cols[i]})")
        return True

    for j in range(1, n+1):
        cols[level + 1] = j
        if queens(level + 1):
            return True
    return False


if __name__ == "__main__":
    queens(0)
