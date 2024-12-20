import sys

def delete_medians(data: list[int], size: int) -> str:
    data.sort()
    right = size // 2
    left = right - 1
    count = []
    while left >= 0:
        left_median = data[left]
        right_median = data[right]
        if size % 2 == 1:
            left_median, right_median = right_median, left_median
        count.append(f'{left_median} {right_median}')
        left -= 1
        right += 1
    if right < size:
        count.append(str(data[right]))
    return ' '.join(count)


if __name__ == "__main__":
    n = int(input())
    arr = [int(num) for num in sys.stdin.readline().rstrip().split()]
    print(delete_medians(arr, n))