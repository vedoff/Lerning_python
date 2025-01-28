# Модуль с классами
import csv
import uuid


class Phonebase:
    def __init__(self, fname, lname, phonenumber):
        self.fname = fname
        self.lname = lname
        self.phonenumber = phonenumber

    def add_input_users(self):
        fname = input("Введите имя абонента:")
        lname = input("Введите фамилию абонента:")
        phonenumber = input("Введите телефон абонента:")
        return (fname, lname, phonenumber)

    def input_data(self, fname, lname, phonenumber, id=uuid.uuid4()):
        data = [(id, fname, lname, phonenumber), ]
        with open('phonebase.csv', 'a', newline='', encoding='UTF-8') as f:
            csv.writer(f).writerows(data)

    def create_base(self):
        try:
            newfile = [('ID', 'First Name', 'Last Name', 'phone')]
            with open("phonebase.csv", "x", encoding='UTF-8') as csvfile:
                csv.writer(csvfile).writerows(newfile)
        except FileExistsError:
            print("Файл базы уже создан\n")