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


# a stack which keeps track of a minimum element
class MinStack:
    def __init__(self):
        self.item_index = 0
        self.array = []
        self.min_stack = Stack()

    def isEmpty(self):
        return(self.item_index == 0)

    def pop(self):
        if not self.isEmpty():
            if self.array[self.item_index - 1] == self.min_stack.peek():
                self.min_stack.pop()
            self.item_index -= 1

    def push(self, item):
        while len(self.array) <= self.item_index:
            self.array.append("")
        if self.min_stack.isEmpty():
            self.min_stack.push(item)
        elif item < self.min_stack.peek():
            self.min_stack.push(item)
        self.array[self.item_index] = item
        self.item_index += 1

    def peek(self):
        if not self.isEmpty():
            return(self.array[self.item_index])
        else:
            return(None)

    def min(self):
        return(self.min_stack.peek())


def main():
    minStack = MinStack()
    minStack.push(0)
    print minStack.min()
    minStack.push(8)
    print minStack.min()
    minStack.push(1)
    minStack.pop()
    minStack.pop()
    minStack.pop()
    minStack.push(1)
    print minStack.min()
    minStack.push(0)
    print minStack.min()
    minStack.push(8)
    print minStack.min()
    minStack.pop()
    print minStack.min()
    minStack.pop()
    print minStack.min()
    minStack.pop()
    print minStack.min()


if __name__ == "__main__":
    main()
