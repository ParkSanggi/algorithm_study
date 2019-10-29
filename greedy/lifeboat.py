def solution(people, limit):
    people = sorted(people, reverse=True)

    answer = 0
    big = 0
    small = len(people) - 1

    while big < small:
        if people[big] + people[small] <= limit:
            small -= 1

        answer += 1
        big += 1

    if big == small:
        answer += 1

    return answer


solution([70, 50, 80, 50], 100)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def add(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#
#     def is_empty(self):
#         if self.head:
#             return False
#         else:
#             return True
#
#
# def solution(people, limit):
#     linked_list = LinkedList()
#
#     for i in sorted(people):
#         linked_list.add(i)
#
#     answer = 0
#
#     while linked_list.head:
#
#         remove_status = False
#
#         previous = None
#         _max = linked_list.head.data
#         linked_list.head = linked_list.head.next
#
#         temp = linked_list.head
#
#         while temp:
#             if _max + temp.data <= limit:
#                 if temp == linked_list.head:
#                     linked_list.head = linked_list.head.next
#                 else:
#                     previous.next = temp.next
#                 answer += 1
#                 remove_status = True
#                 break
#             else:
#                 previous = temp
#                 temp = temp.next
#
#         if not remove_status:
#             answer += 1
#
#     return answer
#
#
# solution([70, 50, 80, 50], 100)
