import json

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

def save_l1(a, Meaning, open_file):
    if type(a) == str and ( type(Meaning) == str or type(Meaning) == int):
        with open(open_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        data[a] = Meaning
        with open(open_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    if type(a) == list and type(a) == list:
        with open(open_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for aa, men in a, Meaning:
            data[aa] = men
            with open(open_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
    if type(a) == str and type(Meaning) == list:
        with open(open_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        data[a] = Meaning
        with open(open_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)