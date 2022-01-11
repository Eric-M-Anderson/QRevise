class Help:
    def __init__(self):
        pass

    @staticmethod
    def help():
        return '\u001b[34;1m\n-----------------------------------------File Commands-----------------------------------------\n\n\u001b[0m' \
               '\u001b[36;1mload "file path"                         Selects a file to open\n' \
               'save                                     Saves to the original file by overwriting it\n' \
               'save "file path"                         Saves data to a new file\n\n\n\n\u001b[0m' \
               '\u001b[34;1m----------------------------------------Editor Commands----------------------------------------\n\n\u001b[0m' \
               '\u001b[36;1mreplace "text1" "text2"                  Replaces text in a file to specified new text\n' \
               'rlines                                   Removes blank lines in a text file\n' \
               'rspaces <true | false>                   Removes over spacing in a line\n\n\n\n\u001b[0m' \
               '\u001b[34;1m-----------------------------------------More Commands-----------------------------------------\n\n\u001b[0m' \
               '\u001b[36;1mcls                                      Clears the screen\n' \
               'exit                                     Ends the program\n' \
               'help <command>                           Gives more detail about a command\n' \
               'print                                    Prints the current file edits\n' \
               'redo                                     Is the reverse of the undo command\n' \
               'lscript "file path"                      Allows QRevise commands to be executed from a file\n' \
               'undo                                     Goes to previous operations\n\n\u001b[0m'

    @staticmethod
    def help_detail(command):
        if command == 'load':
            return '\u001b[36;1m\nload "file path"                         Selects a file to open\n\n\u001b[0m' \
                   '\u001b[34;1m---------------------------------------------Notes---------------------------------------------\n\u001b[0m' \
                   '\u001b[36;1m\n' \
                   'File Path: The location to save the file and the file name. Also ensure to include the .txt extension\n\u001b[0m'
        elif command == 'replace':
            return '\u001b[36;1m\nreplace "text1" "text2"                  Replaces text in a file to specified new text\n\n\u001b[0m' \
                   '\u001b[34;1m---------------------------------------------Notes---------------------------------------------\n\u001b[0m' \
                   '\u001b[36;1m\n' \
                   'Text1: The text you want to replace in your file\n' \
                   'Text2: What you want to replace text1 with\n\u001b[0m'
        elif command == 'rspaces':
            return '\u001b[36;1m\nmrspaces <true | false>                   Removes over spacing in a line\n\n\u001b[0m' \
                   '\u001b[34;1m---------------------------------------------Notes---------------------------------------------\n\u001b[0m' \
                   '\u001b[36;1m\n' \
                   ' True: Removes the starting spaces on each line\n' \
                   'False: Does not remove the starting spaces on each line\n\u001b[0m'
        elif command == 'save':
            return '\u001b[36;1m\nsave                                     Saves to the original file by overwriting it\u001b[0m' \
                   '\u001b[36;1m\nsave "file path"                         Saves data to a new file\n\n\u001b[0m' \
                   '\u001b[34;1m---------------------------------------------Notes---------------------------------------------\n\u001b[0m' \
                   '\u001b[36;1m\n' \
                   'File Path: The location to save the file and the file name. Also ensure to include the .txt extension\n' \
                   'Warns that the currently loaded file will be overwritten. This is only applicable when no file path is specified\n\u001b[0m'
        elif command == 'lscript':
            return '\u001b[36;1m\nscript "file path"                       Allows QRevise commands to be executed from a file\n\n\u001b[0m' \
                   '\u001b[34;1m---------------------------------------------Notes---------------------------------------------\n\u001b[0m' \
                   '\u001b[36;1m\n' \
                   'File Path: The location to open the scripting file and the file to open. Also ensure to include the .txt extension\n\u001b[0m'
        else:
            return '\u001b[31m{} is, other invalid or does not have an more information on it.\u001b[0m'.format(command)
