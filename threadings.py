

import threading
import queue
import time

class PriorityQueueMessageQueue:
    def __init__(self):
        self.queue = queue.PriorityQueue()

    def enqueue_message(self, message, priority):
        self.queue.put((priority, message))

    def dequeue_message(self):
        return self.queue.get()

    def peek_message(self):
        # Get the highest priority message from the queue without removing it
        message = self.queue.get()
        self.queue.put(message)  # Put the message back into the queue
        return message

    def is_empty(self):
        return self.queue.empty()


class ThreadPool:
    def __init__(self, num_threads):
        self.thread_pool = []
        self.tasks = queue.Queue()

        for _ in range(num_threads):
            thread = threading.Thread(target=self.worker)
            thread.daemon = True
            thread.start()
            self.thread_pool.append(thread)

    def worker(self):
        while True:
            task = self.tasks.get()
            if task is None:
                break
            task()

    def submit_task(self, task):
        self.tasks.put(task)

    def shutdown(self):
        for _ in self.thread_pool:
            self.tasks.put(None)
        for thread in self.thread_pool:
            thread.join()


# Create instances of priority message queue and thread pool
priority_message_queue = PriorityQueueMessageQueue()
thread_pool = ThreadPool(3)  # 3 threads for concurrent processing

def payment_processing(order_details):
    print(f"Processing payment for order: {order_details}")
    time.sleep(1)  # Simulating payment processing time
    print(f"Payment processed for order: {order_details}")

def inventory_management(order_details):
    print(f"Updating inventory for order: {order_details}")
    time.sleep(2)  # Simulating inventory update time
    print(f"Inventory updated for order: {order_details}")

def shipping(order_details):
    print(f"Preparing shipment for order: {order_details}")
    time.sleep(3)  # Simulating order preparation time
    print(f"Shipment prepared for order: {order_details}")

def order_placement(order_details, priority):
    priority_message_queue.enqueue_message(order_details, priority)
    if not priority_message_queue.is_empty():
        thread_pool.submit_task(process_order)

def process_order():
    priority, message = priority_message_queue.dequeue_message()
    if priority == "payment":
        payment_processing(message)
    elif priority == "inventory":
        inventory_management(message)
    elif priority == "shipping":
        shipping(message)



# Simulate order placements with different priorities
order_placement("Order 1", "payment")
order_placement("Order 2", "inventory")
order_placement("Order 3", "shipping")
order_placement("Order 4", "inventory")

# Wait for all orders to be processed
thread_pool.shutdown()





