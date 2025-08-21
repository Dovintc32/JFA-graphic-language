import json, traceback
from Function.create_delete import cd as create_delete
from Function.saver import *
from Function.Loging import loging as logi
from Function.python_ import *
from pathlib import Path


    
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
data_file_path = PROJECT_ROOT / "Data" / "data.json"

with open(data_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
DebugP = data["JFA SETTINGS"]["DebugP"]
Loging = data["JFA SETTINGS"]["Loging"]

if DebugP:
    files_to_check = [
        "Data/data.json",
        "Data/Variables/number.json", 
        "Data/Variables/string.json",
        "Data/data_cpp.json"
    ]

    for filename in files_to_check:
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    json.load(f)
                print(f"✓ {filename} - OK")
            except Exception as e:
                print(f"✗ {filename} - ОШИБКА: {e}")

with open("Data/data_cpp.json", "r", encoding="utf-8") as file:
    data_cpp = json.load(file)
file_data_cpp = data_cpp["File_name"]

with open(f"{file_data_cpp}", 'r', encoding='utf-8') as file:
    jfa_code = file.read()
    jfa_code = jfa_code.replace("\n", "")
    

#===========================     Parser     ===============================#


try:
    for char in jfa_code:
        if char == ";" or char == "{":
            command = command.strip()
            command += char
            code[command_id] = command
            command_id += 1
            command = ""
        else: command += char
    
    for line, com in code.items():
        recognized = False

        if com.startswith("Win."):
            
            if com[4:9] == 'name(':
                index = com.index('"', 10)
                save_l2("Win", "Name", com[10:index], file_data)
                if com[com.index('"', 10):] != '");':
                    errors.append((line, "Win.name error"))
                    raise SyntaxError("Не грусти")
                recognized = True
            if com[4:9] == "size(":
                com = com.replace(" ", "")
                indexs = [com.index(')', 10), com.index(',', 10)]
                save_l2("Win", "SizeX", int(com[9:indexs[1]]), file_data)
                save_l2("Win", "SizeY", int(com[indexs[1] + 1:indexs[0]]), file_data)
                recognized = True
        
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
            recognized, open_win_close, line_OW = True, False, line
    
        if com == "};":
            save_l3("JFA SETTINGS", "Status_Programm", "Open_Win", True, file_data)
            open_win_close, recognized = True, True
    
    if not recognized:
        errors.append((line, "Unknown Command"))
        raise SyntaxError("Не грусти")


except Exception as e:
    save_l3("JFA SETTINGS", "Status_Programm", "Open_Win", False, file_data)
    tb = traceback.extract_tb(e.__traceback__)
    filename, line, func, text = tb[-1]
    error_info = f'JFAP: Ошибка "{type(e).__name__}" в строке {line}: "{e}"'
    print(error_info)
    errors.append(error_info)
    save_l3("JFA SETTINGS", "Status_Programm", "Stopped", False, file_data)
    save_l3("JFA SETTINGS", "Status_Programm", "Stopped_Error", f"{type(e).__name__}", file_data)
    save_l3("JFA SETTINGS", "Status_Programm", "Error_Line", f"{line}", file_data)
    if Loging: logi("./README.md", "./Data/Log")

