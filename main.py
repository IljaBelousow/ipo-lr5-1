slovo = input("Введите слово: ")
dlina = len(slovo)  # Длина слова
print("Длина слова:", dlina)

glasn = "аоуаыэиёюяе"
razdel = "ьъ"

for i in slovo:  # Проходим по каждому символу в слове
    if i in glasn:
        print(i, "- гласная")
    elif i in razdel:
        print(i, "- разделительный")
    else:
        print(i, "- согласный")
