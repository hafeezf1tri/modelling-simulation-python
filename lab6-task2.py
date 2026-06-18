def countdown(n):
    while n > 0:
        yield n
        n -= 1
    yield "done!"


for value in countdown(5):
    print(value)
