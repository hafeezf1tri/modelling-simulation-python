def demo():
    yield "A"  
    yield "B"

g = demo()
print(next(g))  # Output: A
print(next(g))  # Output: B

