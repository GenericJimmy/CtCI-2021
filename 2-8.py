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
    list.headval.nextval.nextval.nextval = Node("delta")
    list.headval.nextval.nextval.nextval.nextval = list.headval.nextval.nextval

    print(chapt2q8(list))


def chapt2q8(list):
    dict = {}
    current = list.headval
    while current is not None:
        if current not in dict:
            dict[current] = False
        if dict[current] is True:
            return(current.dataval)
        dict[current] = True
        current = current.nextval
    return(False)


if __name__ == "__main__":
    main()
