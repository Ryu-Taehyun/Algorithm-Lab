numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print(mid)
        break

    elif numbers[mid] < target:
        left = mid + 1

    else:
        right = mid - 1