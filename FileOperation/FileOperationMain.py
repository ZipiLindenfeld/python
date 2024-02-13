from FileOperation import FileOperation


class FileOperationMain:
    file_path = "../Files/YafeNof.csv"
    new_file_path = "../Files/NewFile.csv"
    # 1
    print("===========1============")
    file = FileOperation()
    data = file.read_csv(file_path)
    print(data)
    # 2
    print("===========2============")
    file.save_to_excel(data[:10:], new_file_path)
    data_to_write = file.read_csv(new_file_path)
    print(data_to_write)
    # task 7
    # 2
    print("read from docx: ")
    file_content = file.read_docx('../Files/text.docx')
    print(file_content)


