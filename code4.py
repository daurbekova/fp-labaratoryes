import random
def ar(n):
    return sorted(random.randint(0, 100) for _ in range(n))
def b(a, target):
    def f(l, h):
        if l > h:
            return -1
        m = (l + h) // 2
        if a[m] == target:
            return m
        elif a[m] < target:
            return f(m + 1, h)
        else:
            return f(l, m - 1)
    return f(0, len(a) - 1)
a = ar(30)
print(a)
t = b(a, 8)
print(t)
