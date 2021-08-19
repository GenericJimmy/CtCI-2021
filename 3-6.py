class Animal:
    def __init__(self, name, type=None):
        self.type = type
        self.name = name

    def isDog(self):
        return(self.type == "dog")

    def isCat(self):
        return(self.type == "cat")


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def isEmpty(self):
        return(self.headval is None)


class AnimalShelter():
    def __init__(self):
        self.arrivalOrder = SLinkedList()

    def enqueue(self, animal):
        if animal.isDog() or animal.isCat():
            if not self.arrivalOrder.isEmpty():
                runner = self.arrivalOrder.headval
                while runner.nextval is not None:
                    runner = runner.nextval
                runner.nextval = Node(animal)
            else:
                self.arrivalOrder.headval = Node(animal)

    def dequeueAny(self, animal=None):
        if animal is None:
            self.dequeueAny(self, self.arrivalOrder.headval.dataval)
        else:
            condition = False
            temp = self.arrivalOrder.headval
            while condition is False:
                if temp is None:
                    condition = True
                elif temp.dataval.type == animal.type:
                    condition = True
                else:
                    temp = temp.nextval
            if temp is not None:
                prev = temp
                temp = temp.nextval
                if temp is not None:
                    prev.dataval = temp.dataval
                    prev.nextval = temp.nextval
                else:
                    prev.dataval = temp
                    prev.nextval = temp
            temp = None
            prev = None

    def dequeueDog(self):
        self.dequeueAny(Animal("", "dog"))

    def dequeueCat(self):
        self.dequeueAny(Animal("", "cat"))


def printList(list):
    temp = list.headval
    while temp is not None:
        if temp.dataval is not None:
            print temp.dataval.name
        temp = temp.nextval


def main():
    dog1 = Animal("dog1", "dog")
    dog2 = Animal("dog2", "dog")
    dog3 = Animal("dog3", "dog")

    cat1 = Animal("cat1", "cat")
    cat2 = Animal("cat2", "cat")
    cat3 = Animal("cat3", "cat")

    shelter = AnimalShelter()
    shelter.enqueue(dog1)
    shelter.enqueue(cat1)
    shelter.enqueue(dog2)
    shelter.enqueue(dog3)
    shelter.enqueue(cat2)
    shelter.enqueue(cat3)

    shelter.dequeueDog()
    printList(shelter.arrivalOrder)
    print"\n"
    shelter.dequeueCat()
    printList(shelter.arrivalOrder)
    print"\n"
    shelter.dequeueCat()
    printList(shelter.arrivalOrder)
    print"\n"
    shelter.dequeueDog()
    printList(shelter.arrivalOrder)
    print"\n"
    shelter.dequeueDog()
    printList(shelter.arrivalOrder)
    print"\n"
    shelter.dequeueDog()
    printList(shelter.arrivalOrder)
    print"\n"
    shelter.dequeueCat()
    printList(shelter.arrivalOrder)
    print"\n"


if __name__ == "__main__":
    main()
