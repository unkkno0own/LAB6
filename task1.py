def insert_before_element(lst, new_element, before_element):
    if before_element in lst:
        index = lst.index(before_element)
        lst.insert(index, new_element)
    else:
        print(f"Елемента '{before_element}' немає в списку.")
    return lst

user_input = input("Введіть елементи списку через пробіл: ")
lst = user_input.split()
new_element = input("Введіть новий елемент для вставки: ")
before_element = input("Введіть елемент, перед яким потрібно вставити новий елемент: ")

result = insert_before_element(lst, new_element, before_element)
print("Кінцевий вигляд списку:", result)
