def process_newlines(jfa_code):
    result = ""
    newline_count = 0
    for char in jfa_code:
        if char == '\n':
            newline_count += 1
        else:
            if newline_count > 0:
                result += '\n'
                for i in range(newline_count - 1):
                    result += "/n_Line;\n"
                newline_count = 0
            result += char
    if newline_count > 0:
        result += '\n'
        for i in range(newline_count - 1):
            result += "None_Line;\n"
    return result