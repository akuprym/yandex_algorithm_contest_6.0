import sys

def append_prefix(arr: list[int], reverse=False) -> list[int]:
    prefix = [0 for _ in range(len(arr))]
    if reverse:
        arr.reverse()
    curr = 0
    for i in range(1, len(arr)):
        curr += arr[i - 1]
        prefix[i] = prefix[i - 1] + curr
    if reverse:
        prefix.reverse()
    return prefix


def move_to_openspace(rooms: list[int]) -> int:
    left = append_prefix(rooms.copy())
    right = append_prefix(rooms.copy(), True)
    ans = float('inf')
    for i in range(len(rooms)):
        ans = min(ans, left[i] + right[i])
    return int(ans)


if __name__ == "__main__":
    _ = input()
    input_data = [int(s) for s in sys.stdin.readline().rstrip().split()]
    print(move_to_openspace(input_data))