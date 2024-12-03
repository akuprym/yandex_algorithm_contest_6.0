import sys

def calc_min_days(days: list[int], k: int) -> int:
    days.sort()
    count = 1
    diff, similar = 0, 0
    while similar < len(days):
        if days[similar] <= days[diff] + k:
            similar += 1
        else:
            count = max(count, similar - diff)
            diff += 1
    return max(count, similar - diff)


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = [int(num) for num in sys.stdin.readline().rstrip().split()]
    print(calc_min_days(arr, k))