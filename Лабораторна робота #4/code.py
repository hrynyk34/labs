import os

while True:
    file_path = input("Введіть шлях до файлу: ")

    if not os.path.isfile(file_path):
        print(f"Файл {file_path} не знайдено!")
        continue

    num_lines = 0
    num_empty_lines = 0
    num_z_lines = 0
    num_z_chars = 0
    num_and_lines = 0

    with open(file_path, "r") as file:
        for line in file:
            num_lines += 1

            if line.strip() == "":
                num_empty_lines += 1

            if "z" in line:
                num_z_lines += 1

            num_z_chars += line.count("z")

            if "and" in line:
                num_and_lines += 1

    print(f"Кількість рядків: {num_lines}")
    print(f"Кількість порожніх рядків: {num_empty_lines}")
    print(f"Кількість рядків з літерою 'z': {num_z_lines}")
    print(f"Кількість літер 'z' у файлі: {num_z_chars}")
    print(f"Кількість рядків з групою символів 'and': {num_and_lines}")

    another_file = input("Чи потрібно проаналізувати ще один документ? (Yes/no): ")
    if another_file.lower() == "no":
        break
