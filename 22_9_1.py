sequence = input("1)Введите целые положительные числа через пробел: ")
a_number = input("2)Введите любое число: ")

def is_int(str):
    """Функция определения цифр в строке."""
    str = str.replace(" ", "")
    try:
        int(str)
        return True
    except ValueError:
        return False

import sys
if " " not in sequence: #Проверка на наличие пробелов в вводе.
    print("\nВвод осуществлен без пробелов. Пожалуйста перечитайте условие и повторите попытку.")
    sys.exit(0)

if a_number.isdigit(): #Проверка любого числа на недопустимые символы.
    any_number = int(a_number)
else:
    print("\nВо втором условии Вы ввели недопустимый символ. Пожалуйста перечитайте условие и повторите попытку.")
    sys.exit(0)

if not is_int(sequence): #Проверка на ввод недопустимых символов.
    print("\nВ первом условии Вы ввели недопустимый символ. Пожалуйста перечитайте условие и повторите попытку.")
    sys.exit(0)
else:
    sequence = sequence.split()

list_sequence = [int(item) for item in sequence]

def merge_sort(sequence):
    """Функция сортировки слиянием (разделение массива)"""
    if len(sequence) < 2:
        return sequence[:]
    else:
        middle = len(sequence) // 2
        left = merge_sort(sequence[:middle])
        right = merge_sort(sequence[middle:])
        return merge(left, right)

def merge(left, right):
    """Функция сортировки слиянием (сортировка разделённого массива)"""
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_sequence = merge_sort(list_sequence)
print(f"Отсортированный список: {list_sequence}")

def binary_search(array, element, left, right):
    """Функция двоичного поиска"""
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return "Число выходит за диапозон списка, введите меньшее число."

#Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
#а следующий за ним больше или равен этому числу.
if not binary_search(list_sequence, any_number, 0, len(list_sequence)):
    element = min(list_sequence, key = lambda x: (abs(x - any_number), x))
    ind = list_sequence.index(element)
    max_ind = ind + 1
    min_ind = ind - 1
    if element < any_number:
        print("\n\tВ списке нет введённого элемента.")
        print(f"Ближайший меньший элемент: {element}, с индексом: {ind}")
        print(f"Ближайший больший элемент: {list_sequence[max_ind]}, с индексом: {max_ind}")
    elif min_ind < 0:
        print("\n\tВ списке нет введённого элемента.")
        print(f"Ближайший больший элемент: {element}, с индексом: {list_sequence.index(element)}")
        print("В списке нет меньшего элемента.")
    elif element > any_number:
        print("\n\tВ списке нет введённого элемента.")
        print(f"Ближайший больший элемент: {element}, с индексом: {list_sequence.index(element)}")
        print(f"Ближайший меньший элемент: {list_sequence[min_ind]}, с индексом: {min_ind}")
    elif list_sequence.index(element) ==0:
        print(f"Индекс введённого элемента: {list_sequence.index(element)}")
    else:
        print(f"Индекс введённого элемента: {binary_search(list_sequence, any_number, 0, len(list_sequence))}")
