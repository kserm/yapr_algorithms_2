# 70872516
from operator import add, sub, mul, floordiv

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def pop_first(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def calculator(arr: Stack) -> int:
    results_array = Stack()
    while arr.size() > 0:
        i = arr.pop_first()
        if i in OPERATORS:
            b = int(results_array.pop())
            a = int(results_array.pop())
            results_array.push(OPERATORS[i](a, b))
        else:
            results_array.push(i)
    return results_array.peek()


def main():
    input_stack = Stack()
    for i in input().split():
        input_stack.push(i)
    print(calculator(input_stack))


if __name__ == '__main__':
    main()
