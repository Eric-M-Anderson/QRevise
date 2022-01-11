from undoredo import UndoRedo
from addons import AddOns


class Commands(UndoRedo):
    def __init__(self, start_data):
        super().__init__(start_data)
        self.a = AddOns()

    def remove_blank_lines(self):
        print('start')
        new_data = []
        data = self.get_current_data().split('\n')
        for e in data:
            if e != '':
                new_data.append(e)
        print('done')
        self.add_change(self.a.list_to_string(new_data, '\n'))

    def remove_double_spaces(self, remove_starting_spaces=False):
        new_data_list = []
        data1 = self.get_current_data().split('\n')
        for e1 in data1:
            data2 = e1.split(' ')
            new_data = []
            found_not_space = False
            for e2 in data2:
                if e2 != '' and found_not_space is False:
                    found_not_space = True
                if remove_starting_spaces is False:
                    if found_not_space is True and e2 != '':
                        new_data.append(e2)
                    elif found_not_space is False:
                        new_data.append(e2)
                elif remove_starting_spaces is True and e2 != '':
                    new_data.append(e2)
            new_data_list.append(self.a.list_to_string(new_data, ' '))
        self.add_change(self.a.list_to_string(new_data_list, '\n'))

    def find_and_replace(self, remove_text, new_text):
        data = self.get_current_data()
        self.add_change(self.a.list_to_string(data.split(remove_text), new_text))

