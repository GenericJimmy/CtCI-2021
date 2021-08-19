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


# a stack of many smaller stacks of limited size
class MultiStack:
    def __init__(self, size_limit=None):
        self.stack_size_limit = size_limit
        self.sub_stack_index = 0
        self.stack_array = []

    def isEmpty(self):
        return(self.sub_stack_index == 0 and self.stack_array[0].isEmpty())

    def pop(self):
        if not self.isEmpty():
            if self.sub_stack_index == 0:  # when we're on the last stack
                self.stack_array[self.sub_stack_index].pop()
                if self.stack_array[self.sub_stack_index].isEmpty():
                    self.sub_stack_index -= 1
            else:  # every other stack
                self.stack_array[self.sub_stack_index - 1].pop()
                if self.stack_array[self.sub_stack_index - 1].isEmpty():
                    self.sub_stack_index -= 1
        if self.sub_stack_index < 0:
            self.sub_stack_index = 0

    def push(self, item):
        while len(self.stack_array) <= self.sub_stack_index:
            self.stack_array.append(Stack())  # when we dont have enough stacks
        self.stack_array[self.sub_stack_index].push(item)
        if self.stack_array[self.sub_stack_index].item_index == self.stack_size_limit:
            self.sub_stack_index += 1

    def peek(self):
        if not self.isEmpty():
            if self.sub_stack_index == 0:
                return(self.stack_array[self.sub_stack_index].peek())
            return(self.stack_array[self.sub_stack_index - 1].peek())
        else:
            return(None)


def main():
    multiStack = MultiStack(4)  # each sub stack can have four elements
    print multiStack.sub_stack_index
    multiStack.push(1)
    multiStack.push(2)
    multiStack.push(3)
    multiStack.push(4)
    print multiStack.sub_stack_index
    print multiStack.peek()
    multiStack.push('a')
    multiStack.push('b')
    multiStack.push('c')
    multiStack.push('d')
    print multiStack.sub_stack_index
    print multiStack.peek()
    multiStack.pop()
    multiStack.pop()
    multiStack.pop()
    multiStack.pop()
    print multiStack.peek()
    multiStack.pop()
    multiStack.pop()
    multiStack.pop()
    multiStack.pop()
    print multiStack.peek()


if __name__ == "__main__":
    main()
