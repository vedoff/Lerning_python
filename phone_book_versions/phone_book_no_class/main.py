import modules as modules
import class_modules as class_modules

# Меню

while True:
    menu = input("1.Создания файла базы\n"
                 "2.Создание абонентов\n"
                 "3.Показать все контакты\n"
                 "4.Найти контакт\n"
                 "5.Изменить контакт\n"
                 "6.Удалить контакт\n"
                 "Для выхода из меню наберите 'Exit'\n")
    if menu == "Exit" or menu == "exit":
        break
    elif menu == "1":
        # modules.create_base()
        phonebase= class_modules.Phonebase(fname=None, lname=None, phonenumber=None)
        phonebase.create_base()
    elif menu == "2":
        fname = input("Введите имя абонента:")
        if fname.isdigit():
            print("В имени допускаются только буквы")
            continue
        lname = input("Введите фамилию абонента:")
        if lname.isdigit():
            print("В фамилии допускаются только буквы")
            continue
        phonenumber = input("Введите телефон абонента:")
        if phonenumber.isdigit() == False:
            print("В номере телефона допускаются только цифры")
            continue
        modules.input_data(fname, lname, phonenumber)
    elif menu == "3":
        modules.output_data()
    elif menu == "4":
        find_name = input("Введите фамилию абонента:")
        if find_name.isdigit():
            print("В фамилии допускаются только буквы")
            continue
        modules.find_base(find_name)
    else:
        print("!!! Используйте соответствующие цифры для активации пунктов меню !!!\n")



# if __name__ == "__main__":
#     modules.input_data(fname,lname,phonenumber)



# # Непосредственная запись в CSV файл
# with open('output.csv', 'x', newline='') as f:
#     csv.writer(f).writerows(data)

# # Непосредственная запись в JSON файл
# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(data,f, ensure_ascii=False, indent=4)

