from typing import Callable


def generator_numbers(text: str) -> Callable:
    """
    Returns a function that generates floating point numbers from the text
    :arg text: the text to generate the numbers from (separated by spaces)
    :return: generator function that generates the numbers
    """
    def generator():
        for number in text.split():
            try:
                number = number.replace(',', '.')
                yield float(number)
            except ValueError:
                pass

    return generator


def sum_profit(text: str, generator: Callable) -> float:
    """
    Returns the sum of the numbers generated from the text using the generator
    :arg text: the text to generate the numbers from (separated by spaces)
    :arg generator: the generator function to generate the numbers
    :return: the sum of the numbers
    """
    gen = generator(text)
    return sum(gen())


if __name__ == '__main__':
    text = ("Загальний дохід працівника складається з декількох частин: "
            "1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і "
            "324.00 доларів.")
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")  # Загальний дохід: 1351.46
