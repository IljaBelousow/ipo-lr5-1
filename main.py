slovo = str(input("vvedite slovo "))
dlina = len(slovo)#длина слова
print("dlina: ", dlina)
for i in slovo:#проходит по каждому символу slovo
    if i == "а" or i == "о" or i == "у" or i == "ы" or i == "э" or i == "и" or i == "е" or i == "ё" or i == "ю" or i == "я":
        print(i, " - гласная")
    elif i == "ь" or i =="ъ":
        print(i, " - разделительный")
    else:
        print(i, " - согласный")