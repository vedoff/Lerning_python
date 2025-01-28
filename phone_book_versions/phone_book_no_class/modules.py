# Функции
import csv
import uuid



# Создание файла базы

def create_base():
    try:
        newfile = [('ID','First Name','Last Name','phone')]
        with open("phonebase.csv", "x", encoding='UTF-8') as csvfile:
            csv.writer(csvfile).writerows(newfile)
    except FileExistsError:
        print("Файл базы уже создан\n")

# Добавление пользователей в базу

def add_input_users():
    fname = input("Введите имя абонента:")
    lname = input("Введите фамилию абонента:")
    phonenumber = input("Введите телефон абонента:")
    return (fname, lname, phonenumber)

def input_data(fname,lname,phonenumber,id=uuid.uuid4()):
    data = [(id, fname, lname, phonenumber),]
    with open('phonebase.csv', 'a', newline='', encoding='UTF-8') as f:
        csv.writer(f).writerows(data)


# Вывод содержимго файла базы
dict_base={}
def output_data():
    with open('phonebase.csv', 'r', newline='', encoding='UTF-8') as f:
        read_base=[line for line in csv.reader(f)]
        print(read_base)
        for i in range(len(read_base)):
            for j in read_base[i]:
                print(j)
                for k in range(len(j[i])):
                    dict_base[read_base[0][k]]=read_base[i][k]
        print(dict_base)

        # print(read_base[1])
        # print(len(read_base[1]))
        # print(read_base[1][1])
        # print(read_base[1][2])
        # print(read_base[1][3])
        # for i in range(len(read_base)):
        #     i=i+1
        # print(i)




# Поиск по базе

def find_base(fname):
    with open('phonebase.csv', 'r', newline='', encoding='UTF-8') as f:
        read_base=[line for line in csv.reader(f)]
        for line in read_base:
            print(line)