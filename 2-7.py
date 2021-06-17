class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None


def main():

    list1 = LinkedList()
    list1.headval = Node("1")
    list1.headval.nextval = Node("2")
    list1.headval.nextval.nextval = Node("3")
    list1.headval.nextval.nextval.nextval = Node("delta")

    list2 = LinkedList()
    list2.headval = Node("a")
    list2.headval.nextval = Node("b")
    list2.headval.nextval.nextval = list1.headval.nextval.nextval

    print(chapt2q7(list1, list2))


def chapt2q7(list1, list2):
    dict = {}
    current1 = list1.headval
    current2 = list2.headval
    while not (current1 is None or current2 is None):
        if current1 not in dict:
            dict[current1] = False

        if current2 not in dict:
            dict[current2] = False

        if dict[current1] is True:
            return(current1.dataval)
        dict[current1] = True

        if dict[current2] is True:
            return(current2.dataval)
        dict[current2] = True

        if current1 is not None:
            current1 = current1.nextval

        if current2 is not None:
            current2 = current2.nextval
    return(False)


if __name__ == "__main__":
    main()
