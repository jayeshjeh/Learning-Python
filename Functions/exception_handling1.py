def division(a, b):
    ans = 0.0
    try:
        ans = a / b

    except Exception:            # catch(exception eboj)
        print("Exception occurred")
    return ans


def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))

    ret = division(no1, no2)
    print("Division is: ", ret)


if __name__ == "__main__":
    main()
