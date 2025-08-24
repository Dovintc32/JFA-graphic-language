
import pygame
import json
import subprocess
import sys
import os

def load_json(file_path):
    """Загрузка JSON файла"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_json(data, file_path):
    """Сохранение данных в JSON файл"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    # Создаем JSON файл с параметрами
    j = {"File_name": sys.argv[1] if len(sys.argv) > 1 else ""}
    with open("Data/data_python.json", 'w') as f:
        json.dump(j, f, indent=4)
    
    # Запускаем Python скрипт парсера
    try:
        subprocess.run([sys.executable, "src/parser.py"], check=True)
    except subprocess.CalledProcessError:
        print("Ошибка запуска parser.py")
        return
    
    number_data = load_json("Data/Variables/number.json")
    string_data = load_json("Data/Variables/string.json")
    commands_data = load_json("Data/Variables/commands.json")
    data = load_json("Data/data.json")
    name = data.get("Win", {}).get("Name", "")
    size_x = data.get("Win", {}).get("SizeX", 800)
    size_y = data.get("Win", {}).get("SizeY", 600)
    open_win = data.get("JFA SETTINGS", {}).get("Status_Programm", {}).get("Open_Win", False)
    
    pygame.init()
    
    if open_win:
        screen = pygame.display.set_mode((size_x, size_y))
        pygame.display.set_caption(name)    
        running = True
        clock = pygame.time.Clock()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                for key, value in commands_data.items():
                    if key[key.index("-")+1:key.index("-", key.index("-")+1)] == "Colorize.background.rgb":
                        value = value.replace(" ", "")
                        r, g, b = map(int, value.split(","))
                        screen.fill((r, g, b))
                    if key[key.index("-")+1:key.index("-", key.index("-")+1)] == "if":
                        yslovie = value
                        print(repr(yslovie))
                        print(yslovie)
                        if value == True:
                            print("Mne")
                    
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
    
    data["Win"] = {
        "Name": "",
        "SizeX": 0,
        "SizeY": 0
    }
    data["JFA SETTINGS"]["Status_Programm"] = {
        "Error_Line": "",
        "Stopped": False,
        "Open_Win": False
    }
    number_data["Numbers"] = {}
    string_data["String"] = {}
    commands_data = {}
    
    save_json(commands_data, "Data/Variables/commands.json")
    save_json(number_data, "Data/Variables/number.json")
    save_json(string_data, "Data/Variables/string.json")
    
    with open("Data/data.json", 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    main()