# Пункты задачи:
# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных
# двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).
calls = 0


def count_calls():  # функция подсчитывающая вызовы остальных функций
    global calls
    calls += 1
    return calls


def string_info(string):  # функция преобразования
    count_calls()
    length = len(string)  # длина строки
    uppercase = string.upper()  # преобразование строки в верхний регистр
    lowercase = string.lower()  # преобразование строки в нижний регистр
    return length, uppercase, lowercase


def is_contains(string, list_to_search):  # функция сравнения
    count_calls()
    for i in list_to_search:
        if string.lower() == i.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
