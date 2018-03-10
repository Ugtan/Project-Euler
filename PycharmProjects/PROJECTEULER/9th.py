"""
PROBLEM 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
#let a=2*m*n , b=m**2-n**2 , c=m**2+n**2
n = 1
while True:
    for m in range(1,50):
        if 2 * m * ( m + n) == 1000 and m > n :   # for a+b+c=1000 2mn+m^2-n^2+m^2+n^2=1000 this implies 2m(m+n)=1000
            print(m,n)
            print(2*m*n , m**2-n**2 , m**2+n**2)  #HERE a=2*m*n , b=m**2-n**2 , c=m**2+n**2
            print('The product of abc is', 2 * m * n * (m ** 2 - n ** 2) * (m ** 2 + n ** 2))
            exit(0)
    else:
        n+=1
        continue

