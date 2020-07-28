number_list = [1, 1, 50, 24, 2, 44, 12, 50, 73, 98]
new_number_list = []
def removeDuplicates(list):
    for element in list: 
        if element not in new_number_list:
            new_number_list.append(element)
    print(new_number_list)

removeDuplicates(number_list)