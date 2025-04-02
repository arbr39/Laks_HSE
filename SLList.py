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


# создание списка из массива
def create_list(arr):
	if not arr:
		return None
	head = Node(arr[0])
	curr = head
	for val in arr[1:]:
		curr.next = Node(val)
		curr = curr.next
	return head


# создание списка с циклом
def create_cyclic_list(arr, pos):
	if not arr:
		return None

	head = create_list(arr)
	if pos < 0:
		return head  # без цикла

	# находим узел, на который будет указывать последний
	cycle_node = head
	for _ in range(pos):
		if not cycle_node.next:
			return head  # позиция вне списка
		cycle_node = cycle_node.next

	# находим последний узел
	last = head
	while last.next:
		last = last.next

	# создаем цикл
	last.next = cycle_node
	return head


# вывод списка (с защитой от циклов)
def print_list(head, limit=20):
	values = []
	count = 0
	curr = head
	while curr and count < limit:
		values.append(str(curr.val))
		curr = curr.next
		count += 1
	result = " → ".join(values)
	if count == limit:
		result += " → ... (возможно, цикл)"
	return result


# демонстрация работы
if __name__ == "__main__":
	print("Демонстрация работы с односвязным списком:")

	# обычный список
	arr = [1, 2, 3, 4, 5, 6, 7]
	normal_list = create_list(arr)
	print("\n1. Обычный список без цикла:")
	print(print_list(normal_list))

	# проверка на цикл
	cycle_len = cycle_length(normal_list)
	print(f"Длина цикла: {cycle_len}")

	# поиск середины
	mid = find_middle(normal_list)
	print(f"Значение середины списка: {mid}")

	# k-й элемент с конца
	k = 2
	kth = kth_from_end(normal_list, k)
	print(f"{k}-й элемент с конца: {kth}")

	# создание списка с циклом
	pos = 2  # цикл начинается с элемента с индексом 2 (значение 3)
	cyclic_list = create_cyclic_list(arr, pos)
	print(f"\n2. Список с циклом (начинается с элемента {arr[pos]}):")
	print(print_list(cyclic_list))

	# проверка на цикл
	cycle_len = cycle_length(cyclic_list)
	print(f"Длина цикла: {cycle_len}")

	# создание списка с циклом в конце
	pos = 0  # цикл начинается с первого элемента
	cyclic_list2 = create_cyclic_list([10, 20, 30, 40, 50], pos)
	print(f"\n3. Список с циклом с начала до конца:")
	print(print_list(cyclic_list2))

	# проверка на цикл
	cycle_len = cycle_length(cyclic_list2)
	print(f"Длина цикла: {cycle_len}")