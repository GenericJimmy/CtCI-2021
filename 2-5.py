class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None


def main():

    # number 11
    list1 = LinkedList()
    list1.headval = Node(1)
    list1.headval.nextval = Node(1)

    # number 89
    list2 = LinkedList()
    list2.headval = Node(9)
    list2.headval.nextval = Node(8)

    print_list(chapt2q5(list1, list2))


def chapt2q5(list1, list2):
    num1 = list1.headval
    num2 = list2.headval
    sum = LinkedList()

    carry = 0
    working_Value = num1.dataval + num2.dataval + carry
    sum.headval = Node(working_Value % 10)
    carry = working_Value // 10

    num1 = num1.nextval
    num2 = num2.nextval
    sum_Index = sum.headval

    while not (num1 is None and num2 is None):

        # if we reach the end of one list, keep parsing through the other
        if num1 is None:
            working_Value = num2.dataval + carry
            sum_Index.nextval = Node(working_Value % 10)
            carry = working_Value // 10
            num2 = num2.nextval
            sum_Index = sum_Index.nextval
        elif num2 is None:
            working_Value = num1.dataval + carry
            sum_Index.nextval = Node(working_Value % 10)
            carry = working_Value // 10
            num1 = num1.nextval
            sum_Index = sum_Index.nextval

        # otherwise we parse both lists
        else:
            working_Value = num1.dataval + num2.dataval + carry
            sum_Index.nextval = Node(working_Value % 10)
            carry = working_Value // 10
            num1 = num1.nextval
            num2 = num2.nextval
            sum_Index = sum_Index.nextval
    if carry == 1:
        sum_Index.nextval = Node(carry)
    return(sum.headval)


def print_list(node):
    if node is not None:
        print(node.dataval)
        print_list(node.nextval)


if __name__ == "__main__":
    main()
