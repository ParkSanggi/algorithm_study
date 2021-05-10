# 정렬되어 있지 않은 연결리스트에서 중복되는 원소를 제거하세요.


# 연결리스트를 순회하면서 딕셔너리에 Node의 data를 담아두고
# data 값의 key가 존재하면 노드를 삭제
def remove_duplication1(node):
    compare_table = {}
    previous = None

    while node:
        if node.data in compare_table:
            previous.next = node.next
        else:
            compare_table[node.data] = 1

        previous = node
        node = node.next


# 다른 자료구조를 사용할 수 없는 경우 연결리스트 내에서 두개의 포인터를 사용해서
# 중복는 원소가 있는지 확인
def remove_duplication2(head):
    cur = head

    while cur:
        runner = cur

        while runner.next:
            if cur.data == runner.next.data:
                runner.next = runner.next.next
            else:
                runner = runner.next

        cur = cur.next
