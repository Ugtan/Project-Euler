"""PROJECT EULER
   FIRST PROBLEM
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multipl
es is 23.

Find the sum of all the multiples of 3 or 5 below 1000"""


def sum_multiple():               # A Function sum multiple to check if the multiples of 3 or 5 from from 1 to 1000 and
    summ = 0                               # find sum of multiple
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:   # To check for multiples of three and five
            summ = summ + i
    return summ


def main():
    print(sum_multiple())           # To print the sum of all the multiples of 3 or 5 from 1 to 1000


if __name__ == '__main__':
    main()
