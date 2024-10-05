class Person:
    def __init__(self, full_name, age , is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):

        print(self.__dict__)


class Student(Person):
    def __init__(self, full_name, age, is_married):
        super().__init__(full_name, age, is_married)
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def average_rating(self):
        print(f"средняя оценка по всем предметам {sum(self.marks.values()) // len(self.marks.values())}")


class Teacher(Person):
    base_salary = 30000
    def __init__(self ,full_name, age , is_married, experience):
        super().__init__( full_name, age , is_married)
        self.experience = experience

    def counter(self):
        if self.experience > 3:
            self.experience -= 3
            self.base_salary += self.base_salary * (self.experience * 5) // 100
        print(self.base_salary)


obj = Teacher('Людмила Анатольевна', 58, True, 5)

obj.introduce_myself()
obj.counter()

def create_students():
    obj1 = Student('Данилa Сарапулов', 18, False)
    obj2 = Student('Максим Тарасов', 18, False)
    obj3 = Student('Анастасия Буланова', 18, False)
    return [obj1, obj2, obj3]

for i in create_students():
    i.add_mark("Химия", 4)
    i.add_mark("Матем", 3)
    i.add_mark("Биология", 5)
    i.average_rating()
    i.introduce_myself()


