import unittest
import pandas as pd
from unittest.mock import patch
from FileOperation import FileOperation


class FileOperationTestCase(unittest.TestCase):

    def setUp(self):
        self.file = FileOperation()

    def test_read_csv(self):
        self.assertEqual(self.file.read_csv('new.csv'), None)  # Replace with expected result

    @patch('pandas.DataFrame.to_csv')
    def test_save_to_excel(self, mock_to_csv):
        data = pd.DataFrame({'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']})
        self.file.save_to_excel(data, 'test.xlsx')
        mock_to_csv.assert_called_once_with('test.xlsx', index=False)

    def test_read_docx(self):
        self.assertEqual(self.file.read_docx('test.docx'), None)  # Replace with expected result


if __name__ == '__main__':
    unittest.main()
