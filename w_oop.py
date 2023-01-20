from data_mark import DATA

class Bachelor:

    def __init__(self,name,group,avg_rate):
        self.name = name
        self.group = group
        self.avg_rate = avg_rate
        self.DATA = DATA

    def bachelor_scholarship(self):
        for element in self.DATA:
            self.min_rate = element['min_rate']
            self.max_rate = element['max_rate']
            if self.avg_rate == self.max_rate: # Если оценка = 5
                return element['scholarship_bachelor']
            elif self.min_rate < self.avg_rate < self.max_rate: # Если оценка от 4 до 5
                return element['scholarship_bachelor']
            elif self.min_rate <= self.avg_rate < self.max_rate: # Если оценка от 3 до 4
                return element['scholarship_bachelor']
        else:
            return 'С данным средним баллом студент не может иметь степендию'

class Graduate(Bachelor):

    def graduate_scholarship(self):
        for element in self.DATA:
            self.min_rate = element['min_rate']
            self.max_rate = element['max_rate']
            if self.avg_rate == self.max_rate: # Если оценка = 5
                return element['scholarship_graduate']
            if self.min_rate < self.avg_rate < self.max_rate: # Если оценка от 4 до 5
                return element['scholarship_graduate']
            if self.min_rate <= self.avg_rate < self.max_rate: # Если оценка от 3 до 4
                return element['scholarship_graduate']
        else:
            return 'С данным средним баллом студент не может иметь степендию'   

# проверки
# a = Bachelor('Student1', 1011, 2)
# b = Bachelor('Student2', 1011, 4)
# c = Graduate('Student3',1012, 2.54)
# d = Graduate('Student4',1012, 4.22)
# print(a.bachelor_scholarship())
# print(b.bachelor_scholarship())
# print(c.graduate_scholarship())
# print(d.graduate_scholarship())