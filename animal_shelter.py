from collections import deque

"""
먼저 들어온 동물이 먼저 나가는 동물 보호소에서
개와 고양이 중 선택해서 데리고 갈 수 있는 자료구조를 만드세요.
"""


class Animal:
    def __init__(self, name):
        self.name = name
        self.order = None

    # 동물들은 보호소에 들어온 순서를 갖는다.
    def set_order(self, order):
        self.order = order

    def get_order(self):
        return self.order

    def is_order_than(self, animal):
        return self.order < animal.get_order()


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class AnimalQueue:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order = 0

    def enqueue(self, animal):
        animal.set_order(self.order)
        self.order += 1

        if isinstance(animal, Dog):
            self.dogs.append(animal)

        if isinstance(animal, Cat):
            self.cats.append(animal)

    def dequeue_any(self):
        if not self.dogs and not self.cats:
            return "보호소에 동물이 없습니다."

        elif not self.dogs:
            return self.dequeue_cat()

        elif not self.cats:
            return self.dequeue_dog()

        # 가장 먼저 나갈 동물들을 확인
        dog = self.dogs[0]
        cat = self.cats[0]

        if dog.is_order_than(cat):
            return self.dequeue_dog()

        else:
            return self.dequeue_cat()

    def dequeue_dog(self):
        return self.dogs.popleft()

    def dequeue_cat(self):
        return self.cats.popleft()
