import unittest
from library_management_system_15_06_25 import Book
import os # Import os module for the same path
# Now we can ensure that the script is running from the same directory
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.b1 = Book("1984", "George Orwell")

    def tearDown(self):
        return super().tearDown()
    
    def test_A_initial_state(self):
        self.assertFalse(self.b1.is_checked_out)

    def test_B_check_out(self):
        self.b1.check_out()
        self.assertTrue(self.b1.is_checked_out)
    
    def test_C_double_check_out(self):
        self.b1.check_out()
        with self.assertRaises(Exception):
            self.b1.check_out()

    def test_D_return_book(self):
        with self.assertRaises(Exception):
            self.b1.return_book()

    def test_E_check_out_return_book(self):
        self.b1.check_out()
        self.b1.return_book()

if __name__ == '__main__':
    unittest.main()