"""
Stack to queue converter.
"""

from arrayqueue import ArrayQueue   # or from linkedqueue import LinkedQueue


def stack_to_queue(stack):
    """
    Returns a queue with the same contents as the stack.
    The stack is left intact.
    """
    queue = ArrayQueue()
    queue_list = [item for  item in stack][::-1]
    # print(queue_list)
    for item in queue_list:
        queue.add(item)
    return queue
