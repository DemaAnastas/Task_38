# В программе можно выбрать один из трёх режимов:

# w - запись нового контакта в файл phone.csv;
# r - чтение из файла phone.csv;
# c - копирование контакта из файла phone.csv в файл new_phone.csv.


from csv import DictReader, DictWriter
from os.path import exists
file_name = "phone.csv"
new_file_name = "new_phone.csv"

def get_info():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    flag = False
    while not flag:
        try: 
            phone_number = int(input("Введите телефон: "))
            if len(str(phone_number)) != 11:
                print("Неверная длина номера")
            else: 
                flag = True
        except ValueError:
            print("Невалидный номер")
            
    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding="utf=8", newline="") as data:
        f_w = DictWriter(data, fieldnames=["имя", "фамилия", "телефон"])
        f_w.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding="utf=8") as data:
        f_r = DictReader(data)
        return list(f_r)
    
def standart_write(file_name, my_lst):
    with open(file_name, 'w', encoding="utf=8", newline="") as data:
        f_w = DictWriter(data, fieldnames=["имя", "фамилия", "телефон"])
        f_w.writeheader()
        f_w.writerows(my_lst)

    
def write_file(file_name, lst):
    res = read_file(file_name)
    object = {"имя": lst[0], "фамилия": lst[1], "телефон": lst[2]}
    res.append(object)
    standart_write(file_name, res)

def copy_row(file_name=file_name, new_file_name=new_file_name):
    with open(file_name, 'r', encoding="utf=8", newline="") as data:
        f_r = DictReader(data)
        lst_1 = []
        for row in f_r:
            lst_1.append(row)
        flag = False
        while not flag:
            try:
                number = int(input("Введите номер строки: "))
                if number > len(lst_1):
                    print(f"Вводимое число не должно превышать количество строк ({len(lst_1)})!")
                else:
                    flag = True
            except ValueError:
                print("Невалидный номер")
        if not exists(new_file_name):
            create_file(new_file_name)
        res = read_file(new_file_name)
        res.append(lst_1[number - 1])
        standart_write(new_file_name, res)
            

def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "w":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует, создайте его")
                continue
            print(*read_file(file_name))
        elif command == "c":
            copy_row(file_name)

main()