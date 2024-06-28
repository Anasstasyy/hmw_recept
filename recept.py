cook_book = {}
with open('cookbook.txt', 'rt', encoding = "utf-8") as file:
    for l in file:
        dish = l.strip()
        ingredient_list = []
        count = file.readline()
        for i in range(int(count)):
            dish = file.readline()
            ingredient_name, quantity, measure = dish.strip().split(' | ')
            ingredient_list.append({'ingredint_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            dep = {dish: ingredient_list}
        separstse = file.readline()
        cook_book.update(dep)
        
#print(f'cook_book = {cook_book}')
        
        
def get_shop_list_by_dishes(dishes, person_count):
    result ={}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['product'] in result:
                    result[consist['product']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['product']] = {'measure': consist['measure'], 'quantity': (consist['quantity'] * person_count)}
        else:
            print('ошибка')
    print(result)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)



    
    



