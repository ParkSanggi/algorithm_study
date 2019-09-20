def solution(phone_book):
    index_kind = {}

    for number in phone_book:
        length = len(number)

        if length not in index_kind:
            index_kind[length] = 1

            equal_count = 0

            for num in phone_book:
                if num[:length] == number:
                    equal_count += 1
                    if equal_count > 1:
                        return False

    return True