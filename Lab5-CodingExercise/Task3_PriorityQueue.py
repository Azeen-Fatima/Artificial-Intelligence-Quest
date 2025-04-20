class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        # Create a tuple (priority, item)
        new_element = (priority, item)
        inserted = False

        # Insert the new element based on priority
        for i in range(len(self.queue)):
            if self.queue[i][0] > priority:
                self.queue.insert(i, new_element)
                inserted = True
                break
        
        # If not inserted, it has the lowest priority, so append at the end
        if not inserted:
            self.queue.append(new_element)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)[1]  # remove the element with highest priority (lowest number)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0][1]  # look at the element with highest priority

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue content (from highest to lowest priority):")
        for priority, item in self.queue:
            print(f"{item} (Priority: {priority})")

# Example usage
pq = PriorityQueue()
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)

pq.display()

print("\nDequeued item:", pq.dequeue())
pq.display()

