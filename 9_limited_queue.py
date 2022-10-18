class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    lim_queue = Queue(m)
    for i in range(n):
        command = input()
        if command == 'peek':
            print(lim_queue.queue[lim_queue.head])
        elif command == 'size':
            print(lim_queue.size)
        elif command == 'pop':
            print(lim_queue.pop())
        elif command.split()[0] == 'push':
            lim_queue.push(int(command.split()[1]))
