from data_mark import DATA


def bachelor_scholarship(name, group, avg_rate):
    for element in DATA:
        if avg_rate == element['max_rate']: # Если оценка = 5
            return element['scholarship_bachelor']
        elif element['min_rate'] < avg_rate < element['max_rate']: # Если оценка от 4 до 5
            return element['scholarship_bachelor']
        elif element['min_rate'] <= avg_rate < element['max_rate']: # Если оценка от 3 до 4
            return element['scholarship_bachelor']
    else:
        return 'С данным средним баллом студент не может иметь степендию'
    

def graduate_scholarship(name, group, avg_rate):
    for element in DATA:
        if avg_rate == element['max_rate']: # Если оценка = 5
            return element['scholarship_graduate']
        elif element['min_rate'] < avg_rate < element['max_rate']: # Если оценка от 4 до 5
            return element['scholarship_graduate']
        elif element['min_rate'] <= avg_rate < element['max_rate']: # Если оценка от 3 до 4
            return element['scholarship_graduate']
    else:
        return 'С данным средним баллом студент не может иметь степендию'
    

# проверки
# a = bachelor_scholarship('Student1', 1011, 2)
# b = bachelor_scholarship('Student2', 1011, 4)
# c = graduate_scholarship('Student3',1012, 2.54)
# d = graduate_scholarship('Student4',1012, 4.22)
# print(a)
# print(b)
# print(c)
# print(d)