import json, traceback
from Function.create_delete import cd as create_delete
from Function.saver import save as saver
from Function.Loging import loging
from Function.python_ import *



with open("Data/data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
DebugP = data["JFA SETTINGS"]["DebugP"]
Loging = data["JFA SETTINGS"]["Loging"]

with open("Data/data_cpp.json", "r", encoding="utf-8") as file:
    data_cpp = json.load(file)
file_name = data_cpp["File_name"]

with open(file_name, 'r', encoding='utf-8') as file:
    jfa_code = file.read()
    jfa_code = jfa_code.replace("\n", "")

saver(b="Win", c="Open_Win", Meaning=True)

#===========================     Parser     ===============================#

try:
    for char in jfa_code:
        if char == ";" or char == "{":
            command = command.strip()
            code[command_id] = command
            command_id += 1
            command = ""
        else: command += char

    for i, com in code.items():
        if com[0:4] == "Win.":
            if com[4:9] == 'name(':
                index = com.index('"', 10)
                saver(b="Win", c="Name", Meaning=com[10:index])
                if com[com.index('"', 10):] != '")':
                    raise SyntaxError("Win.name not close")
            if com[4:9] == "size(":
                com = com.replace(" ", "")
                indexs = [com.index(')', 10), com.index(',', 10)]
                saver(b="Win", c="SizeX", Meaning=int(com[9:indexs[1]]))
                saver(b="Win", c="SizeY", Meaning=int(com[indexs[1] + 1:indexs[0]]))
        
        if com[0:8] == "Open_Win{":
            saver(b="Win", c="Open_Win", Meaning=True)

except Exception as e:
    print(e)
    saver(b="Win", c="Open_Win", Meaning=False)
    tb = traceback.extract_tb(e.__traceback__)
    filename, line, func, text = tb[-1]
    error_info = f'JFAP: Ошибка "{type(e).__name__}" в строке {line}: "{e}"'
    errors.append(error_info)
    saver(a="JFA SETTINGS", b="Status_Programm", c="Stopped", Meaning=False)
    saver(a="JFA SETTINGS", b="Status_Programm", c="Stopped_Error", Meaning=f"{type(e).__name__}")
    saver(a="JFA SETTINGS", b="Status_Programm", c="Error_Line", Meaning=f"{line}")
    if Loging: loging("./README.md", "./Data/Log")