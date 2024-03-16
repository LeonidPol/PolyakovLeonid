import csv

def reader(route, d):
    """
    Функция читает файлы из текстового файла
    Вход: путь к файлу и разделитель csv
    """
    headers = []
    data = []
    with open(route, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=d)
        flag = True
        for row in reader:
            if flag:
                headers = row
                flag = False
                continue
            user = {}
            for ind in range(0, len(headers)):
                user[headers[ind]] = row[ind]
            data.append(user)
    return headers, data

def main():
    header, data = reader("../monster_game.txt", "$")
    while True:
        name = input()
        if name == "мир":
            break
        ident = None
        for m in data:
            if m["MonsterName"] == name:
                ident = m
                break
                print(m)
        if ident is None:
            print("Ого, вам попался новый монстр! БЕГИТЕ!")
        else:
            print(f'{m["MonsterName"]}: {m["attack"]}, {m["protection"]}, {m["health"]}, {m["speed"]}')




main()