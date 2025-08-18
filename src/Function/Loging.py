import datetime, json, os


def loging(readme_path, Save_path):

    now = datetime.datetime.now()
    Name = f"Log_{now.strftime('%Y-%m-%d_%H-%M-%S')}"

    with open("./Data/data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    logi = data["JFA SETTINGS"]["Loging"]
    Stopped = data["JFA SETTINGS"]["Status_Programm"]["Stopped"]
    Stopped_Error = data["JFA SETTINGS"]["Status_Programm"]["Stopped_Error"]
    Error_Line = data["JFA SETTINGS"]["Status_Programm"]["Error_Line"]


    if logi:
        with open(f"{Save_path}/{Name}.log", "a", encoding="utf-8") as log_file:
            with open(readme_path, "r", encoding="utf-8") as readme_file:
                lines = readme_file.readlines()
                if lines:
                    last_line = lines[-1].rstrip()
                    Prelast_line = lines[-2].rstrip()
                else:
                    last_line = "Пустой файл"
            log_file.write(f"=============== | {"-"*len(last_line)} | ===============\n")
            log_file.write(f"=============== | {last_line} | ===============\n")
            log_file.write(f"=============== | {"-"*len(last_line)} | ===============\n\n")
            log_file.write(f"{Prelast_line[:19]} {last_line} | {Prelast_line[21:]} |\n")
            log_file.write(f"Путь к запущеному файлу: '{os.path.dirname(os.path.abspath(__file__))}'\n")
            log_file.write(f"Путь к .log файлам: '{Save_path}'\n")
            now = datetime.datetime.now()
            Start_Time = now.strftime('%Y.%m.%d %H:%M:%S')
            log_file.write(f"Дата Запуска: '{Start_Time}'\n\n")
            if Stopped:
                log_file.write("| PROGRAMM STOPPED |\n")
                log_file.write(f"| Ошибка: {Stopped_Error} |\n")
                log_file.write(f"| Линия: {Error_Line} |\n")
                log_file.write("| PROGRAMM STOPPED |\n")

    else: 
        return "JFAP: Debug is Disable, Enable it: jfa -L"

    data["JFA SETTINGS"]["Status_Programm"]["Stopped"] = False