class ListQueue:
    def __init__(self) -> None:
        self.array = []

    def size(self):
        return len(self.array)

    def get(self):
        if self.size() == 0:
            return 'error'
        else:
            if self.array:
                return self.array.pop(0)

    def put(self, x):
        self.array.append(x)


if __name__ == '__main__':
    n = int(input())
    q = ListQueue()
    for i in range(n):
        command = input()
        if command == 'size':
            print(q.size)
        elif command == 'get':
            print(q.get())
        elif command.split()[0] == 'put':
            q.put(command.split()[1])
