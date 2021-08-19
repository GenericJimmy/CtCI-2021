class Stack:
    def __init__(self):
        self.item_index = 0
        self.array = []

    def isEmpty(self):
        return(self.item_index == 0)

    def pop(self):
        if not self.isEmpty():
            self.item_index -= 1

    def push(self, item):
        while len(self.array) <= self.item_index:
            self.array.append("")
        self.array[self.item_index] = item
        self.item_index += 1

    def peek(self):
        if not self.isEmpty():
            return(self.array[self.item_index-1])
        else:
            return(None)


# a queue composed of two stacks, wooden-block-stacking-puzzle style
class Queue:
    def __init__(self):
        self.just_enqueued = True
        self.length = 0
        self.stack = Stack()
        self.buffer = Stack()

    def isEmpty(self):
        return(self.stack.isEmpty() and self.buffer.isEmpty())

    def enqueue(self, item):
        if not self.just_enqueued:
            while not self.buffer.isEmpty():
                self.stack.push(self.buffer.peek())
                self.buffer.pop()
        self.just_enqueued = True
        self.stack.push(item)

    def dequeue(self):
        if not self.isEmpty():
            if self.just_enqueued:
                while not self.stack.isEmpty():
                    self.buffer.push(self.stack.peek())
                    self.stack.pop()
                self.stack.pop()
                self.just_enqueued = False
            else:
                self.buffer.pop()

    def peek(self):
        if self.just_enqueued:
            while not self.stack.isEmpty():
                self.buffer.push(self.stack.peek())
                self.stack.pop()
            self.just_enqueued = False
            return(self.buffer.peek())
        else:
            return(self.buffer.peek())


def print_Stack(stack):
    copy = Stack()
    while not stack.isEmpty():
        print(stack.peek())
        copy.push(stack.peek())
        stack.pop()

    while not copy.isEmpty():
        stack.push(copy.peek())
        copy.pop()


def main():
    foo = Queue()
    print(foo.peek())
    foo.dequeue()
    print(foo.peek())
    foo.enqueue('a')
    print(foo.peek())
    foo.enqueue('b')
    print(foo.peek())
    foo.enqueue('c')
    print(foo.peek())
    foo.dequeue()
    print(foo.peek())
    foo.dequeue()
    print(foo.peek())
    foo.dequeue()
    print(foo.peek())


if __name__ == "__main__":
    main()
