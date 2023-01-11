class LinkedList_Element():
    def __init__(self, next=None):
        self.next = next


class LinkedList():
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.count = 0

    def append(self, item):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = item
            self.tail = item
        else:
            self.head = item
            self.tail = item

        self.count += 1

    def insert(self, item, index: int):
        if index == 0:
            item.next = self.head.next
            self.head = item

        current = self.head
        prev = None
        position = 0

        while current.next:
            if index == position:
                prev.next = item
                item.next = current
                self.count += 1
                print(f"Inserted at position {position}")
            else:
                prev = current
                current = current.next
                position += 1

        if index == position:
            prev.next = item
            item.next = current
            self.count += 1
            print(f"Inserted at position {position}")

    def get_index(self, item) -> int:
        if self.head == item:
            return 1

        current = self.head
        position = 0

        while current.next:
            if current == item:
                return position
            else:
                current = current.next
                position += 1

        if current == item:
            return position
        else:
            return -1

    def remove_tail(self) -> LinkedList_Element:
        current = self.head

        while current.next:
            if current.next == self.tail:
                temp = self.tail
                current.next = None
                self.tail = None
                self.count -= 1
                return temp
            else:
                current = current.next

        if current.next == self.tail:
            temp = self.tail
            current.next = None
            self.tail = None
            self.count -= 1
            return temp

        return None