import time


def find_endpoint(memo, grid, path, start, end):
    if start == end:
        path.append((start[0], start[1]))
        return path

    if grid[start[0]][start[1] + 1] and (start[0], start[1] + 1) not in memo:
        path.append((start[0], start[1]))
        ret = find_endpoint(memo, grid, path, (start[0], start[1] + 1), end)
        if ret:
            return ret

    if grid[start[0] + 1][start[1]] and (start[0] + 1, start[1]) not in memo:
        path.append((start[0], start[1]))
        ret = find_endpoint(memo, grid, path, (start[0] + 1, start[1]), end)
        if ret:
            return ret

    memo[f'{start}'] = 0

    path.pop()


memo = {}
grid = [[1, 1, 1, 1, None], [1, None, 1, 1, None], [1, 1, None, None, None], [None, 1, 1, 1, None],
        [None, None, None, None]]
path = []
start = time.time()
print(find_endpoint(memo, grid, path, (0, 0), (3, 3)))
end = time.time()
print("WorkingTime: {} sec".format(end - start))
