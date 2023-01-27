# проверка количества взятых конфет

def candies_checking():
    input_data = input("How many candies (1-28) do you want to grab : ")
    if not input_data.isdigit():
        print('The value must be integer and between (1 and 28), please try again: ')
        return candies_checking()
    if 0 < int(input_data) <= 28:
        return int(input_data)
    elif int(input_data) <= 0 or int(input_data) > 28:
        print('The value must be between (1 and 28), please try again: ')
        return candies_checking()