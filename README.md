# PythonThreading
AI Planet assignment

Overview

This code implements a system for processing orders with different priorities concurrently using Python's threading and queue modules. It is designed to simulate an order management system where orders are processed based on their priority (payment, inventory, or shipping) and executed in parallel using a thread pool.


Key Components

PriorityQueueMessageQueue:
This class manages a priority queue using Python's queue.PriorityQueue class. Orders are added to the queue along with their priority, and can be dequeued based on priority.

ThreadPool:
This class creates a thread pool with a specified number of threads. Each thread runs a worker function that consumes tasks from a shared task queue and executes them. The thread pool allows for concurrent processing of orders.

payment_processing, inventory_management, shipping:
These functions simulate different order processing tasks such as payment, inventory management, and shipping. They print out the order details and simulate a processing delay using time.sleep.

order_placement:
This function adds an order to the priority queue based on its priority and submits a task to the thread pool for processing.

process_order:
This function dequeues an order from the priority queue and processes it based on its priority.


Usage

Initialization:
Create instances of PriorityQueueMessageQueue and ThreadPool.

Order Placement:
Use the order_placement function to add orders to the priority queue with their respective priorities.

Processing Orders:
Call process_order function which processes orders based on their priority, simulating different tasks such as payment processing, inventory management, and shipping.
