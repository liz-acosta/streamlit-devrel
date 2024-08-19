import unittest
import main

class TestData(unittest.TestCase):

    """Test class for data retrieval"""
     
    def test_sheet_data(self):
        
        expected_result = ""

        test_result = main.sheet_data()
        print(test_result)
        self.assertEqual(expected_result, test_result)
