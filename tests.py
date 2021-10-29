from json.decoder import JSONDecodeError
import unittest
from main import get_data, extract_schema


class TestJSONtoSchema(unittest.TestCase):
    '''
    Tests the various functions used in the converson of
    data from JSOn format to the python dict and back to
    JSON
    '''
    def test_getdata(self):
        self.assertEqual(type(get_data('data/data_1.json')), dict,
                         "Return Type should be a dictionary")

    def test_invalid_file(self):
        self.assertRaises(FileNotFoundError, get_data, 'abc.txt')

    def test_invalidJSON(self):
        self.assertRaises(JSONDecodeError, get_data, 'data/invalid.json')

    def test_processdata(self):
        data = get_data('data/data_1.json')
        self.assertEqual(type(extract_schema(data)), dict,
                         "Return Type should be a dictionary")

    
if __name__ == '__main__':
    unittest.main()
