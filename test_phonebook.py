import unittest

from phonebook import Phonebook

book = Phonebook() 

class PhonebookTestCase(unittest.TestCase):
    """Test case for the phonebook app"""
    def setUp(self):
        self.name = "steve"
        self.number = "0712762717"

    def test_add(self):
        """Test user can add a new contact"""
        result = book.add(self.name, self.number)
        self.assertEqual(result, "contact added successfully")

    def test_delete(self):
        result = book.delete(self.name)
        self.assertEqual(result, "contact deleted successfully")

if __name__ == '__main__':
    unittest.main()