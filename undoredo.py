class UndoRedo:
    def __init__(self, start_data):
        self.index = 0
        self.start_data = start_data
        self.change_list = [self.start_data]
        self.data_ahead_current_index = False

    def get_current_data(self):
        return self.change_list[self.index]

    def add_change(self, data):
        if self.data_ahead_current_index is False:
            self.change_list.append(data)
            self.index += 1
        else:
            self.change_list = self.change_list[:self.index + 1]
            self.change_list.append(data)
            self.index = len(self.change_list) - 1

    def redo(self):
        self.data_ahead_current_index = True
        if self.index < len(self.change_list) - 1:
            self.index += 1
        else:
            print("\u001b[31mredo not possible\u001b[0m")

    def undo(self):
        if self.index > 0:
            self.index -= 1
        else:
            print("\u001b[31mundo not possible\u001b[0m")
        if len(self.change_list) - 1 == self.index:
            self.data_ahead_current_index = False

    def current_index(self):
        return self.index, len(self.change_list) - 1

    def current_list(self):
        return self.change_list
