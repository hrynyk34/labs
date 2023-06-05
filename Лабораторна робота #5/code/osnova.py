from NUM_PROJ.greetings import greet_user # імпорт функції зі створеної раніше директорії
from NUM_PROJ.convert import convert_number_to_words # імпорт функції зі створеної раніше директорії

def main(): # створення нашої функції
    greet_user() # Викликаємо дану наму функцію
    number = int(input("Ведіть число: ")) # запитуємо в користувача число за допомогою команди "input"
    words = convert_number_to_words(number) # застусовуємо директорію для перетворення числа
    print(words)

if __name__ == "__main__": # звіряємо чи основний модуль пов'язаний з головною бібліотекою
    main()
