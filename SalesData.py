import datetime
import random
import platform
from itertools import chain

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import pytz as vv


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

    def plot_total_sales(self):
        total_sales = self.calculate_total_sales()
        products = total_sales['Product']
        sales = total_sales['Total']
        plt.figure(figsize=(10, 6))
        plt.bar(products, sales, color='skyblue')
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.title('Total Sales for Each Product')
        plt.tight_layout()
        plt.show()

    def _calculate_total_sales_per_month(self):
        """calculate the total sales for each month"""
        total_sales_per_month = self.data.groupby(self.data['Date'].dt.month)['Total'].sum()
        return total_sales_per_month

    def plot_total_sales_per_month_lineplot(self):
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=total_sales_per_month.index, y=total_sales_per_month.values)
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Line Plot)')
        plt.show()

    def plot_total_sales_per_month_scatterplot(self):
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=total_sales_per_month.index, y=total_sales_per_month.values)
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Scatter Plot)')
        plt.show()

    def plot_total_sales_per_month_barplot(self):
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.barplot(x=total_sales_per_month.index, y=total_sales_per_month.values)
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Bar Plot)')
        plt.show()

    def plot_total_sales_per_month_boxplot(self):
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=total_sales_per_month.values)
        plt.xlabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Box Plot)')
        plt.show()

    def plot_total_sales_per_month_violinplot(self):
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.violinplot(x=total_sales_per_month.values)
        plt.xlabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Violin Plot)')
        plt.show()

    def plot_total_sales_per_month(self):
        total_sales_per_month = self._calculate_total_sales_per_month()
        plt.plot(total_sales_per_month.index, total_sales_per_month.values, marker='o', linestyle='-')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month')
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        plt.xticks(total_sales_per_month.index, month_names)
        plt.tight_layout()
        plt.show()

    def plot_total_sales_per_month_horizontal_bar(self):
        total_sales_per_month = self._calculate_total_sales_per_month()
        total_sales_per_month.plot(kind='barh', color='skyblue')
        plt.xlabel('Total Sales')
        plt.ylabel('Month')
        plt.title('Total Sales per Month (Horizontal Bar Plot)')
        plt.tight_layout()
        plt.show()

    def plot_total_sales_per_month_pie(self):
        total_sales_per_month = self._calculate_total_sales_per_month()
        plt.figure(figsize=(8, 8))
        total_sales_per_month.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.tab20.colors)
        plt.ylabel('')
        plt.title('Total Sales Distribution per Month (Pie Chart)')
        plt.tight_layout()
        plt.show()

    def plot_total_sales_per_month_step(self):
        total_sales_per_month = self._calculate_total_sales_per_month()
        plt.step(total_sales_per_month.index, total_sales_per_month.values, color='skyblue', where='mid')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month (Step Plot)')
        plt.xticks(total_sales_per_month.index,
                   ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        plt.tight_layout()
        plt.show()

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
        monthly_sales = self.data.groupby(['Product', self.data['Date'].dt.month])['Total'].sum().groupby(
            'Product').cumsum().reset_index()
        return monthly_sales

    def plot_monthly_sales_histogram(self):
        monthly_sales = self.calculate_cumulative_sales()
        plt.figure(figsize=(10, 6))
        plt.hist(monthly_sales['Total'], bins=20, color='skyblue', edgecolor='black')
        plt.xlabel('Total Sales')
        plt.ylabel('Frequency')
        plt.title('Histogram of Total Sales per Product')
        plt.grid(True)
        plt.show()

    def plot_monthly_sales_boxplot(self):
        monthly_sales = self.calculate_cumulative_sales()
        plt.boxplot(monthly_sales['Total'], vert=False)
        plt.xlabel('Total Sales')
        plt.title('Box Plot of Total Sales per Product')
        plt.show()

    def add_values_to_the_dictionary(self):
        """return mean sum of sales for month for each product"""
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

    def bar_chart_category_sum(self):
        """represent a bar chart of the sum of quantities sold for each product."""
        grouped_data = self.data.groupby('Product')['Quantity'].sum().reset_index()
        plt.bar(grouped_data['Product'], grouped_data['Quantity'])
        plt.xlabel('Product')
        plt.ylabel('Quantity Sold')
        plt.title('Sum of Quantities Sold for Each Product')
        plt.tight_layout()
        plt.show()

    def calculate_mean_quantity(self):
        """return the mean,the second max and the median of the total of the sales"""
        total_column = self.data['Total'].values
        mean = np.mean(total_column)
        median = np.median(total_column)
        max_total = np.max(total_column)
        max_index = np.where(total_column == max_total)
        total_column = np.delete(total_column, max_index)
        second_max = np.max(total_column)
        return mean, median, second_max

    def filter_by_selling_or(self):
        """return filtered dataset that include the products that were sold at least 5 times or never were sold"""
        sales_summary = self.data.groupby('Product').count().reset_index()
        return sales_summary[(sales_summary['Quantity'] > 5) | (sales_summary['Quantity'] == 0)]

    def filter_by_selling_and(self):
        """return filtered dataset that include the products that their price is above 300 dollars and thy were sold less than twice"""
        sales = self.data
        sales['Count'] = sales.groupby('Product')['Product'].transform('count')
        return sales[(sales['Price'] > 300) & (sales['Count'] < 2)]

    def divide_by_2(self):
        """adding the price for the black friday"""
        self.data['Black_Friday'] = self.data['Price'] / 2

    def treat_errors(self):
        current_date = datetime.datetime.now().date()
        current_time = datetime.datetime.now().time()
        current_name = "Zipi&Sari&Ruth"
        try:
            x = 4 / 0
            print(x)
        except ZeroDivisionError:
            print("<" + current_name + "," + str(current_date) + "," + str(
                current_time) + "> type error: divide by zero! <" + current_name + ">")
        try:
            year = 50
            month = 50
            day = 50
            if year < 2000 | year > 2024 | month < 1 | month > 12 | day < 1 | day > 31:
                raise SyntaxError
            datetime.datetime(year, month, day)
        except SyntaxError:
            print("<" + current_name + "," + str(current_date) + "," + str(
                current_time) + "> type error: you didnt enter correct date!!! <" + current_name + ">")
        try:
            y = "aaa"
            print(int(y))
        except BaseException:
            print("<" + current_name + "," + str(current_date) + "," + str(
                current_time) + "> cannot convert type str to int <" + current_name + ">")
        try:
            s = {'o': 'f'}
            print(s['Price'])
        except BaseException:
            print("<" + current_name + "," + str(current_date) + "," + str(
                current_time) + "> cannot find 'Price' in s <" + current_name + ">")

    def rand_num(self, product_name):
        sum_sales = self.data.groupby('Product')['Quantity'].count()[product_name]
        max_sales_sum = self.data.groupby('Product')['Price'].max()[product_name]
        rand_num = random.randint(sum_sales, max_sales_sum)
        a = []
        a.append(product_name)
        a.append(sum_sales)
        a.append(max_sales_sum)
        a.append(rand_num)
        print(a)

    def get_python_version(self):
        version = platform.python_version()
        return version

    def process_parameters(*args):
        result = {}

        for param in args:
            if isinstance(param, str) and "=" in param:
                value, name = param.split("=", 1)
                result[name] = value
            elif isinstance(param, (int, float)):
                print(param)
        return result

    def print_from_data(self):
        print(self.data)
        print(self.data.loc[[0, 1, 2]])

        print("==================")
        print(self.data.tail(2))

        random_row = self.data.sample(n=1)
        print(random_row)

    def read_on_time(self):
        for value in self.data.select_dtypes(include=[np.number]).values.flatten():
            print(value)


class SalesDataMain:
    from FileOperation import FileOperation

    file_path = "YafeNof.csv"
    # 1
    file = FileOperation()
    data = file.read_csv(file_path)
    # print(data)

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
    # monthly_sales = sales.calculate_cumulative_sales()
    # print(monthly_sales)
    # 12
    # sales.add_90_values_column()
    # print(sales.data)
    # 13
    # sales.bar_chart_category_sum()
    # 14
    # tuple_calculated = sales.calculate_mean_quantity()
    # print(tuple_calculated)
    # 15
    # sales = sales.filter_by_selling_or()
    # print(sales[['Product', 'Quantity']])
    # sales = sales.filter_by_selling_and()
    # print(sales[['Product', 'Quantity', 'Price']])
    # 16
    # sales.divide_by_2()
    # print(sales.data)
    # task 6
    # 1
    # sales.plot_total_sales()
    # 2
    # sales.plot_total_sales_per_month()
    # 3
    # sales.plot_total_sales_per_month_horizontal_bar()
    # 4
    # sales.plot_total_sales_per_month_pie()
    # 5
    # sales.plot_total_sales_per_month_step()
    # 6
    # sales.plot_monthly_sales_histogram()
    # 7
    # sales.plot_monthly_sales_boxplot()
    # seaborn
    # 1
    # sales.plot_total_sales_per_month_lineplot()
    # 2
    # sales.plot_total_sales_per_month_scatterplot()
    # 3
    # sales.plot_total_sales_per_month_barplot()
    # 4
    # sales.plot_total_sales_per_month_boxplot()
    # 5
    # sales.plot_total_sales_per_month_violinplot()
    # task 7
    # 1
    # sales.treat_errors()
    # 3
    # sales.rand_num('Zipi')
    # 4
    # python_version = sales.get_python_version()
    # print(python_version)
    # 5
    # result1 = sales.process_parameters(10, "j=number", 3.14)
    # print("Result 1:", result1)
    # result2 = sales.process_parameters("zipi=name", 20, "ruth=age", 25)
    # print("Result 2:", result2)
    # result3 = sales.process_parameters("d=key", True,5, "o=value", False)
    # print("Result 3:", result3)
    # 6
    # sales.print_from_data()
    # 7
    # sales.read_on_time()
