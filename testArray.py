import unittest
from task_3 import TestArray


class TestArrays(unittest.TestCase):
    def setUp(self):
        self.array = TestArray([1, 23, 4, 5, 5])

    def test_find_max(self):
        self.assertEqual(self.array.findMax(), (23, 5))
