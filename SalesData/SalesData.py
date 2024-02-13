import datetime
import random
import platform

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


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
        """bar plot for total sales """
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
        """ linerplot for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=total_sales_per_month.index, y=total_sales_per_month.values)
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Line Plot)')
        plt.show()

    def plot_total_sales_per_month_scatterplot(self):
        """ scatterplot for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=total_sales_per_month.index, y=total_sales_per_month.values)
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Scatter Plot)')
        plt.show()

    def plot_total_sales_per_month_barplot(self):
        """ barplot for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.barplot(x=total_sales_per_month.index, y=total_sales_per_month.values)
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Bar Plot)')
        plt.show()

    def plot_total_sales_per_month_boxplot(self):
        """ boxplot for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=total_sales_per_month.values)
        plt.xlabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Box Plot)')
        plt.show()

    def plot_total_sales_per_month_violinplot(self):
        """ violinplot for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.violinplot(x=total_sales_per_month.values)
        plt.xlabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Violin Plot)')
        plt.show()

    def plot_total_sales_per_month(self):
        """ simple plot for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        plt.plot(total_sales_per_month.index, total_sales_per_month.values, marker='o', linestyle='-')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month')
        plt.tight_layout()
        plt.show()

    def plot_total_sales_per_month_horizontal_bar(self):
        """ horizontal_bar for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        total_sales_per_month.plot(kind='barh', color='skyblue')
        plt.xlabel('Total Sales')
        plt.ylabel('Month')
        plt.title('Total Sales per Month (Horizontal Bar Plot)')
        plt.tight_layout()
        plt.show()

    def plot_total_sales_per_month_pie(self):
        """ pie for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        plt.figure(figsize=(8, 8))
        total_sales_per_month.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.tab20.colors)
        plt.ylabel('')
        plt.title('Total Sales Distribution per Month (Pie Chart)')
        plt.tight_layout()
        plt.show()

    def plot_total_sales_per_month_step(self):
        """ step plot for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        plt.step(total_sales_per_month.index, total_sales_per_month.values, color='skyblue', where='mid')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month (Step Plot)')
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
        """ histogram for monthly sales"""
        monthly_sales = self.calculate_cumulative_sales()
        plt.figure(figsize=(10, 6))
        plt.hist(monthly_sales['Total'], bins=20, color='skyblue', edgecolor='black')
        plt.xlabel('Total Sales')
        plt.ylabel('Frequency')
        plt.title('Histogram of Total Sales per Product')
        plt.grid(True)
        plt.show()

    def plot_monthly_sales_boxplot(self):
        """ boxplot for monthly sales"""
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
        """do dictionary with the best-selling product and the month with highest sales"""
        d = {
            'best_selling_product': self._identify_best_selling_product(),
            'month_with_highest_sales': self._identify_month_with_highest_sales(),
        }
        return d

    def add_90_values_column(self):
        """add discount"""
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
        """return filtered dataset that include the products that their price is above 300 dollars and thy were sold
        less than twice"""
        sales = self.data
        sales['Count'] = sales.groupby('Product')['Product'].transform('count')
        return sales[(sales['Price'] > 300) & (sales['Count'] < 2)]

    def divide_by_2(self):
        """adding the price for the black friday"""
        self.data['Black_Friday'] = self.data['Price'] / 2

    def treat_errors(self):
        """errors"""
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
                raise ValueError("Invalid date")
            datetime.datetime(year, month, day)
        except ValueError:
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
        """rand number range"""
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
        """return the version of python"""
        version = platform.python_version()
        return version

    def process_parameters(*args):
        """sorting parameters with tags"""
        result = {}
        for param in args:
            if isinstance(param, str) and "=" in param:
                value, name = param.split("=", 1)
                result[name] = value
            elif isinstance(param, (int, float)):
                print(param)
        return result

    def print_from_data(self):
        """print 3 first rows, 2 last and one random row"""
        print(self.data.head(3))
        print("==================")
        print(self.data.tail(2))
        random_row = self.data.sample(n=1)
        print(random_row)

    def read_on_time(self):
        """read all the numbers in one line"""
        for value in self.data.select_dtypes(include=[np.number]).values.flatten():
            print(value)
