class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None


def main():

    list = LinkedList()
    list.headval = Node("1")
    list.headval.nextval = Node("2")
    list.headval.nextval.nextval = Node("3")
    list.headval.nextval.nextval.nextval = Node("4")
    list.headval.nextval.nextval.nextval.nextval = Node("5")
    list.headval.nextval.nextval.nextval.nextval.nextval = Node("6")

    # passing node "3"
    chapt2q3(list.headval.nextval.nextval)
    print_list(list.headval)


def chapt2q3(node):
    temp = node.nextval
    node.dataval = temp.dataval
    node.nextval = temp.nextval
    temp = None


def print_list(node):
    if node is not None:
        print(node.dataval)
        print_list(node.nextval)


if __name__ == "__main__":
    main()
