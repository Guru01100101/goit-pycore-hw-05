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


if __name__ == '__main__':
    text = ("Загальний дохід працівника складається з декількох частин: "
            "1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і "
            "324.00 доларів.")
    gen = generator_numbers(text)
    for number in gen():
        print(number)