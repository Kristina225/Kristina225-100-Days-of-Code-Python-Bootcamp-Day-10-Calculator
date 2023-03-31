# HELPER FUNCTIONS FOR: printing, clearing screen...
import os


def clear_screen() -> None:
    """Clears the screen"""
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def print_game_logo(game_logo: str) -> None:
    """Takes in a str and prints it"""
    print(game_logo)


def print_operations(operations: dict) -> None:
    """Takes in a dictionary and prints its keys line by line"""
    for operation in operations:
        print(operation)


def print_calculation_result(x: float, y: float, operation: str, result: float):
    """Takes in operators and operands and prints the calculation"""
    print(f"{round(x, 2)} {operation} {round(y, 2)} = {round(result, 2)}")
