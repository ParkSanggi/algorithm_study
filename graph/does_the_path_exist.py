from queue import Queue

# 방향 그래프가 주어졌을 때 두 노드 사이에 경로가 존재하는 지 확인하는 알고리즘을 작성하세요.

n = 9


def search(start, end, graph):
    q = Queue()
    visited = [False for _ in range(n)]

    q.put(start)
    visited[start] = True

    while not q.empty():
        vertex = q.get()
        vertex_list = graph[vertex]

        for u in vertex_list:
            if end == u :
                return True
            q.put(u)
            visited[u] = True

    return False
