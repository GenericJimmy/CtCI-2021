class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None


def main():

    list = LinkedList()
    list.headval = Node(3)
    list.headval.nextval = Node(5)
    list.headval.nextval.nextval = Node(8)
    list.headval.nextval.nextval.nextval = Node(5)
    list.headval.nextval.nextval.nextval.nextval = Node(10)
    list.headval.nextval.nextval.nextval.nextval.nextval = Node(2)
    list.headval.nextval.nextval.nextval.nextval.nextval.nextval = Node(1)

    chapt2q4(list, 5)
    print_list(list.headval)


def chapt2q4(list, num):
    current = list.headval
    runner = list.headval
    end_node = list.headval

    while end_node.nextval is not None:
        end_node = end_node.nextval

    shift_Nodes(current, runner, end_node, num)


def shift_Nodes(current, runner, end_node, num):
    if runner is None:
        return(None)

    elif current.dataval < num:
        current = current.nextval
        shift_Nodes(current, runner.nextval, end_node, num)

    elif current.dataval >= num:
        move_node_to_end(current, end_node)
        runner = runner.nextval
        shift_Nodes(current, runner.nextval, end_node.nextval, num)


def move_node_to_end(node, end_node):
    end_node.nextval = Node(node.dataval)
    temp = node.nextval
    node.dataval = temp.dataval
    node.nextval = temp.nextval


def print_list(node):
    if node is not None:
        print(node.dataval)
        print_list(node.nextval)


if __name__ == "__main__":
    main()
