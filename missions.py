def show_all_missions(missions):
    for index, mission in enumerate(missions, start=1):
        print(f"{index}. {mission['name']}")
        print(f" Год запуска: {mission['year']}")
        print(f" Направление: {mission['direction']}\n")


def search_missions(missions, target_direction):
    found = False
    for mission in missions:
        if mission['direction'].lower() == target_direction.lower():
            print(f"- {mission['name']} ({mission['year']} год)")
            found = True
    if not  found:
        print(f"Миссии по направлению {target_direction} не найдены")
