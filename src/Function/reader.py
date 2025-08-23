import json

def reader_l1(a, path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file) 
    return data[a]

def reader_l2(a, b, path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file) 
    return data[a][b]