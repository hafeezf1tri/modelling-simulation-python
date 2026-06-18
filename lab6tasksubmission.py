def high_temperature_alerts(temperatures, limit):
    for temp in temperatures:
        if temp > limit:
            yield temp


def running_total(numbers):
    total = 0
    for num in numbers:
        total = total + num
        yield total


print("Task 1: CPU Temperature Alert Generator")
readings = [42, 50, 55, 60, 70, 78, 80]
for temp in high_temperature_alerts(readings, 75):
    print("Alert:", temp, "°C")

print()

print("Task 2: Running Total Generator")
marks = [10, 15, 20, 5]
for total in running_total(marks):
    print(total)

print()


