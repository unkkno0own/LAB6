def display_sorted_char_set(char_set):
    """
    Функція сортує множину символів в алфавітному порядку.
    Множина перетворюється на список для сортування, оскільки множини не підтримують порядок.

    Parameters:
        char_set (set): множина символів
    """
    print("Початкова множина символів:", char_set)

    # Перетворення множини на список для сортування
    sorted_list = sorted(char_set, key=lambda x: x.lower())  # Сортування без урахування регістра

    # Друк відсортованих елементів
    print("Відсортовані елементи множини:", sorted_list)

# Задана множина символів
char_set = {'Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm',
            'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz'}

# Виклик функції
display_sorted_char_set(char_set)
