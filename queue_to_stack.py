"""
Queue to stack converter.
"""

from arraystack import ArrayStack    # or from linkedstack import LinkedStack


def queue_to_stack(queue):
    """
    Returns a stack with the same contents as the queue.
    The queue is left intact.
    """
    stack = ArrayStack()
    queue_list = [item for item in queue][::-1]
    for item in queue_list:
        stack.add(item)
    return stack
