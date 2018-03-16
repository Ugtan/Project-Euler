"""215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?"""


from math import pow


def power():     # to find 1000th power of 2
    return pow(2, 1000)


def main():
    sum = 0
    x = power()
    x = int(x)     # since 2^1000 will be very large so to remove the signtific notation of e
    while x != 0:
        sum += x % 10       # to add the sum of the digits of 2^1000
        x = x//10
    print(sum)


if __name__ == "__main__":
    main()
