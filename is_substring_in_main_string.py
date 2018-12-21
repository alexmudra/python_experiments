# ПЕРЕГЛЯНЕМО ЧИ ВХОДИТЬ ЕЛЕМЕНТ в СТРІНГУ ЗА ДОПОМОГОЮ (in)
# Перевіряємо чи входить підстрока(це може бути букваа/символ) в головну стрінгу

user_input = input("Enter some text: ")

if "sasha" in user_input:
    print("Cool. You guessed Sasha")
elif "anya" in user_input:
        print("You guessed Anya")
elif "girl" in user_input:
        print("You guessed Girl")
else:
    print("Try more!")

#-----------------------------------------------


print("ing" in "string")
#True    поверне тру бо підстрінга ing є в головній стрінгі string