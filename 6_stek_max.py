class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print('error')

    def get_max(self):
        if self.items:
            print(max(self.items))
        else:
            print('None')


stack = StackMax()


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
