import json, os
def save_l3(a, b, c, Meaning, open_file):
    with open(open_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    data[a][b][c] = Meaning
    with open(open_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def save_l2(a, b, Meaning, open_file):
    with open(open_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    data[a][b] = Meaning
    with open(open_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)