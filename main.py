from shapeManager import ShapeManager


def print_greeting() -> None:
    print("Добро пожаловать в векторный редактор!")
    print("Доступные команды:")
    print_help()


def print_help() -> None:
    print("- add point <x> <y>")
    print("- add line <start_x> <start_y> <end_x> <end_y>")
    print("- add circle <center_x> <center_y> <radius>")
    print("- add square <top_left_x> <top_left_y> <side_length>")
    print("- remove <index>")
    print("- list")
    print("- help")
    print("- exit")


def main() -> None:
    manager = ShapeManager()
    print_greeting()

    while True:
        command = input("> ").strip().lower().split()
        if not command:
            continue

        action = command[0]
        try:
            if action == "add":
                if len(command) < 3:
                    print("Неверный формат команды.")
                    continue
                else:
                    manager.handle_shape(command)
            elif action == "remove" and len(command) == 2:
                index = int(command[1])
                manager.remove_shape(index)
            elif action == "list":
                manager.list_shapes()
            elif action == "help":
                print_help()
            elif action == "exit":
                print("Выход из редактора. До свидания!")
                break
            else:
                print("Неизвестная команда. Введите 'help' для списка команд.")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
