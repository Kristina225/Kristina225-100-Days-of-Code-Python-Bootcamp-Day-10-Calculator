# FUNCTIONS REQUESTING USER INPUT
import sys


def end_calculation() -> str:
    while True:
        end_calc = input("Would you like to start a new calculation or exit the program."
                                    "Enter 'r' to start a new calculation or 'q' to exit: ")
        if end_calc not in ("r", "q"):
            print("That's not a valid input. Please try again.")
        else:
            return end_calc


def continue_calculation(result: float) -> str:
    while True:
        cont_calc = input(f"Would you like to continue the calculation with"
                     f" the previous result of {round(result, 2)} as your first number?"
                        f"Enter 'y' or 'n': ")
        if cont_calc not in ("y", "n"):
            print("Please enter either 'y' or 'n': ")
        else:
            return cont_calc


def choose_operator(operations: dict) -> str:
    """Takes in a dictionary of operators, returns the operator entered by the user in a promp,
    after checking if the operator is in the dictionary"""
    operator = input("Please choose one of the operations above: ")
    while True:
        if operator not in operations.keys():
            operator = input("That's not a valid operation. Please enter '+', '-', '*', or '/'.")
        else:
            return operator


def choose_number(number_placement: str) -> float:
    """Takes in a string indicating the placement of the number in the equation (first or second),
    returns the number entered by the user in a promp, after checking the number's validity"""
    try:
        number = float(input(f"Please enter the {number_placement} number: "))
    except ValueError:
        print("That's not a valid number. Please enter a valid number.")
        return choose_number(number_placement)
    except Exception as e:
        sys.exit("Something went wrong. We apologize. Please restart the program.")
    else:
        return number
