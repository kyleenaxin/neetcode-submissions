class LinkedList:
    
    def __init__(self):
        self.list = []
        self.length = len(self.list)
        # if self.length > 0:
        #     self.head = 0
        #     self.tail = self.list[self.length - 1]
    
    def get(self, index: int) -> int:
        if index > self.length - 1 or index < 0:
            return -1
        else:
            return self.list[index]

    def insertHead(self, val: int) -> None:
        if self.length == 0:
            self.list.append(val)
        else:
            self.list.insert(0, val)
        self.length += 1

    def insertTail(self, val: int) -> None:
        self.list.append(val)
        self.length += 1
        
    def remove(self, index: int) -> bool:
        if index > self.length - 1 or index < 0:
            return False
        else:
            self.list.pop(index)
            self.length -= 1
            return True
        

    def getValues(self) -> List[int]:
        return self.list
        
