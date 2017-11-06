def is_pythag_triple(a, b, c):
    return a ** 2 + b ** 2 == c ** 2
for a in range(1, 1000):
    for b in range(1, 1000 - a):
        for c in range(1, 1000 - b):
            if a + b + c == 1000:
                if is_pythag_triple(a, b, c):
                    print (a, b, c)
                    print("Product: {}".format(a * b * c))
                    exit (0)
