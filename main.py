from banner import Banner
from file import File
from commands import Commands
from help import Help
from addons import AddOns
from os import system


if __name__ == "__main__":
    system("cls")  # Allows the colored text to work in an exe with pyinstaller

    print('\u001b[32;1m{}\u001b[0m'.format(Banner('  QRevise')))  # Prints The program name in an ascii font
    print("\n\nType 'help' to show the available commands")

    h = Help()  # Creates an instance of the Help class
    a = AddOns()  # Creates an instance of the AddOns class
    isScript = False

    while True:
        if isScript is True:
            command = a.read_command(command_list[scriptIndex])
            print('\u001b[30;1m>>>\u001b[0m {}'.format(command_list[scriptIndex]))
            scriptIndex += 1
            if len(command_list) - 1 == scriptIndex:
                isScript = False
        else:
            user_input = input('\u001b[30;1m>>> \u001b[0m')  # The command input for the program
            command = a.read_command(user_input)

        if command[0] == 'save':  # Overwrites the currently opened txt file with the new edited text
            if len(command) == 1:
                print('\u001b[33mAre you sure you want to over write', f.get_path(), '\u001b[0m')  # Prints a user warning
                while True:
                    answer = input("\u001b[30;1m#>> \u001b[0m")  # The input to answer the warning message
                    if answer.lower() == 'yes' or answer.lower() == 'y':
                        f.save_file(c.get_current_data(), False, f.get_path())  # Saves the edited text to the file
                        break
                    elif answer.lower() == 'no' or answer.lower() == 'n':
                        print('\u001b[33mCanceling Operation\u001b[0m')
                        break
                    else:
                        print('\u001b[31m{} is not an option. Enter [yes/y] or [no/n].\u001b[0m'.format(answer))
            else:
                f.save_file(c.get_current_data(), True, command[1][0])
                print("\u001b[32mOperation Complete\u001b[0m")

        elif command[0] == 'undo':
            c.undo()  # undoes an edit to the current text

        elif command[0] == 'redo':
            c.redo()  # redoes an edit to the current text

        elif command[0] == 'print':
            print('\u001b[35;1m{}\u001b[0m'.format(c.get_current_data()))  # Prints the currently edited text

        elif command[0] == 'cls':
            system("cls")  # Clears the screen
            print('\nType help to show the available commands')

        elif command[0] == 'help':
            if len(command) == 1:
                print(h.help())  # Shows all the available commands with a short description
            else:
                print(h.help_detail(command[1][0]))  # Shows additional detail about a command

        elif command[0] == 'load':
            try:
                f = File(command[1][0])  # Loads a files text into a File class instance
                c = Commands(f.get_data())  # Loads file text into a Commands class instance
                print('\u001b[32m{} has been successfully loaded in to program\u001b[0m'.format(f.get_file_name()))
            except FileNotFoundError:
                del f

        elif command[0] == 'lscript':
            try:
                script = File(command[1][0])  # Loads a files text into a File class instance
                command_list = script.get_data().split('\n')
                isScript = True
                scriptIndex = 0
                print('\u001b[32m{} has been successfully loaded in to program\u001b[0m'.format(script.get_file_name()))
            except FileNotFoundError:
                del f

        elif command[0] == 'rlines':
            c.remove_blank_lines()  # Removes blank lines in a file

        elif command[0] == 'rspaces':
            try:
                c.remove_double_spaces(eval(command[1][0].capitalize()))  # Removes double spaces in a file
            except NameError:
                print('\u001b[31m{} is not true or false\u001b[0m'.format(command[1][0]))

        elif command[0] == 'replace':
            c.find_and_replace(command[1][0], command[1][1])  # Replaces text in a file with other text

        elif command[0] == 'exit':
            break  # Ends the program

        else:
            filtered_command = list(filter(lambda x: x != ' ', command[0]))
            filtered_command = list(filter(lambda x: x != '\t', filtered_command))
            if filtered_command == [] or command[0] == ['']:  # Allows blank lines to be ignored
                pass
            else:
                print('\u001b[31m{} is not a command\u001b[0m'.format(command))
