class Arithmetic:
    def __init__(self, value1, value2):
        self.v1 = value1
        self.v2 = value2

    def addition(self):
        ans = self.v1 + self.v2
        return ans

    def subtraction(self):
        result = self.v1 - self.v2
        return result

    def multiplication(self):
        ans = self.v1 * self.v2
        return ans

    def division(self):
        ans = self.v1 / self.v2
        return ans


def main():
    print("Enter first number: ")
    no1 = int(input())

    print("Enter second number: ")
    no2 = int(input())

    obj = Arithmetic(no1, no2)

    abt = obj.addition()
    print("Addition is: ", abt)

    bbt = obj.subtraction()
    print("Subtraction is: ", bbt)

    cbt = obj.multiplication()
    print("Multiplication is: ", cbt)

    dbt = obj.division()
    print("Division is: ", dbt)


if __name__ == "__main__":
    main()
