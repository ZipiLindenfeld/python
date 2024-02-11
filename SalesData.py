import pandas as pd
import numpy as np


class SalesData:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def eliminate_duplicates(self):
        """avoiding duplicate lines in the dataset """
        self.data.drop_duplicates(inplace=True)
        self.data.dropna(inplace=True)

    def calculate_total_sales(self):
        """calculate the total sales for each product"""
        total_sales = self.data.groupby('Product')['Total'].sum().reset_index()
        return total_sales

    def _calculate_total_sales_per_month(self):
        """calculate the total sales for each month"""
        self.data['Date'] = pd.to_datetime(self.data['Date'], dayfirst=False, format='%d.%m.%Y')
        total_sales_per_month = self.data.groupby(self.data['Date'].dt.month)['Total'].sum()
        return total_sales_per_month

    def _identify_best_selling_product(self):
        """find the product with the max total sales"""
        total_sales = self.calculate_total_sales().max()
        return total_sales['Product']

    def _identify_month_with_highest_sales(self):
        """find the month with the max total sales"""
        total_sales = self._calculate_total_sales_per_month().idxmax()
        return total_sales

    def calculate_cumulative_sales(self):
        """calculate the total sales for each product in each month"""
        self.data['Date'] = pd.to_datetime(self.data['Date'], dayfirst=False, format='%d.%m.%Y')
        monthly_sales = self.data.groupby(['Product', self.data['Date'].dt.month])['Total'].sum().groupby(
            'Product').cumsum().reset_index()
        return monthly_sales

    def add_values_to_the_dictionary(self):
        d = self.analyze_sales_data()
        d['minimest selling product'] = self.calculate_total_sales().min()['Product']
        d["average of the sales for monthes"] = self._calculate_total_sales_per_month().mean()
        return d

    def analyze_sales_data(self):
        d = {
            'best_selling_product': self._identify_best_selling_product(),
            'month_with_highest_sales': self._identify_month_with_highest_sales(),
        }
        return d

    def add_90_values_column(self):
        self.data['Discount'] = 0.9 * (self.data['Price'])


class SalesDataMain:
    from FileOperation import FileOperation

    file_path = "YafeNof.csv"
    # 1
    file = FileOperation()
    data = file.read_csv(file_path)
    print(data)

    # 4
    sales = SalesData(data)

    # print(sales.data)
    # sales.eliminate_duplicates()
    # print(sales.data)
    # 5
    # total = sales.calculate_total_sales()
    # print(total)
    # 6
    # total1 = sales.calculate_total_sales_per_month()
    # print(total1)
    # 7
    # total = sales.identify_best_selling_product()
    # print("max product:", total['Product'])
    # 8
    # total = sales.identify_month_with_highest_sales()
    # print("max month:", total)
    # 9
    # data = sales.analyze_sales_data()
    # print(data)

    # 10
    # data = sales.add_values_to_the_dictionary()
    # print(data)
    # 11
    print("_____________________11_______________________")
    monthly_sales = sales.calculate_cumulative_sales()
    print(monthly_sales)
    # 12
    sales.add_90_values_column()
    print(sales.data)
