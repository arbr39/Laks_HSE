class Node:
	def __init__(self, key, val):
		self.key, self.val = key, val
		self.prev = self.next = None


class LRUCache:
	def __init__(self, capacity):
		self.cap = capacity
		self.d = dict()
		self.head, self.tail = Node(0, 0), Node(0, 0)  # фейк узлы
		self.head.next, self.tail.prev = self.tail, self.head

	def _remove(self, node):  # вырезать
		node.prev.next, node.next.prev = node.next, node.prev

	def _add(self, node):  # вставить вперёд
		node.next, node.prev = self.head.next, self.head
		self.head.next.prev = node
		self.head.next = node

	def get(self, key):
		if key in self.d:
			node = self.d[key]
			self._remove(node)
			self._add(node)
			return node.val
		return -1  # нет такого

	def put(self, key, val):
		if key in self.d:
			self._remove(self.d[key])
		node = Node(key, val)
		self._add(node)
		self.d[key] = node
		if len(self.d) > self.cap:
			lru = self.tail.prev
			self._remove(lru)
			del self.d[lru.key]  # выкинули старый

	def print_cache(self):
		# вывод содержимого кэша
		print("Кэш (от новых к старым):", end=" ")
		node = self.head.next
		while node != self.tail:
			print(f"({node.key}:{node.val})", end=" → " if node.next != self.tail else "\n")
			node = node.next


# демонстрация работы
if __name__ == "__main__":
	print("Демонстрация работы LRU Cache:")

	# создание кэша на 3 элемента
	cache = LRUCache(3)
	print("Создан кэш размером 3")

	# добавление элементов
	print("\nДобавляем элементы (1:10), (2:20), (3:30):")
	cache.put(1, 10)
	cache.put(2, 20)
	cache.put(3, 30)
	cache.print_cache()

	# получение элемента (перемещение в начало)
	print("\nПолучаем элемент с ключом 1:")
	val = cache.get(1)
	print(f"get(1) вернул: {val}")
	cache.print_cache()

	# добавление нового элемента в заполненный кэш
	print("\nДобавляем элемент (4:40) в заполненный кэш:")
	cache.put(4, 40)
	cache.print_cache()
	print("Элемент (2:20) был вытеснен как наименее используемый")

	# попытка получить вытесненный элемент
	print("\nПытаемся получить вытесненный элемент:")
	val = cache.get(2)
	print(f"get(2) вернул: {val}")

	# обновление существующего значения
	print("\nОбновляем значение для ключа 3:")
	cache.put(3, 35)
	cache.print_cache()

	# заполнение кэша и вытеснение всех элементов
	print("\nДобавляем новые элементы (5:50), (6:60), (7:70):")
	cache.put(5, 50)
	cache.put(6, 60)
	cache.put(7, 70)
	cache.print_cache()
	print("Все предыдущие элементы были вытеснены")