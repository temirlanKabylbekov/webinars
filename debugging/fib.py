def fib_iterative(n):
    # import pdb; pdb.set_trace()
    breakpoint()
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_recursive(n):
    if n == 1 or n == 0:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_sequence(n):
    result = [0, 1]
    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])
    return result


if __name__ == '__main__':
    print(fib_iterative(10))
    # print(fib_iterative(10) * fib_recursive(10))
