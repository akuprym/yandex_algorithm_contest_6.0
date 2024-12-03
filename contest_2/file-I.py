import sys

def find_learning_order(a: list[int], b: list[int], c: list[int]) -> list[int]:
    count = []
    algos = []
    for i in range(len(a)):
        algos.append((a[i], b[i], i + 1))
    sorted_a = list(sorted(algos, key=lambda x: (x[0], x[1], -x[2]), reverse=True))
    sorted_b = list(sorted(algos, key=lambda x: (x[1], x[0], -x[2]), reverse=True))
    used_id = set()
    pa, pb = 0, 0
    for j in c:
        if j == 0 and pa < len(a):
            if not sorted_a[pa][2] in used_id:
                count.append(sorted_a[pa][2])
                used_id.add(sorted_a[pa][2])
                pa += 1
            else:
                while pa < len(a):
                    if not sorted_a[pa][2] in used_id:
                        count.append(sorted_a[pa][2])
                        used_id.add(sorted_a[pa][2])
                        pa += 1
                        break
                    pa += 1
        elif j == 1 and pb < len(b):
            if not sorted_b[pb][2] in used_id:
                count.append(sorted_b[pb][2])
                used_id.add(sorted_b[pb][2])
                pb += 1
            else:
                while pb < len(b):
                    if not sorted_b[pb][2] in used_id:
                        count.append(sorted_b[pb][2])
                        used_id.add(sorted_b[pb][2])
                        pb += 1
                        break
                    pb += 1
    return count


if __name__ == "__main__":
    _ = input()
    interesting_algos = [int(s) for s in sys.stdin.readline().rstrip().split()]
    useful_algos = [int(s) for s in sys.stdin.readline().rstrip().split()]
    mood_indicators = [int(s) for s in sys.stdin.readline().rstrip().split()]
    print(*find_learning_order(interesting_algos, useful_algos, mood_indicators))