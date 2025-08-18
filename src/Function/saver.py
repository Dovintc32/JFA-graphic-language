import json, os
def save(b, c, Meaning, open_file="Data/data.json", Delete=False, a='Type'):
    Kill_file = False
    with open(open_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if Delete: del data[a][b][c]
    if not Delete: data[a][b][c] = Meaning

    with open(open_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    if Kill_file and os.path.exists(open_file): os.remove(open_file)
