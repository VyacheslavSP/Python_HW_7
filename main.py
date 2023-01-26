from menu import Menu
import function as fn

# if __name__ == "__main__":
#     # основной блок
menuitems = [
    ("1", "Вывод автобусов"),
    ("2", "Добавление автобуса"),
    ("3", "Вывод водителей"),
    ("4", "Добавление водителей"),
    ("5", "Вывод маршрута"),
    ("6", "Добавление маршрута"),
    ("7", "Удаление маршрута"),
    ("8", "Выход")]
text = None
menu = Menu(menuitems)
# menu.run('>:')
while (True):
    if (text != None):
        fn.wait_answer()
    for i in menuitems:
        print(i[0], i[1])
    while (True):
        try:
            # минимум проверки ввода
            text = int(input("Введите номер: "))
            if (not (1 <= text <= 8)):
                raise
            else:
                break
        except:
            print("неккорекный номер")
    match text:
        case 1:
            print(fn.print_bus())
        case 2:
            fn.add_bus()
        case 3:
            print(fn.print_driver())
        case 4:
            fn.add_driver()
        case 5:
            inform = fn.print_route(int(input("Введите номер маршрута :")))
            print("информация о водителе: ")
            print(inform[0])
            print("информация о автобусе: ")
            print(inform[1])
        case 6:
            fn.add_route()
        case 7:
            fn.del_route(int(input("Введите номер маршрута :")))
        case 8:
            break
