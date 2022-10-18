def abs_fibo(n, k):
    f = [1, 1]
    d = (10**k)
    if n < 2:
        return 1
    else:
        for i in range(n-1):
            s = (f[0] + f[1]) % d
            f[0] = f[1]
            f[1] = s
        return f[1]


if __name__ == '__main__':
    n, k = (int(i) for i in input().split())
    print(abs_fibo(n, k))
