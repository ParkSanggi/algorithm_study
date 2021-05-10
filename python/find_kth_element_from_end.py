# 연결리스트에서 뒤에서 k번째 원소를 찾으세요.


# 재귀적 방법
def find_element_recursive(k, node):
    if not node:
        return [0, None]

    # 연결리스트의 끝까지 이동
    count_and_element = find_element_recursive(k, node.next)

    # 뒤에서 몇번째인지 카운트
    count_and_element[0] += 1

    # 찾고자 하는 원소라면 데이터의 값을 할당
    if count_and_element[0] == k:
        count_and_element[1] = node.data
        return count_and_element

    # 찾고자 하는 원소가 아니라면 카운트만 반영한 뒤 리턴
    else:
        return count_and_element


# 순환적 방법
# 두개의 포인터를 두고 그 중 하나를 k만큼 미리 이동시켜 놓는다면
# 이동시킨 포인터가 연결리스트의 끝에 도착했을 때 나머지 카운터가 끝에서 k번째 위치에 도달하게 된다.
def find_element_iterative(k, head):
    find_element = head
    find_end = head

    for _ in range(k):
        if not find_end:
            return None
        find_end = find_end.next

    while find_end.next:
        find_element = find_element.next
        find_end = find_end.next

    return find_element.data
