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

    print(chapt2q2(list, 6))
    print(chapt2q2(list, 5))
    print(chapt2q2(list, 3))
    print(chapt2q2(list, 2))
    print(chapt2q2(list, 1))
    print(chapt2q2(list, 0))
    print(chapt2q2(list, -1))


def chapt2q2(list, k):
    current = list.headval
    if k <= 0:
        offset = None
    else:
        offset = list.headval
        for i in range(0, k):
            if offset is not None:
                offset = offset.nextval
    return(chapt2q2_Helper(current, offset))


def chapt2q2_Helper(current, offset):
    if offset is None:
        return(current.dataval)
    else:
        return(chapt2q2_Helper(current.nextval, offset.nextval))


if __name__ == "__main__":
    main()
