class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,x):
        self.queue.append(x)
        print("Pushed", x ,"in Queue")
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue)==0
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"
    def display(self):
        print("Queue: ", self.queue)

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("\n")
q.dequeue()
q.display()
print("\n")
print("Front elemet is ", q.front())

