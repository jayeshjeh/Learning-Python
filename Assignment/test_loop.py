data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

top_i = len(data) - 1
for i, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_i - i, value)
        del data[top_i - i]

print(data)
