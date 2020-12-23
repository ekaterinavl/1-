def Read():  # ключ - название должности, значение - количество ставок
    _dict = {}  # основной словарь
    _dict_little = {}  # словарь для значений каждого отдела или сотрудника
    row = ""

    f = open("input.txt", 'r', encoding='utf-8')
    list = f.read()

    for elem in list:
        if elem == ':':
            key = row
            row = ""
            continue
        if elem == "\n":
            value = row
            row = ""
            if value == "":
                gl_key = key
                _dict_little = {}
            else:
                _dict_little[key] = value
                _dict[gl_key] = _dict_little
            continue
        row = row + elem
        if row == " ":
            row = ""

    f.close()
    return _dict

class Otdel:
    def Info(self):
        list_of_dep = Read()

        for Key, Values in list_of_dep.items():
            print(Key)
            for Person in Values.items():
                print(Person[0], ":", Person[1], " стави(ок)")
            print()

    def List(self):
        dict = Read()
        Positions = []
        State = []

        for Key, Values in dict.items():
            for Position, Rate in Values.items():
                if (Key.split())[0] != "Сотрудник":
                    Positions.append(Position)
                    Positions.append(Rate)
                else:
                    State.append(Position)
                    State.append(Rate)

        return [Positions, State]

class Employee:
    def List(self):
        dict = Read()
        Employees = []

        for Key, Values in dict.items():
            if (Key.split())[0] == "Сотрудник":
                Employees.append(Key.split()[1] + " " + Key.split()[2])

        return Employees

    def NewPerson(self):
        self.name = input("Введите фамилию и имя нового сотрудника: ")
        f = open("input.txt", 'a', encoding='utf-8')
        f.write('Сотрудник ')
        f.write(self.name)
        f.write(':\n-:-\n\n')
        f.close()
        print("Ура! Сотрудник успешно добавлен!\n")

    def Employment(self):
        Employees = Employee.List(self)
        List = Otdel.List(self)
        Positions = List[0]
        State = List[1]

        print("\nВыберите сотрудника:")
        for i in range(0, len(Employees)):
            print(i + 1, '-', Employees[i])

        s = int(input("\nВведите номер: ")) - 1

        print("\nДоступные должности:")
        for i in range(0, len(Positions)):
            if i % 2 == 0:
                if i == 0:
                    print(1, '-', Positions[i])
                else:
                    print((i // 2) + 1, '-', Positions[i])

        p_n = input("\nВведите номер должности и количество ставок через пробел: ")
        (p, n) = p_n.split(' ')
        index = (int(p) - 1) * 2
        name = Positions[index]
        kol_rates = int(Positions[index + 1])
        count = 0

        for i in range(0, len(State)):
            if State[i] == name:
                try:
                    count = count + int(State[i + 1])
                except Exception:
                    count = count + float(State[i + 1])  #дробные ставки

        free_rates = kol_rates - count

        print('\nСвободные ставки:', free_rates, '\nВыбрано ставок для трудоустройства:', n)

        if float(n) > free_rates:
            print("Нет свободных ставок. В трудоустройстве отказано.\n")
        else:
            f = open("input.txt", "r", encoding='utf-8')
            lines = f.readlines()
            f.close()
            f = open("input.txt", "w", encoding='utf-8')
            for k in range(0, len(lines)):
                if lines[k] == ("Сотрудник " + Employees[s] + ":\n"):
                    if lines[k + 1] == "-:-\n":
                        lines[k + 1] = name + ": " + n + "\n"
                    else:
                        for i in range(k + 1, len(lines)):
                            if lines[i] == "\n":
                                lines[i] = name + ": " + n + "\n\n"
                                break
                f.write(lines[k])
            f.close()
            print("Сотрудник", Employees[s], "трудоустроен на", n, "ставку(и) должности", name, "\n")

    def Dismissal(self):
        Employees = Employee.List(self)
        print("\nВыберите сотрудника:")

        for i in range(0, len(Employees)):
            print(i + 1, '-', Employees[i])

        s = int(input("\nВведите номер: ")) - 1
        emp = "Сотрудник " + Employees[s]
        dict = Read()
        list = []

        for Key, Values in dict.items():
            if Key == emp:
                for Position, Rate in Values.items():
                    if Position != "-":
                        list.append(Position + ": " + Rate)
                    else:
                        print("Сотрудник нигде не работает. Может пора уже?\n")
                        return

        print("\nЗанимаемые должности и количество ставок:")
        for i in range(0, len(list)):
            print(i + 1, '-', list[i])

        n = int(input("\nВведите номер: ")) - 1
        name = list[n]
        list.pop(n)
        list.append("\n")

        f = open("input.txt", 'r', encoding='utf-8')
        lines = f.readlines()
        f.close()
        f = open("input.txt", "w", encoding='utf-8')

        for k in range(0, len(lines)):
            if lines[k] == emp + ":\n":
                if len(list) > 1:
                    for i in range(k + 1, k + 1 + len(list)):
                        lines[i] = list[i - k - 1]
                else:
                    lines[k + 1] = "-:-\n"
            f.write(lines[k])
        f.close()
        print("Сотрудник", Employees[s], "успешно уволен с должности", name, "\n")

    def Delete(self):
        Employees = Employee.List(self)
        print("\nВыберите сотрудника:")

        for i in range(0, len(Employees)):
            print(i + 1, '-', Employees[i])

        s = int(input("\nВведите номер: ")) - 1
        emp = "Сотрудник " + Employees[s]
        dict = Read()
        list = []

        for Key, Values in dict.items():
            if Key == emp:
                for Position, Rate in Values.items():
                    if Position != "-":
                        list.append(Position + ": " + Rate)

        if len(list) == 0:
            f = open("input.txt", 'r', encoding='utf-8')
            lines = f.readlines()
            f.close()
            f = open("input.txt", "w", encoding='utf-8')

            for k in range(0, len(lines)):
                if lines[k] == emp + ":\n":
                    lines[k] = lines[k + 1] = lines[k + 2] = ""
                f.write(lines[k])
            f.close()
            print(emp, "успешно удален", "\n")
        else:
            print("Ой! А Вы уверены? Этот сотрудник все еще у нас работает. Его бы для начала уволить.\n")
            return


d = Otdel()
p = Employee()

while True:
    print('Список команд:\n1 - Информация об отделах, существующих сотрудниках и их должностях\n2 - Трудоустроить сотрудника\n'
          '3 - Уволить бездаря\n4 - Создать нового сотрудника\n5 - Удалить сотрудника\n6 - поставить "5"\n0 - Завершить программу')
    s = input("\nВведите номер команды: ")
    if s == '1':
        d.Info()
    if s == '2':
        p.Employment()
    if s == '3':
        p.Dismissal()
    if s == '4':
        p.NewPerson()
    if s == '5':
        p.Delete()
    if s== '6':
        print('Ура! Вы упешно поставили Кате "5"')
    if s == '0':
        break