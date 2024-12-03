import sys

def find_possible_count(distances: list[int], max_distance: int):
    size = len(distances)
    right = 0
    count = 0
    for left in range(size):
        while right < size and distances[right] - distances[left] <= max_distance:
            right += 1
        count += size - right
    return count

if __name__ == "__main__":
    params = []
    for line in sys.stdin:
        params.append(line)
    max_distance = int(params[0].split()[1])
    distances = [int(dist) for dist in params[1].strip().split()]
    print(find_possible_count(distances, max_distance))