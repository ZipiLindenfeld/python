import pandas as pd


class FileOperation:

    def read_csv(self, file_path):
        """ read the data from a given file path"""
        data = pd.read_csv(file_path)
        return data

    def save_to_excel(self, data, file_name: str):
        """save data in an Excel file"""
        pd.DataFrame(data).to_csv(file_name, index=False)
        print(f"Data saved to {file_name} successfully.")


class FileOperationMain:
    file_path = "YafeNof.csv"
    # 1
    file = FileOperation()
    data = file.read_csv(file_path)
    print(data)
    # 2
    file.save_to_excel(data, "new.csv")
    data_to_write = file.read_csv("new.csv")
    print(data_to_write)
