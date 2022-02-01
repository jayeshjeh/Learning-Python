empty = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbs = even + odd
print(numbs)

even.extend(odd)
print(even)

another_even = even
print(another_even)

even.sort(reverse=True)
print(even)

print(another_even)


page = "The quick brown fox jumps over the lazy dog"

letters = sorted(page)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_num = sorted(numbers)
print(sorted_num)

numbers.sort()
print(numbers)

missing_letters = sorted("The quick brown fox jumps over the lazy dog", key=str.casefold)
print(missing_letters)
names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"]

names.sort(key=str.casefold)
print(names)
