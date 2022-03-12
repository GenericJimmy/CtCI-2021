class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None


def main():

    list = LinkedList()
    list.headval = Node("a")
    list.headval.nextval = Node("b")
    list.headval.nextval.nextval = Node("a")
    list.headval.nextval.nextval.nextval = Node("a")
    list.headval.nextval.nextval.nextval.nextval = Node("c")
    list.headval.nextval.nextval.nextval.nextval.nextval = Node("b")

    chapt2q1alt(list)
    print_list(list.headval)


def chapt2q1(list):
    dict = {}
    current = list.headval

    while current is not None:
        dict[current.dataval] = False
        current = current.nextval

    current = list.headval
    while current is not None:
        dict[current.dataval] = True
        if current.nextval is not None and \
           dict[current.nextval.dataval] is True:
            temp = current.nextval
            current.nextval = None
            current.nextval = temp.nextval
        elif current.nextval is None and dict[current.dataval] is True:
            current = None
        else:
            current = current.nextval


def chapt2q1alt(list):
    # with no temporary buffer
    dict = {}
    current = list.headval

    while current is not None:
        dict[current.dataval] = False
        current = current.nextval

    prev = list.headval
    current = prev.nextval
    while prev is not None:
        dict[prev.dataval] = True
        if current is not None and dict[current.dataval] is True:
            prev.nextval = current.nextval
            current = None
            current = prev.nextval
        elif current is None and dict[prev.dataval] is True:
            prev = None
        else:
            prev = prev.nextval
            current = current.nextval


def print_list(node):
    if node is not None:
        print(node.dataval)
        print_list(node.nextval)


if __name__ == "__main__":
    main()
