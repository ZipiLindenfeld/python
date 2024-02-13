import pandas as pd
import docx2txt


class FileOperation:

    def read_csv(self, file_path):
        """ read the data from a given file path"""
        return self.convert_date_format(file_path)

    # def convert_date_format(self, file_path):
    #     date_columns = ['Date']
    #     data = pd.read_csv(file_path, parse_dates=date_columns)
    #     return data
    def convert_date_format(self, file_path):
        """convert date format while reading from file"""
        date_columns = ['Date']
        def parse_cube_date(x):
            return pd.to_datetime(x, format='%d.%m.%Y')
        data = pd.read_csv(file_path, parse_dates=date_columns, converters={'Date': parse_cube_date})

        return data

    def save_to_excel(self, data, file_name):
        """save data in an Excel file"""
        pd.DataFrame(data).to_csv(file_name, index=False)

    def read_docx(self, file_path):
        """read data from docx file"""
        text = docx2txt.process(file_path)
        return text
