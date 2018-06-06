# PROBLEM 48
'''The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.'''

import time
start = time.time()


def main():
    sum = 0

    for num in range(1, 1001):
        sum = sum + num ** num
    result = str(sum)
    print("The last ten digits of the series is {}.".format(result[-10:]))
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
