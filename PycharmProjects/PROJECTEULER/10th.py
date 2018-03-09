"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def is_prime(n):                     # to find if the number is prime or not
    k = 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            k = k + 1
    if k <= 0:
        return True                  # to return true if it is a prime
    else:
        return False


def main():
    summ = 0
    m = 2000000
    for i in range(2, m):
        x = is_prime(i)
        if x is True:
            summ += i
    print(summ)


if __name__ == '__main__':
    main()
