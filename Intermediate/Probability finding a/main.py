import itertools


def find_probability():
    n = int(input())
    ls = input().split()
    k = int(input())
    com = list(itertools.combinations(ls, k))
    tol = [i for i in com  if "a" in i ]
    print(com,tol)
    print(round((len(tol)/len(com)),3))


find_probability()