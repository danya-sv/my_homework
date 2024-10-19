def binary_search(element, sorted_list):
    first = 0
    last = len(sorted_list) - 1
    result_ok = False
    pos = -1

    while first <= last:
        middle = (first + last) // 2
        if element == sorted_list[middle]:
            result_ok = True
            pos = middle
            break
        elif element > sorted_list[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        print("Элемент найден. Индекс :", pos)
    else:
        print("Элемент не найден")

my_list = [2, 4, 6, 8, 10, 12]
search_element = 6
binary_search(search_element, my_list)
