"""
Text Hierarchy Reformatter
"""


def file_hierarcher(file_name):
    """
    Reformats an outline text file with no tabs for hierarchies
    :param file_name:
    :return:
    """
    new_lines = []
    curr_tab = ''
    old_line = ''
    lines = [line.rstrip('\n') for line in open('files/' + file_name)]
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

    for line in new_lines:
        print(line)


file_hierarcher(input("Enter file name: "))





