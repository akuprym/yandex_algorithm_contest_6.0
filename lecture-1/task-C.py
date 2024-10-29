n = int(input())
table = [input() for _ in range(n)]

def find_lines(table, x) -> list[list[int]]:
    lines = []
    current_line = []
    in_line = False
    for y in range(len(table)):
        if table[y][x] == "#":
            if not in_line:
                in_line = True
                current_line.append(y)
        else:
            if in_line:
                current_line.append(y)
                lines.append(current_line)
                current_line = []
                in_line = False
    else:
        if in_line:
            current_line.append(y + 1)
            lines.append(current_line)
    return lines


def determine_letter(table):
    status = 'find_first_lines'

    for x in range(len(table[0])):
        lines = find_lines(table, x)

        if status == 'find_first_lines':
            if len(lines) == 1:
                status = 'find_i'
                check_lines = lines
            elif len(lines) > 1:
                return 'X'
        elif status == 'find_i':
            if len(lines) == 0:
                status = 'i_end'
            elif len(lines) == 1:
                if lines[0] == check_lines[0]:
                    continue
                elif lines[0][1] == check_lines[0][1] and lines[0][0] > check_lines[0][0]:
                    status = 'find_l'
                    check_lines = lines
                elif lines[0][0] > check_lines[0][0] and lines[0][1] < check_lines[0][1]:
                    status = 'find_h'
                    left_intervals = check_lines
                    check_lines = lines
                else:
                    return 'X'
            elif len(lines) == 2:
                if lines[0][0] == check_lines[0][0] and lines[1][1] < check_lines[0][1]:
                    status = 'find_p'
                    check_lines = lines
                elif lines[0][0] == check_lines[0][0] and lines[1][1] == check_lines[0][1]:
                    status = 'find_c'
                    left_intervals = check_lines
                    check_lines = lines
                else:
                    return 'X'
            else:
                return 'X'
        elif status == 'find_l':
            if len(lines) == 0:
                status = 'l_end'
            elif len(lines) == 1:
                if lines[0] != check_lines[0]:
                    return 'X'
            else:
                return 'X'
        elif status == 'find_h':
            if len(lines) == 1:
                if lines[0] == check_lines[0]:
                    continue
                elif left_intervals[0] == lines[0]:
                    status = 'right_h'
                    check_lines = lines
                else:
                    return 'X'
            else:
                return 'X'
        elif status == 'right_h':
            if len(lines) == 0:
                status = 'h_end'
            elif len(lines) == 1:
                if lines[0] != check_lines[0]:
                    return 'X'
            else:
                return 'X'
        elif status == 'find_p':
            if len(lines) == 2:
                if lines != check_lines:
                    return 'X'
            elif len(lines) == 1:
                if lines[0][0] == check_lines[0][0] and lines[0][1] == check_lines[1][1]:
                    status = 'p_right'
                    check_lines = lines
                else:
                    return 'X'
            else:
                return 'X'
        elif status == 'p_right':
            if len(lines) == 0:
                status = 'p_end'
            elif len(lines) == 1:
                if lines[0] != check_lines[0]:
                    return 'X'
            else:
                return 'X'
        elif status == 'find_c':
            if len(lines) == 0:
                status = 'c_end'
            elif len(lines) == 2:
                if lines != check_lines:
                    return 'X'
            elif len(lines) == 1:
                if lines == left_intervals:
                    status = 'find_o'
                    check_lines = lines
                else:
                    return 'X'
            else:
                return 'X'
        elif status == 'find_o':
            if len(lines) == 0:
                status = 'o_end'
            elif len(lines) == 1:
                if lines == check_lines:
                    continue
                else:
                    return 'X'
            else:
                return 'X'
        elif status == 'i_end' or status == 'l_end' or status == 'h_end' or status == 'p_end' or status == 'c_end' or status == 'o_end':
            if len(lines) != 0:
                return 'X'
    else:
        if status == 'i_end' or status == 'find_i':
            return 'I'
        elif status == 'l_end' or status == 'find_l':
            return 'L'
        elif status == 'h_end' or status == 'right_h':
            return 'H'
        elif status == 'p_end' or status == 'p_right':
            return 'P'
        elif status == 'c_end' or status == 'find_c':
            return 'C'
        elif status == 'o_end' or status == 'find_o':
            return 'O'
        else:
            return 'X'

print(determine_letter(table))