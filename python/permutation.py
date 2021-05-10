def perm(data, k, n):
    if k == n - 1:
        print(data)
        return
    i = k
    while i < n:
        data[k], data[i] = data[i], data[k]
        perm(data, k + 1, n)
        data[k], data[i] = data[i], data[k]
        i += 1


if __name__ == "__main__":
    data = ['a', 'b', 'c', 'd']
    n = len(data)
    k = 0
    perm(data, k, n)
