import os
from pprint import pprint

cook_book = {}

with open('file_1.txt', 'r', encoding='utf-8') as file_obj:
    for line in file_obj:
        name_key = line.strip()
        quant = int(file_obj.readline().strip())
        new_list = []
        for elem in range(quant):
            inside_dict = {}
            ingredients = file_obj.readline().split('|')
            inside_dict['ingredient_name'] = ingredients[0].strip()
            inside_dict['quantity'] = int(ingredients[1].strip())
            inside_dict['measure'] = ingredients[2].strip()
            new_list.append(inside_dict)
        file_obj.readline()
        cook_book[name_key] = new_list

# pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    count_equal_dish = {i:dishes.count(i) for i in dishes}
    for dish, ingredients in cook_book.items():
        if dish in dishes:
            for elem in ingredients:
                new_dict = {}
                new_dict['measure'] = elem['measure']
                new_dict['quantity'] = int(elem['quantity'] * person_count * count_equal_dish[dish])

                if elem['ingredient_name'] in result.keys():
                    new_dict['quantity'] += new_dict['quantity']
                result[elem['ingredient_name']] = new_dict

    # return pprint(result)

# person = 2
# get_shop_list_by_dishes(['Фахитос', 'Омлет'], person)
# print()
# get_shop_list_by_dishes(['Омлет', 'Омлет', 'Омлет'], person)

result_dict = {}

for filename in os.listdir('home_work'):

    with open(os.path.join('home_work', filename), 'r', encoding='utf-8') as result_file:
        file_text = result_file.read()

    with open(os.path.join('home_work', filename), 'r', encoding='utf-8') as result_file:
        file_string_list = result_file.readlines()
        count_string = len(file_string_list)
        result_dict[filename] = [count_string, file_text]

with open('result.txt', 'a', encoding='utf-8') as file_help:
    sorted_values = sorted(result_dict.values())
    sorted_result_dict = {}
    for count_and_string in sorted_values:
        for files in result_dict.keys():
            if result_dict[files] == count_and_string:
                sorted_result_dict[files] = result_dict[files]
                break
        file_help.write(f'\nИмя файла: {files}\nКоличество строк в файле: {count_and_string[0]}\n{count_and_string[1]}\n')



