"""
무게가 다른 짐들이 있고
무게가 제한된 트럭이 있다.

짐들을 모두 다른 곳으로 옮기기 위해 필요한 트럭의 대수를 구하세요.
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def is_empty(self):

        if self.head:
            return False
        else:
            return True


load_count, max_weight = map(int, input().split())
number_list = sorted([n for n in map(int, input().split(' '))])

linked_list = LinkedList()

# 정렬의 부담없이 이동이 완료된 짐들을 제거하기 위해 연결리스트 사용
for i in number_list:
    linked_list.add(i)

truck_count = 0


while linked_list.head:

    _sum = 0

    previous = None
    temp = linked_list.head

    # 무게가 높은 순서로 트럭에 대입해서 제한된 무게에 도달 했는지 확인
    while _sum < max_weight:

        # 트럭이 꽉차지 않았다면 다음 짐의 무게를 확인
        if _sum + temp.data < max_weight:
            _sum += temp.data

            if temp.next:
                if temp == linked_list.head:
                    temp = temp.next
                    linked_list.head = linked_list.head.next
                else:
                    previous.next = temp.next

            # 짐들을 다 확인 했다면 트럭 카운트를 올리고 다음 트럭에 실을 짐을 확인
            else:
                if not linked_list.head.next:
                    linked_list.head = None
                break

        # 꽉 찼다면 트럭을 보내고 다음 트럭에 실을 짐을 확인
        elif _sum + temp.data == max_weight:
            if temp.next:
                if temp == linked_list.head:
                    temp = temp.next
                    linked_list.head = linked_list.head.next
                    break

                else:
                    previous.next = temp.next
                    break
            else:
                if not linked_list.head.next:
                    linked_list.head = None
                break
        #  해당 지금 실을 수 없다면 다음 짐을 확인
        else:
            if temp.next:
                previous = temp
                temp = temp.next
            else:
                break

    truck_count += 1

print(truck_count)
