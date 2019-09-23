def find_endpoint(memo, grid, path, start, end):
    if start == end:
        path.append((start[0], start[1]))
        return path

    if grid[start[0]][start[1] + 1]:
        path.append((start[0], start[1]))
        ret = find_endpoint(memo, grid, path, (start[0], start[1] + 1), end)
        if ret:
            return ret

    if grid[start[0] + 1][start[1]]:
        path.append((start[0], start[1]))
        ret = find_endpoint(memo, grid, path, (start[0] + 1, start[1]), end)
        if ret:
            return ret

    path.pop()


memo = {}
grid = [[1, 1, None, None], [1, None, 1, None], [1, 1, 1, None], [None, None, None, None]]
path = []
find_endpoint(memo, grid, path, (0, 0), (2, 2))
