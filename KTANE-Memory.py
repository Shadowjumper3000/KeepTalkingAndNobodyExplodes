"""Memory Module Solver for Keep Talking and Nobody Explodes."""

from utils import get_int_input, run_module


def main():
    """Run the Memory module solver through all 5 stages."""
    # Initialize tracking arrays at the start
    number = []
    position = []
    selected = []

    # Run through all 5 stages
    stage_1(number, position, selected)
    stage_2(number, position, selected)
    stage_3(number, position, selected)
    stage_4(number, position, selected)
    stage_5(number, position, selected)

    # Show summary
    print("\nSummary:")
    print(f"Display numbers: {number}")
    print(f"Positions selected: {position}")
    print(f"Numbers selected: {selected}")


# Stage 1
def stage_1(number, position, selected):
    """Logic for stage 1 of the Memory module."""
    print("Stage 1")
    num = get_int_input("Number on display: ", min_val=1, max_val=4)
    number.append(str(num))

    if num == 1:
        print("Select Position 2")
        position.append("2")
    elif num == 2:
        print("Select Position 2")
        position.append("2")
    elif num == 3:
        print("Select Position 3")
        position.append("3")
    elif num == 4:
        print("Select Position 4")
        position.append("4")

    selected.append(str(get_int_input("Selected Number: ", min_val=1, max_val=4)))
    print("------------------------------")


# Stage 2
def stage_2(number, position, selected):
    """Logic for stage 2 of the Memory module."""
    print("Stage 2")
    num = get_int_input("Number on display: ", min_val=1, max_val=4)
    number.append(str(num))

    if num == 1:
        print("Select Number 4")
        selected.append("4")
        position.append(
            str(get_int_input("Position of Selected Number: ", min_val=1, max_val=4))
        )
    elif num == 2:
        print(f"Select Position {position[0]}")
        position.append(position[0])
        selected.append(str(get_int_input("Selected Number: ", min_val=1, max_val=4)))
    elif num == 3:
        print("Select Position 1")
        position.append("1")
        selected.append(str(get_int_input("Selected Number: ", min_val=1, max_val=4)))
    elif num == 4:
        print(f"Select Position {position[0]}")
        position.append(position[0])
        selected.append(str(get_int_input("Selected Number: ", min_val=1, max_val=4)))

    print("------------------------------")


# Stage 3
def stage_3(number, position, selected):
    """Logic for stage 3 of the Memory module."""
    print("Stage 3")
    num = get_int_input("Number on display: ", min_val=1, max_val=4)
    number.append(str(num))

    if num == 1:
        print(f"Select Number {selected[1]}")
        selected.append(selected[1])
        position.append(
            str(get_int_input("Position of Selected Number: ", min_val=1, max_val=4))
        )
    elif num == 2:
        print(f"Select Number {selected[0]}")
        selected.append(selected[0])
        position.append(
            str(get_int_input("Position of Selected Number: ", min_val=1, max_val=4))
        )
    elif num == 3:
        print("Select Position 3")
        position.append("3")
        selected.append(str(get_int_input("Selected Number: ", min_val=1, max_val=4)))
    elif num == 4:
        print("Select Number 4")
        selected.append("4")
        position.append(
            str(get_int_input("Position of Selected Number: ", min_val=1, max_val=4))
        )

    print("------------------------------")


# Stage 4
def stage_4(number, position, selected):
    """Logic for stage 4 of the Memory module."""
    print("Stage 4")
    num = get_int_input("Number on display: ", min_val=1, max_val=4)
    number.append(str(num))

    if num == 1:
        print(f"Select Position {position[0]}")
        position.append(position[0])
        selected.append(str(get_int_input("Selected Number: ", min_val=1, max_val=4)))
    elif num == 2:
        print("Select Position 1")
        position.append("1")
        selected.append(str(get_int_input("Selected Number: ", min_val=1, max_val=4)))
    elif num == 3:
        print(f"Select Position {position[1]}")
        position.append(position[1])
        selected.append(str(get_int_input("Selected Number: ", min_val=1, max_val=4)))
    elif num == 4:
        print(f"Select Position {position[1]}")
        position.append(position[1])
        selected.append(str(get_int_input("Selected Number: ", min_val=1, max_val=4)))

    print("------------------------------")


# Stage 5
def stage_5(number, position, selected):
    """Logic for stage 5 of the Memory module."""
    print("Stage 5")
    num = get_int_input("Number on display: ", min_val=1, max_val=4)
    number.append(str(num))

    if num == 1:
        print(f"Select Number {selected[0]}")
        selected.append(selected[0])
        position.append(
            str(get_int_input("Position of Selected Number: ", min_val=1, max_val=4))
        )
    elif num == 2:
        print(f"Select Number {selected[1]}")
        selected.append(selected[1])
        position.append(
            str(get_int_input("Position of Selected Number: ", min_val=1, max_val=4))
        )
    elif num == 3:
        print(f"Select Number {selected[3]}")
        selected.append(selected[3])
        position.append(
            str(get_int_input("Position of Selected Number: ", min_val=1, max_val=4))
        )
    elif num == 4:
        print(f"Select Number {selected[2]}")
        selected.append(selected[2])
        position.append(
            str(get_int_input("Position of Selected Number: ", min_val=1, max_val=4))
        )

    print("------------------------------")


if __name__ == "__main__":
    run_module(main)
