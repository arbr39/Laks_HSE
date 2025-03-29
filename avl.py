class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.height = 1

def height(n):
    return n.height if n else 0

def balance_factor(n):
    return height(n.left) - height(n.right) if n else 0

def update_height(n):
    n.height = 1 + max(height(n.left), height(n.right))

def rotate_right(y):  # вправо
    x = y.left
    y.left, x.right = x.right, y
    update_height(y)
    update_height(x)
    return x

def rotate_left(x):  # влево
    y = x.right
    x.right, y.left = y.left, x
    update_height(x)
    update_height(y)
    return y

def rebalance(node):
    update_height(node)
    bf = balance_factor(node)
    if bf > 1:  # левый случай
        if balance_factor(node.left) < 0:
            node.left = rotate_left(node.left)  # LR
        return rotate_right(node)  # LL
    if bf < -1:  # правый случай
        if balance_factor(node.right) > 0:
            node.right = rotate_right(node.right)  # RL
        return rotate_left(node)  # RR
    return node

def insert(node, key):
    if not node:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return rebalance(node)

def min_value_node(node):
    while node.left:
        node = node.left
    return node

def delete(node, key):
    if not node:
        return node
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:  # нашли узел
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        else:
            temp = min_value_node(node.right)
            node.key = temp.key
            node.right = delete(node.right, temp.key)
    return rebalance(node)

def search(node, key):
    if not node:
        return False
    if key == node.key:
        return True
    return search(node.left, key) if key < node.key else search(node.right, key)