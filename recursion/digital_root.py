def digital_root(n):
    if n == 0:
        return n
    sum_of_digits = 0
    while n > 0:
        sum_of_digits = sum_of_digits + (n % 10)
        n = n // 10
    if sum_of_digits < 10:
        return sum_of_digits
    else:
        return digital_root(sum_of_digits)


def main(n):
    x = digital_root(n)
    print(x)


if __name__ == '__main__':
    main(99999)
