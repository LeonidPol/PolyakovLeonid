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
    header, data = reader("../monster_opportunity.csv", ",")
    for i in range(5):
        print(data[i]["power"])


main()