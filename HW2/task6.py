list_product = []

while True:
    temp_dict = {}
    user_input = input("Для выхода наберите 'exit', 'add' для добавления товара и 'a' для аналитики ")
    if user_input == "exit":
        break

    elif user_input == "a":
        dict_analytics = {"Название": [], "Цена": [], "Количество": [], "Ед.": []}
        for i in list_product:
            dict_analytics['Название'].append(i[1]['Название'])
            dict_analytics['Цена'].append(i[1]['Цена'])
            dict_analytics['Количество'].append(i[1]['Количество'])
            dict_analytics['Ед.'].append(i[1]['Ед.'])
        print(dict_analytics)

    elif user_input == "add":
        temp_dict["Название"] = input("Введите название товара ")
        temp_dict["Цена"] = int(input("Введите цену товара "))
        temp_dict["Количество"] = int(input("Введите количество товара "))
        temp_dict["Ед."]  = input("Введите единицу измерения ")
        list_product.append((len(list_product) + 1, temp_dict))



