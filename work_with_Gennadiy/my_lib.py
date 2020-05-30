import json

#функція якій даємо рядок а вона повертає тру чи фолс Якщо перший символ великий
def is_first_upper (s):
    if len(s) == 0:
        return False
    c = s[0]
    return c.isupper()

#перевіряємо чи ключі це число
def work_gmdn (file_name):
    with open(file_name, encoding="utf8") as f:
        data = json.load(f)
        result = ""
    for k in data.keys():
        # print(k) #показати всі ід в gmdn файлі
        if k.isdigit:
            result = k, "Ce chislo"
        else:
            result = k, "Some errors"
        print(result)


def make_test_if_first_upper_in_value(file_name):
    with open(file_name, encoding="utf8") as f:
        data = json.load(f) #отримали дікт із файлу json
    for k in data:
        object_o = data[k]
        for x in object_o:
            if x == "name_uk":
                s = object_o[x]
                if not is_first_upper(s):
                    print(k,s)
