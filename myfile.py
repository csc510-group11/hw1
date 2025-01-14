def pow(x,n):
    if x == 0:
        return 0

    if n == 0:
        return 1

    if n == 1:
        return x

    inverted = False

    if n < 0:
        inverted = True
        n = n * -1

    result = 1

    while n > 1:
        if n % 2 != 0:
            result = result * x
            n = n - 1
        else:
            x = x * x
            n = n // 2
        
    result = result * x

    return result if not inverted else 1/result

print(pow(11, 13))
