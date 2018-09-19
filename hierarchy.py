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
    roman_numerals = ('I.', 'II.', 'III.', 'IV.', 'V.', 'VI.', 'VII.', 'VIII.', 'IX.', 'X.')
    uppercase_letters = ('A.', 'B.', 'C.', 'D.', 'E.', 'F.', 'G.', 'H.', 'J.', 'K.', 'L.', 'M.', 'N.', 'O.', 'P.', 'Q.')
    undercase_letters = ('a.', 'b.', 'c.', 'd.', 'e.', 'f.', 'g.', 'h.', 'i.', 'j.', 'k.', 'l.', 'm.', 'n.', 'o.', 'p.', 'q.')
    undercase_letters_parenthesis = ('a.)', 'b.)', 'c.)', 'd.)', 'e.)', 'f.)', 'g.)', 'h.)', 'i.)', 'j.)', 'k.)', 'l.)', 'm.)', 'n.)', 'o.)', 'p.)', 'q.)')
    numbers = ('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.')
    numbers_parenthesis = ('1.)', '2.)', '3.)', '4.)', '5.)', '6.)', '7.)', '8.)', '9.)', '10.)')
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
                if line.startswith(roman_numerals):
                    curr_tab = ''
                    new_line = curr_tab + line.rstrip()
                elif line.startswith(uppercase_letters):
                    curr_tab = '        '
                    new_line = curr_tab + line.rstrip('/n')
                elif line.startswith(numbers_parenthesis):
                    curr_tab = '                        '
                    new_line = curr_tab + line.rstrip()
                elif line.startswith(undercase_letters_parenthesis):
                    curr_tab = '                            '
                    new_line = curr_tab + line.rstrip()
                elif line.startswith(numbers):
                    curr_tab = '                '
                    new_line = curr_tab + line.rstrip()
                elif line.startswith(undercase_letters):
                    curr_tab = '                    '
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





