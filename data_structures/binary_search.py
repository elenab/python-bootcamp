def binary_search(input_array, value):
    """
    
    :param input_array: Python list to search through
    :param value: value you're searching for
    :return: Return the index of value, or -1 if the value doesn't exist in the list.
    """
    left = 0
    right = len(input_array) - 1

    while left <= right:
        middle_index = (left + right) // 2
        middle_value = input_array[middle_index]
        if value == middle_value:
            return middle_index
            break
        else:
            if value < middle_value:
                right = middle_index - 1
            else:
                left = middle_index + 1
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
