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
        if len(self.history)==0:
            return
        temp = self.history.pop()
        self.status = 1
        if temp[0]=='+':
            self.subtract(temp[1])
        elif temp[0]=='-':
            self.add(temp[1])
        self.status = 0
        self.redos.append(temp)

        

    def redo(self):
        if len(self.redos)==0:
            return
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
        



