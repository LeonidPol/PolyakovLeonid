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
    sett = {}
    for monster in data:
        if monster["MonsterName"] not in sett:
            sett[monster["MonsterName"]] = 0
        sett[monster["MonsterName"]] += float(monster["attack"])
    names = list(sett.keys())[:10]
    for n in names:
        print(n, sett[n])





main()