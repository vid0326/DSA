class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class Dequeue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def appendFront(self, x):  # appendleft
        newNode = Node(x)
        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            newNode.next = self.front
            self.front.prev = newNode
            self.front = newNode
        self.size += 1

    def appendBack(self, x):  # append
        newNode = Node(x)
        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            newNode.prev = self.rear
            self.rear = newNode
        self.size += 1

    def popFront(self):  # popleft
        if self.front is None:
            return "No Element is there"
        else:
            data = self.front.data
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
                self.front.prev = None
        self.size -= 1
        return data

    def popBack(self):  # pop
        if self.rear is None:
            return "No Element is there"
        else:
            data = self.rear.data
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.rear = self.rear.prev
                self.rear.next = None
        self.size -= 1
        return data

    def getFront(self):
        return self.front.data if self.front else "No Element"

    def getRear(self):
        return self.rear.data if self.rear else "No Element"

    def reverse(self):
        if self.front is None or self.rear is None:
            return "No Element is there"

        curr = self.front
        temp = None

        while curr is not None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev

        if temp is not None:
            self.front, self.rear = self.rear, self.front

    def extendLeft(self, lst):
        for x in reversed(lst):
            self.appendFront(x)

    def extend(self, lst):
        for x in lst:
            self.appendBack(x)

    def display(self):
        current = self.front
        result = []
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def rotate(self, x):
        if self.front is None or self.rear is None or self.size <= 1:
            return

        x = x % self.size
        if x == 0:
            return

        if x > 0:
            for _ in range(x):
                data = self.popBack()
                self.appendFront(data)
        else:
            for _ in range(-x):
                data = self.popFront()
                self.appendBack(data)

    def count(self, x):
        curr = self.front
        count = 0
        while curr is not None:
            if curr.data == x:
                count += 1
            curr = curr.next
        return count

    def getElementByIndex(self, x):
        if x < 0 or x >= self.size:
            return "Index out of bounds"

        curr = self.front
        index = 0
        while curr is not None:
            if index == x:
                return curr.data
            curr = curr.next
            index += 1
        return "Index not found"

    def insertAtGivenIndex(self, x, val):
        if x < 0 or x > self.size:
            return "Index out of bounds"

        newNode = Node(val)

        if x == 0:
            self.appendFront(val)
        elif x == self.size:
            self.appendBack(val)
        else:
            current = self.front
            index = 0
            while index < x - 1:  # Traverse to the node just before the target index
                current = current.next
                index += 1
            # Insert the new node
            newNode.next = current.next
            newNode.prev = current
            if current.next:
                current.next.prev = newNode
            current.next = newNode
            self.size += 1


