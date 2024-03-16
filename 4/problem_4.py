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
    print(header)
    ability = {"усиление атаки": "attack", "регенерация":  "health", "дополнительный ход": "speed"}
    monsters_exp = []
    for monster in data:
        exp = 0
        for r in ['attack', 'health',  'speed', "protection"]:
            num = float(monster[r])
            mult = 1
            to_ab = ability[monster["opportunity"]]
            if to_ab == r:
                mult = 1.5
            exp = exp + mult*num
        corrected_monster = []
        corrected_monster = [monster["MonsterName"], exp]
        monsters_exp.append(corrected_monster)
    print(monsters_exp)
    for i in range(10):
        print(monsters_exp[i][0]+":"+str(monsters_exp[i][1]))




main()