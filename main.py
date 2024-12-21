stroka = input("Введите строку: ")
dlina = len(stroka)  
print("Длина строки:", dlina)

glasn = "аоуаыэиёюяе"
razdel = "ьъ"
soglasn = "бвгджзйклмнпрстфхцчшщ"

count_glasnye = 0
count_soglasnye = 0

for i in stroka.lower():  
    if i in glasn:
        count_glasnye += 1  
    elif i in razdel:
        continue  
    elif i in soglasn:
        count_soglasnye += 1 

print("Количество гласных:", count_glasnye)
print("Количество согласных:", count_soglasnye)
