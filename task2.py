import csv

"""""
counter = счетчик для количества ошибок
проверка по условию в цикле

"""""
f = open("game.txt", "r", encoding="UTF-8")
reader = csv.DictReader(f, delimiter="$", quotechar='"')
# file = open("game_new_count.csv", "w", encoding="UTF-8")
# writer = csv.writer(file)
counter = input()
n = 0
for line in reader:
    while n < 6:
        if str(line["characters"]) == counter:
            print(line["GameName"])
        n += 1