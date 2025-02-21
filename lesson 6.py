def check_input():
    try:
        user_input = input("Введите строку: ")
        if not user_input.isalpha():
            raise ValueError("Ошибка: строка должна содержать только буквы!")
        print("Строка введена правильно.")
    except ValueError as e:
        print(e)

check_input()