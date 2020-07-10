class EventSourcer():
    # Do not change the signature of any functions


    def __init__(self):
        self.value = 0
        self.history = []
        self.redos = []
        self.status = 0



    def add(self, num: int):
        self.value += num
        if self.status==0:
            self.history.append(['+',num])
        

    def subtract(self, num: int):
        self.value -= num
        if self.status==0:
            self.history.append(['-',num])
        
        

    def undo(self):
        
        temp = self.history.pop()
        self.status = 1
        if temp[0]=='+':
            self.subtract(temp[1])
        elif temp[0]=='-':
            self.add(temp[1])
        self.status = 0
        self.redos.append(temp)

        

    def redo(self):

        temp = self.redos.pop(0)
        if temp[0]=='+':
            self.add(temp[1])
        else:
            self.subtract(temp[1])

        

    def bulk_undo(self, steps: int):
        i = 0
        for i in range(min(len(self.history),steps)):
            self.undo()
        

    def bulk_redo(self, steps: int):
        i = 0
        for i in range(min(len(self.redos),steps)):
            self.redo()
        



# value = EventSourcer()
# value.add(3)
# value.undo()
# value.redo()
# value.add(7)
# value.add((3))
# value.bulk_undo(2)
# value.bulk_redo(2)
# value.subtract(4)
# value.undo()
# value.add(3)
# value.add(23)
# value.bulk_redo(3)
# value.bulk_undo(4)

# # value.add(12)
# print(value.value)