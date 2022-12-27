import collections
from sys import stdin

width, height = map(int, stdin.readline().split())

var = "Hello world!"
a = collections.Counter(var)
arr = [(lambda: 0, lambda: 1)[letter == "o"]() for letter in var]
print(arr)
print(a)
