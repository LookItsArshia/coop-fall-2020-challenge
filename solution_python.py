class EventSourcer():
    # Do not change the signature of any functions


    def __init__(self):
        self.value = 0
        self.history = []
        self.redo = []



    def add(self, num: int):
        self.value += num
        self.history.append(['+',num])
        print(self.value)
        

    def subtract(self, num: int):
        self.value -= num
        self.history.append(['-',num])
        

    def undo(self):
        temp = self.history.pop()
        if temp[0]=='+':
            self.subtract(temp[1])
        else:
            self.add(temp[1])
        self.redo.append(temp)

        

    def redo(self):
        temp = self.redo.pop(0)
        if temp[0]=='+':
            self.add(temp[1])
        else:
            self.subtract(temp[1])

        

    def bulk_undo(self, steps: int):
        i = 0
        for i in range(steps):
            self.undo()
        

    def bulk_redo(self, steps: int):
        i = 0
        for i in range(steps):
            self.redo()
        



value = EventSourcer()
value.add(3)
value.undo()
value.add(7)
value.subtract((3))
value.bulk_undo(2)
value.add(12)
