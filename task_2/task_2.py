import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float]:
    """
    Extracts and generates floating-point numbers or integers from a given text
    string. The function utilizes regular expressions to identify numbers that
    are surrounded by whitespace in the input text, converts them to floating-point
    values, and yields them one by one.

    :param text: The input text containing numbers to be extracted.
        Important: the numbers are expected to be surrounded by whitespace.
    :return: A generator yielding floating-point representations of the numbers found in the input text.
    """
    # Find all numbers in the text
    numbers = re.findall(r'(?<=\s)\d+(?:\.\d+)?(?=\s)', text)
    for num in numbers:
        # yield each number as a float
        yield float(num)


def sum_profit(text: str, func: Callable) -> float:
    """
    Calculates the total profit by applying a given function to the input text and summing up the resulting values.

    :param text: The input text containing data to process.
    :param func: A callable function that processes the input text and returns an iterable of numerical values.
    :return: The total sum of the numerical values obtained by applying the function to the input text.
    """
    return sum(func(text))


text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими "
        "надходженнями 27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
