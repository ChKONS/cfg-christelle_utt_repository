"""
TASK 1
Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items
Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.
"""
#PS! Printing is only for logging purposes.

class CashRegister:

    def __init__(self):
        self.total_items = {} # {'item': price}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, price):
        if type(price) != int and type(price) != float:
            return
        price -= price * self.discount
        self.total_items[item] = price
        self.total_price += price
        print(f"You have added {item} into your basket.")

    def remove_item(self, item):
        self.total_items.pop(item)
        print(f"{item.title()} is removed from your basket.")

    def apply_discount(self, discount):
        if 0 < discount < 1:
            self.discount = discount
            print(f"Discount {discount*100:02.0f}% is applied.")

    def get_total(self):
        print(f"Total price is {self.total_price:02.2f} euros.")
        return self.total_price

    def show_items(self):
        print(f"In your basket, there are: {self.total_items}.")
        return self.total_items

    def reset_register(self):
        print(f"You're basket is clear.")
        self.total_items.clear()


#EXAMPLE code run:
register = CashRegister()

#DISCOUNT
register.apply_discount(0.1)

#ADD
register.add_item("milk", 2)
register.add_item("bread", 3.50)
register.add_item("mango", 5)
register.add_item("apples", 4)

#DELETE
register.remove_item("mango")

#SHOW ITEMS
register.show_items()

#GET TOTAL
register.get_total()

#CLEAR
register.reset_register()

"""
TASK 2
Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.
Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 
"""
#PS! Printing is only for logging purposes.

import statistics

class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = {} #{'subject': grade}

class CFGStudent(Student):

    average_mark = 0

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade
        print(f"{subject.title()} added into the the timetable.")

    def remove_subject(self, subject):
        self.subjects.pop(subject)
        print(f"{subject.title()} is removed from the timetable.")

    def change_subject_grade(self, subject, new_grade):
        self.subjects[subject]=new_grade
        print(f"Now {subject} grade for {self.name} (id:{self.id}) is {new_grade}.")

    def show_all_subjects_and_grades(self):
        print(f"{self.name} (id:{self.id}) subjects are: {self.subjects}.")
        return self.subjects

    def student_average_mark(self):
        self.average_mark = statistics.mean(list(self.subjects.values()))
        print(f"{self.name} (id:{self.id}) average mark is: {self.average_mark:02.2f}.")
        return self.average_mark

#CREATING A STUDENT
anna = CFGStudent('Anna Smith', 21, 1001)

#ADDING SUBJECTS TO THE STUDENT
anna.add_subject("Math", 70)
anna.add_subject("Python", 55)
anna.add_subject("HTML", 87)

#REMOVE SUBJECT
anna.remove_subject("HTML")

#CHANGING SUBJECT GRADE
anna.change_subject_grade("Math", 69)

#STUDENT AVERAGE MARK
anna.student_average_mark()

#SHOWING ALL STUDENT SUBJECTS AND GRADES
anna.show_all_subjects_and_grades()
