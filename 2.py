numbers = [3, 7, 11, 15, 19, 23, 27, 31, 35]

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(binary_search(numbers, 23))
print(binary_search(numbers, 3))
print(binary_search(numbers, 100))