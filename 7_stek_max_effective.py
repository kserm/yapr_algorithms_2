class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        if len(self.items) == 0:
            self.max.append(item)
        elif item > self.max[-1]:
            self.max.append(item)
        else:
            self.max.append(self.max[-1])
        self.items.append(item)

    def pop(self):
        if self.items:
            self.max.pop()
            return self.items.pop()
        else:
            print('error')

    def get_max(self):
        if self.max:
            print(self.max[-1])
        else:
            print('None')


stack = StackMaxEffective()


def command_parser(command):
    # obj = StackMax()
    if command == 'get_max':
        stack.get_max()
    elif command == 'pop':
        stack.pop()
    else:
        if command.split()[0] == 'push':
            stack.push(int(command.split()[1]))


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        command_parser(input())
