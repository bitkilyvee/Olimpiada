import csv
""""
file - новый файл с измененными данными
цикл с проверкой исловия( число 55 присутствует в значении ошибки)
запись полученных(измененных) значений в новый файл

"""
f = open("game.txt", "r", encoding="UTF-8")
reader = csv.DictReader(f, delimiter="$", quotechar='"')
file = open("game_new.csv", "w", encoding="UTF-8")
writer = csv.writer(file)
writer.writerow(["GameName", "characters", "nameError", "date"])
for line in reader:
    if "55" in line["nameError"]:
        print("У персонажа " + line["characters"] + " в игре " + line["GameName"] + " нашлась ошибка с кодом " + line[
            "nameError"] + " дата фиксации: " + line["date"])
        writer.writerow([line["GameName"], line["characters"], "Done", "0000-00-00"])
