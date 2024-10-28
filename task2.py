def find_element_in_list(lst, target):
    """
    Функція здійснює пошук числового елемента за значенням у списку.
    Якщо елемент знайдено, виводить його індекс, інакше - повідомлення про відсутність елемента.
    
    Parameters:
        lst (list): список чисел
        target (int or float): значення для пошуку
    
    Returns:
        int: індекс елемента або -1, якщо елемента не знайдено
    """

    print("Поточний список:", lst)

    if target in lst:
        index = lst.index(target)
        print(f"Елемент {target} знайдено на індексі {index}.")
        return index
    else:
        print(f"Елемент {target} не знайдено у списку.")
        return -1
my_list = [3, 7, 10, 15, 20, 25]
search_value = 10
find_element_in_list(my_list, search_value)
