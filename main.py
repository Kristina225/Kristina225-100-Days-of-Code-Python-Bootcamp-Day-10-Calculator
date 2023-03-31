from helper_functions.calculation_functions import add, subtract, multiply, divide
from helper_functions.user_input_functions import choose_number, choose_operator, continue_calculation, end_calculation
from helper_functions.other_helper_functions import clear_screen, print_operations, print_calculation_result
from helper_functions.other_helper_functions import print_game_logo
from variables.art import logo

OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


# FEEL TOO COMPLICATED. SEE IF YOU CAN SIMPLIFY IT.
def play_calculator() -> None:
    """Calculator program for: adding, subtracting, multiplying or dividing"""
    print_game_logo(logo)
    first_number = choose_number("first")
    print_operations(OPERATIONS)
    while True:
        operator = choose_operator(OPERATIONS)
        operation_fn = OPERATIONS[operator]
        next_number = choose_number("next")
        result = operation_fn(first_number, next_number)
        print_calculation_result(first_number, next_number, operator, result)
        if continue_calculation(result) == 'y':
            first_number, next_number = result, 0
        else:
            restart_or_quit = end_calculation()
            if restart_or_quit == "r":
                clear_screen()
                # QUESTION FRO ZDRAVKO: what if the user keeps doing new calculations?
                # function will keep calling itself and eventually program will crash?
                # feels like this is bad design. ask Zdravko if I need to think of a better solution?
                return play_calculator()
            elif restart_or_quit == "q":
                print("Thank you for using our calculator. Come back any time!")
                break


if __name__ == "__main__":
    play_calculator()
