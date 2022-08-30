class Processing:  # Объявление класса
    def __init__(self, input_data):  # Инициализация объекта класса
        self.input_data = input_data  # Создание динамической переменной для класса

    def count_sign(self):  # Создание метода класса для вычисления длины строки
        self.count_ = len(self.input_data)

    def general(self):  # Создание метода класса для требуемых вычислений
        count_a = ''  # Пустая строка для записи гласных
        count_b = ''  # Пустая строка для записи согласных
        count_honest = 1  # Счетчик для подсчета произведения четных сумм
        if self.input_data[0].isalpha():  # Проверка, являются ли переданные данные - буквами
            for i in self.input_data:  # Запись гласных букв
                if i in "aeiouy":
                    count_a += i
                else:  # Запись согласных букв
                    count_b += i
            if (len(count_a) * len(count_b)) <= self.count_:  # Сравнение проз.глас. и согл букв с дл.строки
                print("Гласные: ", count_a)  # Вывод результата
            else:
                print("Согласные: ", count_b)  # Вывод результата

        elif self.input_data[0].isdigit():  # Проверка, являются ли переданные данные - цифрами
            for i in self.input_data:
                if int(i) % 2 == 0:
                    count_honest *= int(i)  # Подсчет произведения четных чисел
            print("Произведение четных чисел на дл.числа: ", count_honest * self.count_)  # Вывод результата


user_data = input("Введите число или строку: ")  # Запись в переменную введенного значения
object = Processing(user_data)  # Создание объекта класса
object.count_sign()  # Вызов метода для объекта класса
object.general()  # Вызов метода для объекта класса
