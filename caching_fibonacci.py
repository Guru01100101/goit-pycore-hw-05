from collections import defaultdict


def caching_fibonacci(cache=None):
    """
    Returns a Fibonacci function with caching using closure
    :param cache: The cache to store the calculated Fibonacci numbers
    :return function: The Fibonacci function with caching
    """
    # If cache is not provided, create a defaultdict to store the calculated Fibonacci numbers
    if cache is None:
        cache = defaultdict(int)

    def fibonacci(n):
        if n in cache:
            return cache[n]

        # Base case
        if n <= 1:
            return n

        # Recursive call with adding to cache all calculated numbers
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == '__main__':
    fib = caching_fibonacci()
    print(fib(10))  # prints 55
    print(fib(15))  # prints 610
