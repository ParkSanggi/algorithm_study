# 스택에서 min함수를 통해 O(1)로 최소값 찾기


class Stack:
    def __init__(self):
        self.container = list()

        # 최소값을 담아두기 위한 컨테이너
        self.min_container = list()

    def push(self, data):
        self.container.append(data)

        # 최소값 갱신
        if not self.min_container or data < self.min_container[-1]:
            self.min_container.append(data)

    def pop(self):
        pop_data = self.container.pop()

        # 삭제되는 데이터가 최소값이라면 최소값을 갱신
        if pop_data == self.min_container[-1]:
            self.min_container.pop()

        return pop_data

    def _min(self):
        if not self.min_container:
            return None

        return self.min_container[-1]
