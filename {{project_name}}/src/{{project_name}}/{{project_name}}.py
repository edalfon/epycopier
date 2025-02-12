"""Short description of the module.

Longer description that can span several lines and can
even include examples.

Examples:
    >>> from {{ project_name }} import {{ project_name }}
    >>> {{ project_name }}.hello()
"""

from typing import Union


def hello():
    """Says Hello World.

    It does not have any arguments.

    Returns:
        a string saying Hello World

    """
    return "Hello World"


def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Calculates the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a: first number
        b: second number

    Returns:
        sum of the first and the second number
    """

    return float(a + b)
