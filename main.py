"""
Expense Calculator App
"""
from typing import List


def get_amount_of_income() -> int:
    """
    Get the amount of income from the input user

    :return: The amount of income as an integer
    """
    total_income = int(input("Enter your total income:\n>>> "))
    assert total_income > 0, "Income must be greater than 0"  # Validate input

    print("Your total income is: ", total_income)

    return total_income


if __name__ == '__main__':
    print("-" * 30)
    print("\t\tExpense Calculator App")
    print("-" * 30)
    get_amount_of_income()
