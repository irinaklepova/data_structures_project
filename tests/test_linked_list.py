"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_insert(self):
        # Создаем пустой односвязный список
        self.ll = LinkedList()

        # Добавляем данные
        self.ll.insert_at_end({'id': 2})
        self.assertEqual(self.ll.head.data, {'id': 2})
        self.ll.insert_beginning({'id': 1})
        self.assertEqual(str(self.ll), "{'id': 1} -> {'id': 2} -> None")

        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})
        self.assertEqual(str(self.ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

        self.assertEqual(self.ll.head.data, {'id': 0})
        self.assertEqual(self.ll.head.next_node.data, {'id': 1})
        self.assertEqual(self.ll.head.next_node.next_node.data, {'id': 2})
        self.assertEqual(self.ll.head.next_node.next_node.next_node.data, {'id': 3})
