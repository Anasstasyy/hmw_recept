import os


def my_cook_book():
    with open('cookbook.txt', encoding='utf-8') as file:
        cook_book = {}
        for i in file:
            ingredients = []
            recepie_name = i.strip()
            ingredients_count = file.readline()
            cook_book[recepie_name] = ingredients
            for p in range(int(ingredients_count)):
                recepie = file.readline().strip().split(' | ')
                product, quantity, weight = recepie
                ingredients.append({'ingredient_name': product, 'quantity': quantity, 'measure': weight})
            file.readline()
            
def get_shop_list_by_dishes(dishes, person_count:int):
    result ={}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = int(ingredient['quantity']) * int(person_count)

                if ingredient_name in result:
                    result[ingredient_name]['quantity'] += quantity
                else:
                    result[ingredient_name] = {'measure': measure, 'quantity': quantity}
    for ingredient, values in result.items():
        print(f"  '{ingredient}': {values},")
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'],2)





