############Implementing the dequeue in python using list#####################


class Dequee:
    def __init__(self):
        self.dequeue = []
        self.size=0
        
    def insertFront(self,x):
        self.dequeue    