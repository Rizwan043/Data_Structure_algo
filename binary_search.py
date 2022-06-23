def binary_search(number_list, find_number, left_index, right_index):
    if left_index > right_index:
        return -1

    mid_index = (left_index + right_index) // 2

    if right_index > len(number_list) or left_index < 0:
        return -1
    mid_number = number_list[mid_index]

    if mid_number == find_number:
        return mid_index

    if mid_number < find_number:
        left_index = mid_index + 1
    else:
        right_index = mid_index -1

    return binary_search(number_list, find_number, left_index, right_index)

if __name__ == '__main__':
    number_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    find_number = 15
    index = binary_search(number_list, find_number, 0, len(number_list))
    print(index-1)

