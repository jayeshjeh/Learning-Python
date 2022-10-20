
# def sum(n):
#     sum = 0
#     for no in str(n):
#         sum += int(no)
#     return sum


def sum1(n):
    a = 0
    while n != 0:
        a += (n % 10)
        n //= 10
    return a


num = int(input())
print(sum1(num))
