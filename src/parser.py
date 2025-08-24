import json, traceback, os
from Function.create_delete import cd as create_delete
from Function.saver import *
from Function.Loging import loging as logi
from Function.python_ import *
from Function.process_newlines import process_newlines
from Function.reader import *
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent.absolute()
data_file_path = PROJECT_ROOT / "Data" / "data.json"
DebugP = reader_l2("JFA SETTINGS", "DebugP", file_data)
Loging = reader_l2("JFA SETTINGS", "Loging", file_data )
data_cpp = reader_l1("File_name", file_data_cpp)

if DebugP:
    for filename in files_to_check:
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    json.load(f)
                print(f"{filename} - OK")
            except Exception as e:
                print(f"{filename} - ОШИБКА: {e}")


with open(data_cpp, "r", encoding="utf-8") as file:
    jfa_code = process_newlines(file.read())


#===========================     Parser     ===============================#

for char in jfa_code:
    if char == ";" or char == "{":
        command = command.strip()
        command += char
        code[command_id] = command
        command_id += 1
        command = ""
    else: command += char

try:
    for line, com in code.items():
        command_id
        recognized = False
        if programm_start:
            command_line += 1
            recognized = True

        # WIN WIN WIN WIN WIN WIN WIN WIN WIN WIN

        if com.startswith("Win."):
            # NAME NAME NAME NAME NAME NAME NAME NAME NAME NAME
            if com[4:9] == 'name(':
                index = com.index('"', 10)
                save_l2("Win", "Name", com[10:index], file_data)
                if com[com.index('"', 10):] != '");':
                    errors.append((line, "Win.name error"))
                    raise SyntaxError("Не грусти")
                recognized = True
            # SIZE SIZE SIZE SIZE SIZE SIZE SIZE SIZE SIZE SIZE
            if com[4:9] == "size(":
                com = com.replace(" ", "")
                indexs = [com.index(')', 10), com.index(',', 10)]
                save_l2("Win", "SizeX", int(com[9:indexs[1]]), file_data)
                save_l2("Win", "SizeY", int(com[indexs[1] + 1:indexs[0]]), file_data)
                recognized = True
            
        if com.startswith("Colorize."):
            if com[9:].startswith("background."):

                # RGBA RGBA RGBA RGBA RGBA RGBA RGBA RGBA RGBA RGBA

                if com[com.index(".", 9)+1:com.index("(")] == "rgba":
                    if com[com.index("(")+1:com.index(")")].count(",") == 3:
                        colors = list(map(int, com[com.index("(")+1:com.index(")")].replace(" ", "").split(',')))
                        colors.append(f"T{TABS}")
                        if programm_start:
                            save_l1(f"Colorize.background.rgba-{command_line}", colors, file_commands)
                            recognized = True
                        else:
                            errors.append((line, "SyntaxError", "Colorize на пределами Цикла"))
                            raise SyntaxError("Не грусти")
                    else:
                        errors.append((line, "SyntaxError", f"rgba принимает 4 значения не {com[com.index("(")+1:com.index(")")].count(",")+1}"))
                        raise SyntaxError("Не грусти")

                    # RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB
                
                elif com[com.index(".", 9)+1:com.index("(")] == "rgb":
                    if com[com.index("(")+1:com.index(")")].count(",") == 2:
                        colors = list(map(int, com[com.index("(")+1:com.index(")")].replace(" ", "").split(',')))
                        colors.append(f"T{TABS}")
                        if programm_start:
                            save_l1(f"Colorize.background.rgb-{command_line}", colors, file_commands)
                            recognized = True
                        else:
                            errors.append((line, "SyntaxError", "Colorize на пределами Цикла"))
                            raise SyntaxError("Не грусти")
                    else: 
                        errors.append((line, "SyntaxError", f"rgb принимает 3 значения не {com[com.index("(")+1:com.index(")")].count(",")+1}"))
                        raise SyntaxError("Не грусти")
                        
                

        if com.startswith("String."):
            Name = com[com.index(".")+1:com.index(" ")]
            Meaning = com[com.index('"')+1:com.index('"', com.index('"')+1)]
            save_l2("String", Name, Meaning, file_strings)
            recognized = True

        if com.startswith("Number."):
            Name = com[com.index(".")+1:com.index(" ")]
            Meaning = com[com.index(" ", com.index(" ")+1)+1:com.index(";")]
            save_l2("Numbers", Name, Meaning, file_numbers)
            recognized = True
        
        if com.startswith("Open_Win{"):
            recognized, line_OW, programm_start = True, line, True

        if com == "};":
            save_l3("JFA SETTINGS", "Status_Programm", "Open_Win", True, file_data)
            open_win_close, recognized = True, True
        
        if com == "/n_Line;": recognized = True
        if com[0] == "#": recognized = True
    
    if not recognized:
        errors.append((line, "Unknown Command"))
        raise SyntaxError("Не грусти")


except Exception as e:
    print(errors)
    save_l3("JFA SETTINGS", "Status_Programm", "Open_Win", False, file_data)
    tb = traceback.extract_tb(e.__traceback__)
    filename, line, func, text = tb[-1]
    error_info = f'JFAP: Ошибка "{type(e).__name__}" в строке {line}: "{e}"'
    if DebugP: print("\n\n\n", error_info, "\n\n\n")
    error_info2 = f'\nJFAP: Ошибка в файле \033[94m"{os.path.abspath(file_data_cpp)}"\033[0m \n"{errors[0][1]}" в линии {errors[0][0]},\n\033[31m{errors[0][2]}\033[0m\n'
    print(error_info2)
    errors.append(error_info)
    save_l3("JFA SETTINGS", "Status_Programm", "Stopped", False, file_data)
    save_l3("JFA SETTINGS", "Status_Programm", "Stopped_Error", f"{type(e).__name__}", file_data)
    save_l3("JFA SETTINGS", "Status_Programm", "Error_Line", f"{line}", file_data)
    if Loging: logi("./README.md", "./Data/Log")