from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """
    Creates a caching Fibonacci function.

    :return: A function to compute Fibonacci numbers utilizing caching
    """
    cache = {}

    def fibonacci(n):
        """
        Calculate the n-th Fibonacci number using memoization to achieve optimized
        performance. This function recursively computes the Fibonacci sequence while
        storing previously computed results in a cache to avoid redundant calculations.

        :param n: The position in the Fibonacci sequence (starting from 0) for which
                  the value needs to be computed.
        :return: The Fibonacci number corresponding to the given position `n`.
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


fib = caching_fibonacci()
print(f"{fib(10)=}")  # -> 55
print(f"{fib(15)=}")  # -> 610
