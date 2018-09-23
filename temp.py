def func(a, b):
    def pc(x, total=a + b):
        print x
        return x + total

    return "Sums are:", pc(a), pc(b)

print "Hello World!\n", func(1, 2)