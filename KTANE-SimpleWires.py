"""Simple Wires Module Solver for Keep Talking and Nobody Explodes."""

from utils import get_yes_no_input, get_int_input, run_module


def main():
    """Simple Wires main solver function."""
    number_wires = get_int_input("Number of wires (3-6): ", min_val=3, max_val=6)

    if number_wires == 3:
        wires_3()
    elif number_wires == 4:
        wires_4()
    elif number_wires == 5:
        wires_5()
    elif number_wires == 6:
        wires_6()


def wires_3():
    """Logic for 3 wire cases."""
    if not get_yes_no_input("Are there red wires?"):
        print("Cut the second wire")
    elif get_yes_no_input("Is the last wire white?"):
        print("Cut the last wire")
    elif get_int_input("Number of blue wires: ", min_val=0) > 1:
        print("Cut the last blue wire")
    else:
        print("Cut the last wire")


def wires_4():
    """Logic for 4 wire cases."""
    red_wires = get_int_input("Number of red wires:", min_val=0)
    if (
        red_wires > 1
        and get_int_input("Last digit of serial number:", min_val=0, max_val=9) % 2 == 1
    ):
        print("Cut the last red wire")
    elif red_wires == 0 and get_yes_no_input("Is the last wire yellow?"):
        print("Cut the first wire")
    elif get_int_input("Number of blue wires: ", min_val=0) == 1:
        print("Cut the first wire")
    elif get_int_input("Number of yellow wires: ", min_val=0) > 1:
        print("Cut the last wire")
    else:
        print("Cut the second wire")


def wires_5():
    """Logic for 5 wire cases."""
    if (
        get_yes_no_input("Is the last wire black?")
        and get_int_input("Last digit of serial Number: ", min_val=0, max_val=9) % 2
        == 1
    ):
        print("Cut the fourth wire")
    elif (
        get_int_input("Number of red wires: ", min_val=0) == 1
        and get_int_input("Number of yellow wires:", min_val=0) > 1
    ):
        print("Cut the second wire")
    elif not get_yes_no_input("Are there black wires?"):
        print("Cut the second wire")
    else:
        print("Cut the first wire")


def wires_6():
    """Logic for 6 wire cases."""
    yellow_wires = get_int_input("How many yellow wires are there:", min_val=0)
    if (
        yellow_wires == 0
        and get_int_input("Last digit of serial number: ", min_val=0, max_val=9) % 2
        == 1
    ):
        print("Cut the third wire")
    elif yellow_wires == 1 and get_int_input("Number of white wires: ", min_val=0) > 1:
        print("Cut the fourth wire")
    elif get_int_input("Number of red wires: ", min_val=0) == 0:
        print("Cut the last wire")
    else:
        print("Cut the fourth wire")


if __name__ == "__main__":
    run_module(main)
