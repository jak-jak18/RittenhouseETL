import unittest
from test import support

class TestFuncAcceptsSequencesMixin:
    def func(self, arg):
        if type(arg) is list:
            return True
        else:
            return False

    def test_func(self):
        self.func(self.arg)

    def test_func2(self):
        self.func(self.arg, self.arg2)

class AcceptLists(TestFuncAcceptsSequencesMixin, unittest.TestCase):
    arg = [1, 2, 3]
    arg2 = [1, 2, 3]

class AcceptStrings(TestFuncAcceptsSequencesMixin, unittest.TestCase):
    arg = 'abc'

class AcceptTuples(TestFuncAcceptsSequencesMixin, unittest.TestCase):
    arg = (1, 2, 3)
