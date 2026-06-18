def high_temperature_alerts(temperatures, limit):
    for temp in temperatures:
        if temp > limit:
            yield temp


def running_total(numbers):
    total = 0
    for num in numbers:
        total = total + num
        yield total


print("Task 1: Temperature Alert Generator")
readings = [32, 35, 41, 38, 45, 29, 50]
for temp in high_temperature_alerts(readings, 40):
    print("Alert:", temp, "°C")

print()

print("Task 2: Running Total Generator")
marks = [10, 15, 20, 5]
for total in running_total(marks):
    print(total)

print()

print("Task 2: Second Test")
numbers = [3, 7, 2, 8]
for total in running_total(numbers):
    print(total)

print()

print("Explanation:")
print("yield pauses a function and gives one value at a time.")
print("When the generator is used again, it continues from where it stopped.")
print("This is useful because we can process values one by one without creating a full list.")
