def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result


def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_list + '\n')


def resave_data_f(name, data_list):  # просто затер и поверх написал
    with open(name, 'w', encoding='utf8') as datafile:
        for row in data_list:
            for element in row:
                if (row.index(element) == len(row)-1):
                    datafile.write(element)
                else:
                    datafile.write(element+',')
            datafile.write('\n')


def print_bus():
    return read_data_from_file('bus.txt')


def add_bus():  # возможно я неправильно понимаю концепцию организации данных в БД. на мой взгляд уникальный идентификатор это что то служебное
 # и недоступное для редакции пользователю, который так и наровит неправильно что то записать. а потом идетификатор станет не уникальный, что то начнет работать не так и т.д.
 # пример организовал ттолько тут как демострацию
    stack = set()
    insert_data = input("Введите поле гос номер автобуса ")
    old_data = read_data_from_file('bus.txt')
    for row in old_data:
        # ну не самый элегантный вариант резать по символу
        id_num = int((row[0].split('s'))[1])
        stack.add(id_num)
    i = 1
    while (True):
        if i in stack:
            i += 1
        else:
            break
    # готовая строка с точно уникальным Id
    result_str = ('bus'+str(i)+','+str(insert_data))
    save_data_to_file('bus.txt', result_str)


def print_driver():
    return read_data_from_file('driver.txt')


def add_driver():
    save_data_to_file('driver.txt', input("Введите водителя: "))


def print_route(find_number):
    result_data = []
    tmp_data = find_for_number_route(find_number)
    srach_index = tmp_data[0]
    route_data = tmp_data[1]
    if (srach_index == None):
        print("Маршрут не найден")
        result_data.append(["нет информации"])
        result_data.append(["нет информации"])
    else:
        id_bus = (route_data[srach_index][2]).split()
        id_driver = (route_data[srach_index][3]).split()
        driver_data = print_driver()
        for row in driver_data:
            if (row[0] == id_driver[0]):
                print("Catch!")
                result_data.append(row)
        bus_data = print_bus()
        for row in bus_data:
            if (row[0] == id_bus[0]):
                result_data.append(row)

    return result_data


def add_route():
    save_data_to_file('route.txt', input("Введите маршрут: "))


def wait_answer():
    input("нажмите ввод для продолжения ")


def del_route(find_number):
    tmp_data = find_for_number_route(find_number)
    try:
        tmp_data[1].pop(tmp_data[0])
        resave_data_f('route.txt', tmp_data[1])
    except:
        print("нет такого маршрута")

# вроде как у пользователя врд ли есть информация о ID, поэтому ищи по номеру


def find_for_number_route(find_number):
    srach_index = None
    route_data = read_data_from_file('route.txt')
    for row in route_data:
        if (int(row[1]) == find_number):
            srach_index = route_data.index(row)
    return srach_index, route_data
