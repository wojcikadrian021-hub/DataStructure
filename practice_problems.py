"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.
"""

def has_duplicates(product_ids):
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)

    return False

# I used a set because it makes it easy to check if an ID was already seen.
# Checking and adding to a set is usually O(1), so the whole function is O(n).


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added,
and support removing tasks from the front.
"""

from collections import deque

class TaskQueue:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if len(self.tasks) == 0:
            return None

        return self.tasks.popleft()

# I used a queue because the first task added should be the first one removed.
# Adding and removing items with deque is usually O(1).


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point,
you should be able to return the number of unique values seen so far.
"""

class UniqueTracker:
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)

# I used a set because sets automatically ignore duplicate values.
# Adding values and checking the size are usually O(1).
