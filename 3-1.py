class TripleStack:
    def __init__(self):
        self.first_item_index = -3
        self.second_item_index = -2
        self.third_item_index = -1
        self.array = []

    def isEmpty(self, stack=None):
        if stack == 1:
            return(self.first_item_index == -3)
        elif stack == 2:
            return(self.second_item_index == -2)
        elif stack == 3:
            return(self.third_item_index == -1)
        elif stack is None:
            return(self.isEmpty(1) and self.isEmpty(2) and self.isEmpty(3))
        print("Invalid Stack")

    def pop(self, stack):
        if stack not in {1, 2, 3}:
            print('Invalid Stack')
        elif stack == 1 and not self.isEmpty(1):
            self.first_item_index -= 3
        elif stack == 2 and not self.isEmpty(2):
            self.second_item_index -= 3
        elif stack == 3 and not self.isEmpty(3):
            self.third_item_index -= 3
        else:
            pass

    def push(self, stack, item):
        maxLength = max(self.first_item_index, self.second_item_index, self.third_item_index)
        while len(self.array) - 3 <= maxLength:
            self.array.append("")
        if stack == 1:
            self.first_item_index += 3
            self.array[self.first_item_index] = item
        elif stack == 2:
            self.second_item_index += 3
            self.array[self.second_item_index] = item
        elif stack == 3:
            self.third_item_index += 3
            self.array[self.third_item_index] = item
        else:
            print('Invalid Stack')

    def peek(self, stack):
        if stack not in {1, 2, 3}:
            print('Invalid Stack')
        elif stack == 1 and not self.isEmpty(1):
            return(self.array[self.first_item_index])
        elif stack == 2 and not self.isEmpty(2):
            return(self.array[self.second_item_index])
        elif stack == 3 and not self.isEmpty(3):
            return(self.array[self.third_item_index])
        else:
            return(None)


def main():
    stack = TripleStack()
    print(stack.isEmpty())
    stack.push(1, 1)
    stack.push(2, 2)
    stack.push(3, 3)
    stack.push(1, "1a")
    print stack.peek(1)
    stack.pop(1)
    print stack.peek(1)
    stack.pop(1)
    print stack.peek(1)
    stack.pop(1)
    stack.pop(1)
    print stack.peek(1)
    print stack.peek(2)
    print stack.peek(3)
    print(stack.isEmpty())


if __name__ == "__main__":
    main()
