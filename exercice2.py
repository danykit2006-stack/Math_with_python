numbers = range(10)
previous = 0
for number in numbers:
    n = number
    sum = n + previous
    print(f"current number: {n}, previous number: {previous}, sum: {sum}")
    previous = n

corde = "pynative"
for index in range(len(corde)):
    print(corde[index])

def remove_chars(chars, numbers):
    for number in range(numbers):
        chars = chars[1:]
    return chars

print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))