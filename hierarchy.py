import os


"""
Text Hierarchy Reformatter
"""


def file_hierarcher():
    """
    Reformats an outline text file with no tabs for hierarchies
    :param file_name:
    :return:
    """

    directory_in_str = 'files'
    directory = os.fsencode(directory_in_str)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            new_lines = []
            curr_tab = ''
            old_line = ''
            print(filename)
            lines = [line.rstrip('\n') for line in open('files/' + filename)]
            for line in lines:
                if line.startswith(('I.', 'II.', 'III.', 'IV.', 'V.', 'VI.', 'VII.')):
                    curr_tab = ''
                    new_line = curr_tab + line.rstrip()
                elif line.startswith(('A.', 'B.', 'C.', 'D.', 'E.', 'F.', 'G.')):
                    curr_tab = '        '
                    new_line = curr_tab + line.rstrip('/n')
                elif line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.')):
                    curr_tab = '                '
                    new_line = curr_tab + line.rstrip()
                else:
                    new_line = curr_tab + '    ' + line.rstrip()
                    new_line = old_line + new_line

                new_lines.append(new_line)

            f = open('files/' + filename, 'w')
            for line in new_lines:
                print(line)
                f.write(line + '\n')


file_hierarcher()





