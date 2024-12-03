n = int(input())
arr = list(map(int, input().strip().split()))

seq = [0 for _ in range(n)]
seq[0] = arr[0]

for i in range(1, n):
    seq[i] = seq[i - 1] + arr[i]

summ = 0
for i in range(1, n - 1):
    summ = (summ + seq[i - 1] * arr[i] * (seq[n - 1] - seq[i])) % 1000000007

print(summ)