def fibo_recursion(n):
    if n == 0 or n == 1:
        return 1
    return fibo_recursion(n - 2) + fibo_recursion(n - 1)


if __name__ == '__main__':
    n = int(input())
    print(fibo_recursion(n))