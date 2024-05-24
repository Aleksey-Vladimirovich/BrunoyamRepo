l = [1, 4, 1, 6, "hello", "a", 5, "hello"]

print(*set([i for i in l if l.count(i) > 1]))
