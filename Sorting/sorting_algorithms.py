import random
from turtle import left

def bubble_sort(num_list):
    for i in range(len(num_list)-1):
        swap = False
        for j in range(len(num_list)-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                swap = True

        if swap == False:
            break

    return num_list

def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        for j in range(i):
            if num_list[j] > num_list[i]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
            else:
                break
    return num_list


def selection_sort(num_list):
    for i in range(len(num_list) - 1):
        min_idx = i
        for j in range(i, len(num_list)):
            if num_list[j] < num_list[min_idx]:
                min_idx = j
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]
    return num_list


def merge_sort(num_list):
    i, j, k = 0, 0, 0
    if len(num_list) == 1:
        return num_list


    mid = len(num_list) // 2
    left_list = num_list[:mid]
    right_list = num_list[mid:]
    merge_sort(left_list)
    merge_sort(right_list)

    while (i < len(left_list) and j < len(right_list)):
        if (left_list[i] <= right_list[j]):
            num_list[k] = left_list[i]
            i += 1
        else:
            num_list[k] = right_list[j]
            j += 1
        k += 1

    while (i < len(left_list)):
        num_list[k] = left_list[i]
        i += 1
        k += 1

    while (j < len(right_list)):
        num_list[k] = right_list[j]
        j += 1
        k += 1

    return(num_list)


def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot < item]

    return quick_sort(left) + [pivot] + quick_sort(right)


data_list = random.sample(range(100), 10)
print(quick_sort(data_list))