"""Stacks and queues module.

This module contains implementations of:
- Stack (LIFO) using both arrays and linked lists
- Queue (FIFO) using both arrays and linked lists
- Deque (double-ended queue)

TODO:
    - Implement Stack with array backend
    - Implement Stack with linked list backend
    - Implement Queue with array backend (using circular queue optimization)
    - Implement Queue with linked list backend
    - Implement Deque
"""

from . import deque, queue_array, queue_linked_list, stack_array, stack_linked_list

__all__ = [
    "stack_array",
    "stack_linked_list",
    "queue_array",
    "queue_linked_list",
    "deque",
]
