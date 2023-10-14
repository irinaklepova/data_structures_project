class Node:
    """Класс для узла стека"""

    def __init__(self, data=None, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None
        self.size = 0

    def __str__(self):
        all_stack = []
        node = self.top
        while node is not None:
            data = node.data
            all_stack.append(data)
            node = node.next_node
        return '\n'.join(all_stack)

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data, self.top)
        if self.top:
            new_node.next_node = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is None:

            return None
        result = self.top.data
        self.top = self.top.next_node
        self.size -= 1
        return result

    def is_empty(self):
        return self.top is None
