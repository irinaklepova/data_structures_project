"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):
    def test_init(self):
        stack = Stack()
        self.assertEqual(stack.top, None)
        self.assertEqual(stack.size, 0)
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')

    def test_push(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.size, 2)

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.pop()
        self.assertEqual(stack.size, 1)
        stack.pop()

    def test_str(self):
        self.stack = Stack()
        self.assertEqual(self.stack.__str__(), "")
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')
        self.assertEqual(self.stack.__str__(), "data3\ndata2\ndata1")
