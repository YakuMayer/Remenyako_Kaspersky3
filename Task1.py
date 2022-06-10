n = int(input())
k = int(input())
def F(n, k):
    if n == 0 or n == 1 or n == 2:
        return 1
    return F(n - 1, k) + F(n - 2, k) * k
print(F(n, k))
