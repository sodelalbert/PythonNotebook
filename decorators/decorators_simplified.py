"""

Decorators

Decorator objects adds behaviour to component. They can also add behaviour to other decorators as well.

References:
    - https://youtu.be/QH5fw9kxDQA
"""
import logging
from math import sqrt
from time import perf_counter
from typing import Callable, Any


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for element in range(2, int(sqrt(number)) + 1):
        if number % element == 0:
            return False
        return True


def count_prime_numbers(upper_bound: int) -> int:
    count = 0
    for number in range(upper_bound):
        if is_prime(number):
            count += 1
    return count


"""
In this case we have count_prime_numbers function and specially designed benchmark function which is calling 
count_prime_numbers to benchmark it. 

Note that in main we are calling benchmark function which is executing wraparounds + count_prime_numbers.
"""


def benchmark(upper_bound: int) -> int:
    start_time = perf_counter()
    value = count_prime_numbers(upper_bound)
    end_time = perf_counter()
    run_time = end_time - start_time
    logging.info(f"Execution of count_prime_numbers took {run_time:.2f}")
    return value


"""
benchmark_wrapper accepts any callable (function),

Callable[..., Any]
... - means that that function which we are passing will be accepted with any argument
Any - is return value of passed function which can be anything   

wrapper function defined internally takes  
"""


def benchmark_wrapper(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()

        value = func(*args, **kwargs)

        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(f"Execution of {func.__name__} took {run_time:.2f}")
        return value
    # 16:06
    return wrapper


@benchmark_wrapper
def print_text(text: str) -> None:
    print(text)


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    # Specific function wraparound
    value = benchmark(100000)
    logging.info(f"number of primes: {value}")

    # Wrapper method accepting any function
    wrapper_fn = benchmark_wrapper(count_prime_numbers)
    wrapper_value = wrapper_fn(100000)
    logging.info(f"number of primes: {wrapper_value}")

    print_text("asa akira")


if __name__ == "__main__":
    main()
