import unittest
import pandas as pd
from unittest.mock import patch, mock_open
from FileOperation import FileOperation


class TestFileOperation(unittest.TestCase):

    def setUp(self):
        self.file_operation = FileOperation()

    @patch('pandas.read_csv')
    def test_read_csv(self, mock_read_csv):
        test_data = pd.DataFrame({'Date': ['2024-01-01', '2024-01-02'],
                                  'Value': [1, 2]})
        mock_read_csv.return_value = test_data
        result = self.file_operation.read_csv('test.csv')
        self.assertEqual(result.to_dict(), test_data.to_dict())

    # def test_convert_date_format(self):
    #     test_data = pd.DataFrame({'Date': ['2024-01-01', '2024-01-02'],
    #                               'Value': [1, 2]})
    #     expected_data = pd.DataFrame({'Date': pd.to_datetime(['2024-01-01', '2024-01-02']),
    #                                   'Value': [1, 2]})
    #     result = self.file_operation.convert_date_format('test.csv')
    #     self.assertTrue(result.equals(expected_data))

    def test_convert_date_format(self):
        file_path = "test.csv"
        result = self.file_operation.convert_date_format(file_path)
        assert isinstance(result, pd.DataFrame)
        assert 'Date' in result.columns
        assert result['Date'].dtype == 'datetime64[ns]'

    @patch('pandas.DataFrame.to_csv')
    def test_save_to_excel(self, mock_to_csv):
        data = {'Date': ['2024-01-01', '2024-01-02'],
                'Value': [1, 2]}
        file_name = 'test.csv'
        self.file_operation.save_to_excel(data, file_name)
        mock_to_csv.assert_called_once_with(file_name, index=False)

    @patch('docx2txt.process')
    def test_read_docx(self, mock_process):
        mock_process.return_value = "Test text"
        result = self.file_operation.read_docx('test.docx')
        self.assertEqual(result, "Test text")


if __name__ == '__main__':
    unittest.main()
