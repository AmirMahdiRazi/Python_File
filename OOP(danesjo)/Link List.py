class Node():
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class Link_list:
    def __init__(self) -> None:
        self.head=None
    
    def insert_First(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_End(self, data):
        if self.head is None:
            print("Empty")
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        new_node = Node(data)
        temp.next = new_node

    def insert_between(self,value_between,data):
        """if Node_beteen is None:
            print("Pls Enter true Node")
            return"""
        temp=self.head
        while(temp):
            if temp.data == value_between:
                break
            temp = temp.next
        if temp is None:
                print("not find")
                return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        #print(Node_between.next.data)
    
    def Travel(self):
        temp=self.head
        #print(self.head)
        while(temp):
            print(temp.data)
            temp = temp.next

Li = Link_list()
#Li.insert_End(2)
Li.insert_First(1)
second=Node(2)
Li.head.next = second
third=Node(3)
Li.head.next.next = third
Li.insert_between(5,4)
Li.Travel()
#print(Li.head.next.data)

"""for _ in range(2,10):
    Nodelast = Node(_-1)
    #print(Nodelast.data)
    Li.insert_between(Nodelast,_)"""
#Li.Travel()
        