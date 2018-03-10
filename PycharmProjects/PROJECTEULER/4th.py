"""    PROJECT EULER
FOURTH PROBLEM
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""


def is_palindrome(n):               # To check if the passed argument is a palindrome or not

    temp = n
    r = 0

    while n > 0:
        r = r + (n % 10)
        if r == temp:
            return True             # to return true if the number is true and vice versa
        r = r * 10
        n = n // 10
    return False


def main():
    lis = []                               # list lis to store the palindrome number formed by product of two numbers
    for i in range(100, 1000):
        for j in range(100, 1000):
            if i * j > 9:
                flag = is_palindrome(i * j)
                if flag is True:

                    lis.append(i * j)
    print(max(lis))                        # to print the largest palindrome made from the product of two 3-digit number


if __name__ == '__main__':
    main()
