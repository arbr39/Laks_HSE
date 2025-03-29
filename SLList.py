class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# длина цикла
def cycle_length(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:  # поймали
            cnt = 1
            slow = slow.next
            while slow != fast:
                slow, cnt = slow.next, cnt + 1
            return cnt
    return 0  # нет цикла

# середина списка
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow.val  # нашли середину

# k-й элемент с конца
def kth_from_end(head, k):
    slow = fast = head
    for _ in range(k):
        if not fast:
            return None  # короткий список
        fast = fast.next
    while fast:
        slow, fast = slow.next, fast.next
    return slow.val  # вот он