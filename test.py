from threadings import PriorityQueueMessageQueue, ThreadPool, payment_processing, inventory_management, shipping, order_placement


def test_priority_queue_message_queue():
    priority_message_queue = PriorityQueueMessageQueue()
    priority_message_queue.enqueue_message("Order 1", "payment")
    priority_message_queue.enqueue_message("Order 2", "inventory")
    priority_message_queue.enqueue_message("Order 3", "shipping")
    priority_message_queue.enqueue_message("Order 4", "inventory")
    assert priority_message_queue.peek_message() == ("inventory", "Order 2")
    assert priority_message_queue.dequeue_message() == ("inventory", "Order 2")
    assert priority_message_queue.peek_message() == ("inventory", "Order 4")
    assert priority_message_queue.dequeue_message() == ("inventory", "Order 4")
    assert priority_message_queue.peek_message() == ("payment", "Order 1")
    assert priority_message_queue.dequeue_message() == ("payment", "Order 1")
    assert priority_message_queue.peek_message() == ("shipping", "Order 3")
    assert priority_message_queue.dequeue_message() == ("shipping", "Order 3")
    assert priority_message_queue.is_empty() == True






def test_payment_processing():
    payment_processing("Order 1")
    
def test_inventory_management():
    inventory_management("Order 2")

def test_shipping():
    shipping("Order 3")

def test_order_placement():
    order_placement("Order 4", "inventory")


def test_thread_pool():
    thread_pool = ThreadPool(3)
    thread_pool.submit_task(payment_processing("Order 1"))
    thread_pool.submit_task(inventory_management("Order 2"))
    thread_pool.submit_task(shipping("Order 3"))
    thread_pool.shutdown()
   

