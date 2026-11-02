numbers = [3, 7, 11, 15, 19, 23, 27, 31, 35]

def binary_search(numbers, target, left, right):

    # 1. 탐색 범위가 없어졌다면?
    if left > right:
        return -1

    mid = (left + right) // 2

    # 2. 목표값을 발견했다면?
    if numbers[mid] == target:
        return mid

    # 3. 목표값이 중간값보다 크다면?
    elif numbers[mid] < target:
        return binary_search(
            numbers, target, mid + 1, right
        )

    # 4. 목표값이 중간값보다 작다면?
    else:
        return binary_search(numbers, target, left, mid - 1)


print(binary_search(numbers, 23, 0, len(numbers) - 1))