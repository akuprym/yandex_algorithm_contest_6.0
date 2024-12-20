import sys

def max_length(s: str, max_str: int) -> int:
    left, right = 0, 0
    ans = 0
    count_a, count_b = 0, 0
    curr_str = 0
    while right < len(s):
        if curr_str <= max_str:
            if s[right] == 'a': count_a += 1
            if s[right] == 'b':
                count_b += 1
                curr_str += count_a
        else:
            while curr_str > max_str:
                if s[left] == 'a':
                    count_a -= 1
                    curr_str -= count_b
                if s[left] == 'b': count_b -= 1
                left += 1
        if curr_str <= max_str:
            ans = max(ans, right - left + 1)
            right += 1
    return ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    text = sys.stdin.readline().rstrip()
    print(max_length(text, k))