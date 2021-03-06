"""
    Here we will see implementation of some well known algorithmic problem's solution
    in a single line using Lambda functions.
    Lamnda function has great powers if used corretly and we will witness it as
    we go through different problems. These are well known problems or will be understandable
    just by the names, so will not be going throug the explanation of the problem
    but our focus will be on the use of lambda function.
"""

# Finding Anagrams
# return True if give strings are anagrams else retur False

is_anagram = lambda x1, x2: sorted(x1) == sorted(x2)

# Now check for the result.
print("Output of is_anagram function: ")
print(is_anagram("elvis", "lives"))
print(is_anagram("elvis", "data"))


print("\n")

# Finding Palindromes
# return True if given string is a palindrome or not.

is_palindrome = lambda x: x == x[::-1]

# Now check for the result
print("Output of is_palindrome function: ")
print(is_palindrome("anna"))
print(is_palindrome("rats live on no evil star"))

print("\n")
# Finding factorials
# return factorial of a given number

factorial = lambda n: n*factorial(n-1) if n > 1 else 1

#Now check the result
print("Output of factorial: ")
print(factorial(5))
print(factorial(7))

print("\n")

# Finding Levenshtein Distance
# return the no of editing steps required to reach from sring a to string b

## Test cases
a = "cat"
b = "chello"
c = "chess"

ls = lambda a, b: len(b) if not a else len(a) if not b else min(ls(a[1:], b[1:])+(a[0]!=b[0]), ls(a[1:], b)+1, ls(a, b[1:])+1)

# Now check the result
print("Output of levenshtein distance: ")
print(ls(a,b))
print(ls(b,c))
print(ls(a,c))

print("\n")

# Calculating the powerset

# we will be using reduce function
from functools import reduce
# Original Set
s = [1,2,3]

ps = lambda s: reduce(lambda P, x: P+[subset | {x} for subset in P], s,[set()])

# Now check the result
print("Output of powerset: ")
print(ps(s))

print("\n")

# Caesar's cipher encryption
# ROT13 algorithm

# Original string
abc = "abcdefghijklmnopqrstuvwxyz"
s = "xthexrussiansxarexcoming"

rt13 = lambda x: "".join([abc[(abc.find(c)+13)%26] for c in x])

# Now check the result
print("Output of the caesar's cipher: ")
print(rt13(s))
print(rt13(rt13(s)))

print("\n")

# Finding prime numbers
# find all prime numbers <= m
n = 20

primes = reduce(lambda r,x: r-set(range(x**2, n, x)) if x in r else r, range(2, int(n**0.5)+1), set(range(2,n)))

print("Output of the prime numbers: ")
print(primes)

print("\n")


# Calculating fibonacci series
# we will be using reduce()

n = 10
fibs = reduce(lambda x, _: x+[x[-2]+x[-1]], [0]*(n-2), [0,1])

# now chwck the result
print("Result of fibonacci series: ")
print(fibs)

print("\n")


# Recursive binary search
# rerturn index where element is found else return -1
l = [ 3, 6, 14, 16, 33, 55, 56, 89]
x = 33
# search for x in l

bs = lambda l, x, lo, hi: -1 if lo>hi else\
    (lo+hi)//2 if l[(lo+hi)//2]==x else\
        bs(l,x, lo, (lo+hi)//2-1) if l[(lo+hi)//2]>x else\
            bs(l, x, (lo+hi)//2+1, hi)

# Now check the result
print("Output of the recursive binary search: ")
print(bs(l, x, 0, len(l)-1))

print("\n")


# Recusrive quicksort algortihm
# return sorted list
unsorted = [33, 2, 3, 45, 6, 54, 33]

q = lambda l: q([x for x in l[1:] if x<= l[0]])+ [l[0]] + q([x for x in l if x > l[0]]) if l else []

# Now check the result
print("Output of the recusrive quicksort algorithm: ")
print(q(unsorted))