"""   PROJECT EULER
THIRD PROBLEM
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""


def is_prime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return True

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        return False


def main():

    n = 13195
    lis = []          # a lis to append all the prime factors in it

    for i in range(2, int(n / 2)):
        x = is_prime(i)
        if n % i == 0 and x is True:
            lis.append(i)
    print(max(lis))         # to print the maximum from all of the prime factors


if __name__ == '__main__':
    main()