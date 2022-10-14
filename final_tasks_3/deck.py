# 70916820
class StackIsFullException(Exception):
    def __init__(self):
        pass


class StackIsEmptyException(Exception):
    def __init__(self):
        pass


class Deque:
    def __init__(self, n):
        self.__queue = [None] * n
        self.__max_n = n
        self.__tail = 0
        self.__head = 0
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def is_full(self):
        return self.__size == self.__max_n

    def push_front(self, value):
        if self.is_full():
            raise StackIsFullException()
        self.__queue[self.__head-1] = value
        self.__head = (self.__head - 1) % self.__max_n
        self.__size += 1

    def push_back(self, value):
        if self.is_full():
            raise StackIsFullException()
        self.__queue[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_n
        self.__size += 1

    def pop_front(self):
        if self.is_empty():
            raise StackIsEmptyException()
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_n
        self.__size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            raise StackIsEmptyException()
        position = (self.__tail - 1) % self.__max_n
        x = self.__queue[position]
        self.__queue[position] = None
        self.__tail = position
        self.__size -= 1
        return x


def run_deque_method(deque, command):
    cmd, *args = command.split()
    action = getattr(Deque, cmd)
    try:
        return action(deque) if not args else action(deque, args[0])
    except (StackIsEmptyException, StackIsFullException):
        return 'error'


def main():
    n = int(input())
    m = int(input())
    q = Deque(m)
    for i in range(n):
        command = input()
        result = run_deque_method(q, command)
        if result:
            print(result)


if __name__ == '__main__':
    main()
