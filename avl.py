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


# выводим дерево в виде дерева, для наглядности
def print_tree(root, prefix="", is_left=True):
	if not root:
		return ""

	result = ""
	result += print_tree(root.right, prefix + ("│   " if is_left else "    "), False)
	result += prefix + ("└── " if is_left else "┌── ") + str(root.key) + " (h=" + str(root.height) + ", bf=" + str(
		balance_factor(root)) + ")\n"
	result += print_tree(root.left, prefix + ("    " if is_left else "│   "), True)
	return result


# вывод дерева в порядке обхода (in-order)
def inorder_traversal(node, result=None):
	if result is None:
		result = []
	if node:
		inorder_traversal(node.left, result)
		result.append(node.key)
		inorder_traversal(node.right, result)
	return result


# вывод дерева в порядке обхода по уровням (level-order)
def level_order_traversal(root):
	if not root:
		return []

	result = []
	queue = [(root, None)]  # (узел, родитель)

	while queue:
		node, parent = queue.pop(0)
		parent_key = parent.key if parent else None
		result.append((node.key, parent_key))

		if node.left:
			queue.append((node.left, node))
		if node.right:
			queue.append((node.right, node))

	return result


# демонстрация работы
if __name__ == "__main__":
	print("Демонстрация работы AVL-дерева:")

	# создаем пустое дерево
	root = None

	# вставляем элементы по одному и демонстрируем вращения
	values = [10, 20, 30, 40, 50, 25]

	print("\n1. Вставка элементов и демонстрация балансировки:")
	for val in values:
		print(f"\nВставка элемента {val}:")
		root = insert(root, val)
		print("Структура дерева после вставки:")
		print(print_tree(root))

	# обход дерева для проверки свойства упорядоченности
	print("\n2. Обход дерева (in-order):")
	inorder = inorder_traversal(root)
	print(f"Элементы в порядке возрастания: {inorder}")

	# обход по уровням для проверки структуры
	print("\n3. Обход дерева по уровням (родитель-дети):")
	level_order = level_order_traversal(root)
	print("Узел -> Родитель:")
	for node, parent in level_order:
		print(f"  {node} -> {parent if parent is not None else 'корень'}")

	# удаление элементов
	print("\n4. Удаление элементов:")
	delete_value = 30
	print(f"Удаление элемента {delete_value}:")
	print("Дерево до удаления:")
	print(print_tree(root))

	root = delete(root, delete_value)

	print(f"Дерево после удаления {delete_value}:")
	print(print_tree(root))

	# поиск элементов
	print("\n5. Поиск элементов:")
	for val in [20, 30]:
		found = search(root, val)
		print(f"Элемент {val}: {'найден' if found else 'не найден'}")