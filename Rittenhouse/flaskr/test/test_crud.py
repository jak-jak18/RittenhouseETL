from crud import create
import unittest
from test import support

class TestFuncAcceptsSequencesMixin:

    def create(self):
        """CRUD create function. Initial function for app and used to create entries.
        Will add entry to db based on POST method.

        :return: returns template
        :rtype:
        """
        if request.method == 'POST':
            data = request.form.to_dict(flat=True)
            get_model().create(tuple(data.values()))

        return render_template("list.html")

    def test_func(self):
        self.create()

    # def test_func2(self):
    #     self.func(self.arg, self.arg2)

class AcceptLists(TestFuncAcceptsSequencesMixin, unittest.TestCase):
    arg = [1, 2, 3]

class AcceptStrings(TestFuncAcceptsSequencesMixin, unittest.TestCase):
    arg = 'abc'

class AcceptTuples(TestFuncAcceptsSequencesMixin, unittest.TestCase):
    arg = (1, 2, 3)


