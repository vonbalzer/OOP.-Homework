class Student:
    grades_lector_python = []
    grades_lector_git = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}
        self.gradess = []
        self.sum_of_ratings = 0
        self.number_of_ratings = 0

    def rate_lector(self, lector, course, grade):
        lector.lecture_scores += grade

        if course in 'Python':
            Student.grades_lector_python += grade
        elif course in 'Git':
            Student.grades_lector_git += grade

        if course in lector.gradess:
            lector.gradess[course] += grade
        else:
            lector.gradess[course] = grade

    def average_all_lector(lector_python, lector_git):

        average_phyton = sum(lector_python) / len(lector_python)
        print(F'Средняя оценка за курс у лекторов по "Phyton": {average_phyton}')

        average_git = sum(lector_git) / len(lector_git)
        print(F'Средняя оценка за курс у лекторов по "Git": {average_git}')

    def socer_student(self, num):
        for val in num:
            self.sum_of_ratings += val
            self.number_of_ratings += 1
            self.average_rating = self.sum_of_ratings / self.number_of_ratings

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {round(self.average_rating, 1)}\n' \
               f'Курсы в процессе изучения: {self.courses_in_progress[0]}, {self.courses_in_progress[1]} \n' \
               f'Завершенные курсы: {self.finished_courses[0]}\n'

    def __gt__(self, other):
        if self.average_rating > other.average_rating:
            return f'Лучший студент: {self.name} с рейтингом: {self.average_rating}'
        else:
            return f'Лучший студент: {other.name} с рейтингом: {other.average_rating}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    lecture_scores = []
    gradess = {}
    curs = []
    sum_of_ratings = 0
    number_of_ratings = 0
    average_rating = 0

    def socer(self, num):
        for val in num:
            self.sum_of_ratings += val
            self.number_of_ratings += 1
        self.average_rating = self.sum_of_ratings / self.number_of_ratings

    def __str__(self):

        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {round(self.average_rating, 1)}'

    def __gt__(self, other):
        if self.average_rating > other.average_rating:
            return f'Лучший лектор: {self.name} с рейтингом: {round(other.average_rating, 1)}'
        else:
            return f'Лучший лектор: {other.name} с рейтингом: {round(other.average_rating, 1)}'

class Reviewer(Mentor):
    courses_attacheds = []
    courses_grades = []
    curse_phyton = []
    curse_git = []
    grades_all_phyton = []
    grades_all_git = []

    def rate_hw(self, student, course, grade):
        student.gradess += grade
        if course in 'Python':
            Reviewer.grades_all_phyton += grade
        elif course in 'Git':
            Reviewer.grades_all_git += grade
        if course in student.grades_student:
            student.grades_student[course] += grade
        else:
            student.grades_student[course] = grade

    def average_all_curs(phyton, git):

        average_phyton = sum(phyton) / len(phyton)
        print(F'Средняя оценка на курсе у учеников по "Phyton": {average_phyton}')

        average_git = sum(git) / len(git)
        print(F'Средняя оценка на курсе у учеников по "Git": {average_git}')
        print()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


some_student1 = Student('Ruoy', 'Eman', 'your_gender')
some_student1.courses_in_progress += ['Python', 'Git']
some_student1.finished_courses += ['Введение в программирование']

some_mentor1 = Reviewer('Some', 'Buddy')
some_mentor1.courses_attacheds += ['Python', 'Git']
some_mentor1.rate_hw(some_student1, 'Python', [10, 10, 7, 10, 10])
some_mentor1.rate_hw(some_student1, 'Git', [10, 6, 4, 10, 10])

some_student2 = Student('Olya', 'Shatilova', 'your_gender')
some_student2.courses_in_progress += ['Python', 'Git']
some_student2.finished_courses += ['Введение в программирование']

some_mentor2 = Reviewer('Bonny', 'Sam')
some_mentor2.courses_attacheds += ['Python', 'Git']
some_mentor2.rate_hw(some_student2, 'Python', [10, 10, 9, 10, 10])
some_mentor2.rate_hw(some_student2, 'Git', [10, 10, 10, 10, 10])

print('Проверяющие')
print()

some_lector1 = Lecturer('Pavel', 'Shatilov')
some_lector1.curs += ['Python', 'Git']
some_student2.rate_lector(some_lector1, 'Python', [10, 1, 9, 10, 10])
some_student1.rate_lector(some_lector1, 'Git', [10, 9, 10, 6, 10])

some_lector2 = Lecturer('Some', 'Buddy')
some_lector2.curs += ['Python', 'Git']
some_student2.rate_lector(some_lector2, 'Python', [10, 10, 9, 10, 10, 10])
some_student2.rate_lector(some_lector2, 'Git', [10, 5, 10, 6, 5])

print(some_mentor1)
print()

print(some_mentor2)
print()

print('Студенты')
print()

some_student1.socer_student(some_student1.gradess)
print(some_student1)

some_student2.socer_student(some_student2.gradess)
print(some_student2)

print('Лекторы')
print()

some_lector1.socer(some_lector1.lecture_scores)

print(some_lector1)
print()

some_lector2.socer(some_lector2.lecture_scores)
print(some_lector2)
print()

print(some_lector1 < some_lector2)
print()

print(some_student2 > some_student1)
print()

Reviewer.average_all_curs(Reviewer.grades_all_phyton, Reviewer.grades_all_git)

Student.average_all_lector(Student.grades_lector_python, Student.grades_lector_git)