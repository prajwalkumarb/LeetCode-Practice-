class CreateNode():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListTest():
    def __init__(self,value):
        new_node = CreateNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(f"[Temp val] -- {temp.value}")
            temp = temp.next
    
    def append(self,value):
        new_node = CreateNode(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
    
    def prepend(self,value):
        new_node = CreateNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
    
    def get(self,index):
        if self.head is None or index > self.length :
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index > self.length:
            return self.append(value)
        temp = self.get(index - 1)
        new_node = CreateNode(value)
        if temp:
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
        
    def remove(self,index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for i in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
if __name__ == "__main__":
    linked_list = LinkedListTest(10)
    # print(f"Head ------- value : {linked_list.head.value} next : {linked_list.head.next}")
    # print(f"Tail ------- value : {linked_list.tail.value} next : {linked_list.tail.next}")
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    linked_list.print_list()
    print("***************************")
    linked_list.pop()
    linked_list.append(40)
    linked_list.prepend(0)
    linked_list.pop_first()
    linked_list.print_list()
    print("^^^^^^^^^^^^^^^^^^^^^^^^")
    linked_list.set_value(2,99)
    linked_list.print_list()
    print("&&&&&&&&&&&&&&&&&&&&&")
    linked_list.remove(1)
    linked_list.print_list()
    print("*%%%%%%%%%%%%%%%%%")
    linked_list.reverse()
    linked_list.print_list()
