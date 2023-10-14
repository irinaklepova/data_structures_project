"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue(self):

        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')

        self.assertEqual(self.queue.head.data, 'data1')
        self.assertEqual(self.queue.head.next_node.data, 'data2')
        self.assertEqual(self.queue.head.next_node.next_node.data, 'data3')
        self.assertEqual(self.queue.tail.next_node, None)

    def test_str(self):

        self.assertEqual(str(Queue()), "")

        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual(str(self.queue), "data1\ndata2\ndata3")
