from SalesData import SalesData


class SalesDataMain:
    from FileOperation.FileOperation import FileOperation

    # 4
    print("========4==========")
    file_path = "../Files/YafeNof.csv"
    file = FileOperation()
    data = file.read_csv(file_path)
    sales = SalesData(data)
    print(sales.data)
    sales.eliminate_duplicates()
    print(sales.data)
    # 5
    print("========5==========")
    total = sales.calculate_total_sales()
    print(total)
    # 6
    print("========6==========")
    total1 = sales._calculate_total_sales_per_month()
    print(total1)
    # 7
    print("========7==========")
    total = sales._identify_best_selling_product()
    print("max product:", total)
    # 8
    print("========8==========")
    total = sales._identify_month_with_highest_sales()
    print("max month:", total)
    # 9
    print("========9==========")
    data = sales.analyze_sales_data()
    print(data)
    # 10
    print("========10==========")
    data = sales.add_values_to_the_dictionary()
    print(data)
    # 11
    print("========11==========")
    monthly_sales = sales.calculate_cumulative_sales()
    print(monthly_sales)
    # 12
    print("========12==========")
    sales.add_90_values_column()
    print(sales.data)
    # 13
    print("========13==========")
    sales.bar_chart_category_sum()
    # 14
    print("========14==========")
    tuple_calculated = sales.calculate_mean_quantity()
    print(tuple_calculated)
    # 15
    print("========15A==========")
    new_sales = sales.filter_by_selling_or()
    print(new_sales[['Product', 'Quantity']])
    print("========15B==========")
    new2_sales = sales.filter_by_selling_and()
    print(new2_sales[['Product', 'Quantity', 'Price']])
    # 16
    print("========16==========")
    sales.divide_by_2()
    print(sales.data)
    # 18 = convert_date_format in FileOperation

    # task 6
    # matplotlib
    # 1
    sales.plot_total_sales()
    # 2
    sales.plot_total_sales_per_month()
    # 3
    sales.plot_total_sales_per_month_horizontal_bar()
    # 4
    sales.plot_total_sales_per_month_pie()
    # 5
    sales.plot_total_sales_per_month_step()
    # 6
    sales.plot_monthly_sales_histogram()
    # 7
    sales.plot_monthly_sales_boxplot()

    # seaborn
    # 1
    sales.plot_total_sales_per_month_lineplot()
    # 2
    sales.plot_total_sales_per_month_scatterplot()
    # 3
    sales.plot_total_sales_per_month_barplot()
    # 4
    sales.plot_total_sales_per_month_boxplot()
    # 5
    sales.plot_total_sales_per_month_violinplot()

    # task 7
    print("**************task 7*****************")
    # 1
    sales.treat_errors()
    # 3
    sales.rand_num('Zipi')
    # 4
    python_version = sales.get_python_version()
    print(python_version)
    # 5
    result1 = sales.process_parameters(10, "j=number", 3.14)
    print("Result 1:", result1)
    result2 = sales.process_parameters("zipi=name", 20, "20=age", 25)
    print("Result 2:", result2)
    result3 = sales.process_parameters("d=key",5, "o=value")
    print("Result 3:", result3)
    # 6
    sales.print_from_data()
    # 7
    sales.read_on_time()
