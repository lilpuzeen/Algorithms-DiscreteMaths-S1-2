class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x: str):
        self.items.append(x)

    def dequeue(self):
        return self.items.pop(0)

    def insert_in_middle(self, x: str):
        self.items.insert((len(self.items) // 2) + 1, x)


if __name__ == '__main__':
    n = int(input())
    my_queue = Queue()
    for i in range(n):
        command = [x for x in input().split()]
        if command[0] == "+":
            my_queue.enqueue(str(command[1]))
        elif command[0] == "-":
            print(my_queue.dequeue())
        elif command[0] == "*":
            my_queue.insert_in_middle(str(command[1]))
