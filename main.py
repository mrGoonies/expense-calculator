"""
Expense Calculator App
"""
from typing import List


list_of_incomes: List[int] = list()
list_of_expenses: List[int] = list()


def amount_of_expense(expense: int) -> List[int]:
    for amount in range(expense):
        expense = int(input("Enter expense amount:\n>>> "))
        assert expense > 0, "Expense must be greater than 0"

        list_of_expenses.append(expense)
    return list_of_expenses


def get_amount_expense() -> int:
    """
    Get the amount of expense from the input user

    :return: The amount of expense as an integer
    """
    total_expense = int(input("Enter your total expense:\n>>> "))
    assert total_expense > 0, "Expense must be greater than 0"  # Validate input

    return total_expense


def enter_income_amounts(amount_of_income: int  ) -> List[int]:
    """
    Enter the amount of income from the user
    :param amount_of_income: The amount of income as an integer
    :return: A list of income amounts
    """

    for amount in range(amount_of_income):
        income = int(input("Enter income amount:\n>>> "))
        assert income > 0, "Income must be greater than 0"

        list_of_incomes.append(income)
    return list_of_incomes


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

    income_amount = get_amount_of_income()
    income_list: List[int] = enter_income_amounts(income_amount)
    income_expense = amount_of_expense(get_amount_expense())
    total_income = sum(income_list)

    print("Your total income is: ", total_income)
    print("Your total expense is: ", sum(income_expense))