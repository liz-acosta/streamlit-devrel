import unittest
import main

class TestAppMethods(unittest.TestCase):

    """Test class for methods in the app"""
     
    def test_sheet_data(self):
        
        expected_columns = ['created_at', 'url', 'clicks', 'utm_source', 'utm_campaign']
        test_result = main.sheet_data()
        
        # print(test_result.columns.array)
        # print(test_result['created_at'])
        
        self.assertEqual(test_result.columns.array, expected_columns)
        self.assertTrue(1 <= entry <= 12 for entry in test_result['created_at'])
        self.assertTrue(entry == 'dev-to' for entry in test_result['utm_source'])

    def test_select_list(self):
        
        expected_list = ['January', 'March', 'April', 'July', 'All time']
        test_result = main.selection_list()
        
        self.assertEqual(test_result, expected_list)

