class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None


def main():

    list1 = LinkedList()
    list1.headval = Node("a")
    list1.headval.nextval = Node(10)
    list1.headval.nextval.nextval = Node(10)
    list1.headval.nextval.nextval.nextval = Node("a")

    list2 = LinkedList()
    list2.headval = Node("a")
    list2.headval.nextval = Node("b")
    list2.headval.nextval.nextval = Node("b")
    list2.headval.nextval.nextval.nextval = Node("a")

    list3 = LinkedList()
    list3.headval = Node("a")
    list3.headval.nextval = Node("b")
    list3.headval.nextval.nextval = Node("c")
    list3.headval.nextval.nextval.nextval = Node(1)
    list3.headval.nextval.nextval.nextval.nextval = Node(2)
    list3.headval.nextval.nextval.nextval.nextval.nextval = Node(3)

    print(chapt2q6(list1))
    print(chapt2q6(list2))
    print(chapt2q6(list3))


def chapt2q6(list):
    current = list.headval
    mirror_List = LinkedList()
    mirror_List.headval = Node(current.dataval)
    current = current.nextval
    list_length = 0

    while current is not None:
        temp = Node(current.dataval)
        temp.nextval = mirror_List.headval
        mirror_List.headval = temp
        current = current.nextval
        list_length += 1

    current = list.headval
    mirror = mirror_List.headval
    for i in range(0, list_length/2 + 1):
        if current.dataval != mirror.dataval:
            return(False)
        current = current.nextval
        mirror = mirror.nextval
    return(True)


if __name__ == "__main__":
    main()
