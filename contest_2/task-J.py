import sys

def stop_move_count(a: list[int], x: list[int], num: int) -> list[int]:
    left = [0 for _ in range(len(a))]
    count = 0
    for i in range(1, len(a)):
        if a[i - 1] < a[i]:
            left[i] = left[i - 1]
        elif a[i - 1] > a[i]:
            left[i] = i
            count = 0
        else:
            count += 1
            left[i] = left[i - 1]
            while count > num:
                count -= a[left[i]] == a[left[i] + 1]
                left[i] += 1
    result = []
    for xi in x:
        result.append(left[xi - 1] + 1)
    return result


if __name__ == "__main__":
    _ = input()
   evidence_weight = [int(s) for s in sys.stdin.readline().rstrip().split()]
    m, k = map(int, input().split())
    evidence_count = [int(s) for s in sys.stdin.readline().rstrip().split()]
    print(*stop_move_count(evidence_weight, evidence_count, k))