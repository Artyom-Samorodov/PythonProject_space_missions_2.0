from missions import show_all_missions, search_missions


missions_list = [
    { "name": "Mars 2020","year": 2020,"direction": "Марс",},
    {"name": "Artemis I", "year": 2022, "direction": "Луна", },
    {"name": "Voyager 1", "year": 1977, "direction": "Дальний космос", },
    {"name": "Chandrayaan-3", "year": 2023, "direction": "Луна", }
]

while True:
    print('\n___МЕНЮ___')
    print('1. Показать все миссии')
    print('2. Поиск миссий по направлению')
    print('3. Выход')


    choice = input("Выберете действие (1-3):")


    if choice == "1":
        show_all_missions(missions_list)
    elif choice == "2":
        target = input("Введите направление для поиска (например, Луна): ")
        search_missions(missions_list , target)
    elif choice == "3":
        print("Программа замечена. До встречи в космосе!")
        break
    else:
        print("Неверный ввод. Пожалуйста, выбирете пункт от 1 до 3.")
