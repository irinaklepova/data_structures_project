class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ""
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        self.head = Node(data, self.head)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next_node is not None:
                node = node.next_node
            node.next_node = new_node

    def to_list(self):
        """Возвращает список с данными, находящимися в односвязном списке"""
        list_nodes = []
        node = self.head
        if node is None:
            return list_nodes
        while node:
            list_nodes.append(node.data)
            node = node.next_node
        return list_nodes

    def get_data_by_id(self, id_value):
        """Метод возвращает первый найденный в `LinkedList` словарь с ключом 'id',
        значение которого равно переданному в метод значению"""
        node = self.head
        if node is None:
            return None
        while node:
            try:
                if node.data['id'] == id_value:
                    return node.data
                node = node.next_node

            except TypeError:
                node = node.next_node
                return 'TypeError: Данные не являются словарем или в словаре нет id.'

            if node is None:
                break
