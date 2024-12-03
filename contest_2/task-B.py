import sys

def find_car_count(cars: list[int], target: int) -> int:
    num = 0
    count = dict()
    count[0] = 1
    for i in range(1, len(cars)):
        cars[i] = cars[i - 1] + cars[i]
    for j in cars:
        if j - target in count:
            num += count[j - target]
        count[j] = count.get(j, 0) + 1
    return num

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = [int(num) for num in sys.stdin.readline().rstrip().split()]
    print(find_car_count(arr, k))