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


def sortStack(stack):
    rack = Stack()
    rack.push(stack.peek())
    stack.pop()

    while not stack.isEmpty():
        if stack.peek() < rack.peek():
            temp = stack.peek()
            stack.pop()
            num_swaps = 0
            while temp < rack.peek():
                num_swaps += 1
                stack.push(rack.peek())
                rack.pop()
            rack.push(temp)
            for i in range(0, num_swaps):
                rack.push(stack.peek())
                stack.pop()
        else:
            rack.push(stack.peek())
            stack.pop()
    while not rack.isEmpty():
        stack.push(rack.peek())
        rack.pop()

    return(stack)


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
    stack = Stack()
    stack.push(-1)
    stack.push(3)
    stack.push(4)
    stack.push(1)
    stack.push(8)
    stack.push(2)
    stack.push(5)
    stack.push(6)

    print_Stack(stack)
    print("\n")
    print_Stack(sortStack(stack))


if __name__ == "__main__":
    main()
