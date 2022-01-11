import os


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_file_size(self):
        try:
            file_size = os.path.getsize(self.file_path)
            return file_size
        except FileNotFoundError:
            return -1

    def get_file_name(self):
        r_file_path = self.file_path[::-1]
        file_name = ''
        for i in r_file_path:
            if i != '\\':
                file_name += i
            else:
                return file_name[::-1]

    def get_data(self):
        if self.get_file_size() == 0:
            print("\u001b[31mThe file is empty and will not be loaded\u001b[0m")
            raise FileNotFoundError
        elif self.get_file_size() == -1:
            print("\u001b[31mThe file was not found\u001b[0m")
            raise FileNotFoundError
        else:
            data = open(self.file_path, "r").read()
            return data

    @staticmethod
    def save_file(data, new_file, path):
        try:
            if new_file is False:
                open(path, "w").write(data)
            else:
                open(path, "x").write(data)
        except FileNotFoundError:
            print("\u001b[31mThe file was not found\u001b[0m")

    def get_path(self):
        return self.file_path

    def set_path(self, new_path):
        self.file_path = new_path
