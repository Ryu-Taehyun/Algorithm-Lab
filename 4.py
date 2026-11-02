numbers = [5, 10, 15, 20, 25]

def recursive_sum(numbers, index=0):

    # 1. 종료 조건
    if index == len(numbers):
        return 0

    # 2. 현재 숫자 + 나머지 숫자들의 합
    return numbers[index] + recursive_sum(
        numbers, index + 1
    )

print(recursive_sum(numbers))