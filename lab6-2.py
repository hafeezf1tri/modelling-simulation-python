def even_numbers(n):

    for number in range(1, n + 1):
        if number % 2 == 0:
            yield number


print("Testing with n=num:20")
for num in even_numbers(20):
    print(num)
