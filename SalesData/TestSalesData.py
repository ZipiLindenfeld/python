import unittest
import pandas as pd
from SalesData import SalesData

class TestSalesData(unittest.TestCase):
    def setUp(self):
        self.example_data = {
            'Product': ['A', 'B', 'A', 'C'],
            'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-01', '2024-01-02']),
            'Total': [100, 200, 150, 300]
        }

    def test_eliminate_duplicates(self):
        sales_data = SalesData(self.example_data)
        sales_data.eliminate_duplicates()
        self.assertTrue(sales_data.data.duplicated().sum() == 0)

    def test_calculate_total_sales(self):
        # Arrange
        example_data = {
            'Product': ['A', 'B', 'A', 'C'],
            'Total': [100, 200, 150, 300]
        }
        sales_data = SalesData(example_data)

        expected_total_sales = pd.DataFrame({
            'Product': ['A', 'B', 'C'],
            'Total': [250, 200, 300]
        })

        # Act
        total_sales = sales_data.calculate_total_sales()

        # Assert
        self.assertTrue(total_sales.equals(expected_total_sales))

if __name__ == '__main__':
    unittest.main()