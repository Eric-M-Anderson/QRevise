class AddOns:

    @staticmethod
    def list_to_string(data, value):
        new_data = []
        for i, e in enumerate(data):
            if i < len(data) - 1:
                new_data.append(e + value)
            else:
                new_data.append(e)
        return ''.join(str(E) for E in new_data)

    @staticmethod
    def read_command(u_input):
        if ' ' not in u_input:
            return [u_input]
        else:
            input_list = u_input.split(' ', 1)
        try:
            input_settings = input_list[1].split('"')
            input_settings = list(filter(lambda x: x != '', input_settings))
            input_settings = list(filter(lambda x: x != ' ', input_settings))
            input_list[1] = input_settings
            print(input_list)
            return input_list
        except IndexError:
            pass
