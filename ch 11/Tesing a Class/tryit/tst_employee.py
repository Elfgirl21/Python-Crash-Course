import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests module employee."""
    def setUp(self):
        """Make an employee to use in tests."""
        self.emp = Employee('lauren', 'harms', 1000)

    def test_give_default_raise(self):
        """Test that default raise works correctly."""
        self.emp.give_raise()
        self.assertEqual(self.emp.salary, 6000)

    def test_give_custom_raise(self):
        """Testthat a custom rais works correctly."""
        self.emp.give_raise(7000)
        self.assertEqual(self.emp.salary, 8000)

unittest.main()
