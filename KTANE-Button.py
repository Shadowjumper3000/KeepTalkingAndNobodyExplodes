"""Button Module Solver for Keep Talking and Nobody Explodes."""
from ktane_utils import get_yes_no_input, get_int_input, run_module

def main():
    """Take button inputs and determine further action."""
    button_color = input("Color of Button: ").strip().lower()
    label = input("Label on Button: ").strip().lower()
    
    if button_color == "blue" and label == "abort":
        hold_button()
    elif label == "detonate" and get_int_input("Number of Batteries: ", min_val=0) > 1:
        print("Press and immediately release the button")
    elif button_color == "white" and get_yes_no_input("Is there a lit CAR Indicator?"):
        hold_button()
    elif get_int_input("Number of Batteries: ", min_val=0) > 2 and get_yes_no_input("Is there a lit FRK Indicator?"):
        print("Press and immediately release the button")
    elif button_color == "yellow":
        hold_button()
    elif button_color == "red" and label == "hold":
        print("Press and immediately release the button")
    else:
        hold_button()

def hold_button():
    """Take Strip color and output correct release time."""
    strip_color = input("Hold button and check strip color: ").strip().lower()
    if strip_color == "blue":
        print("Release when the countdown timer has a 4 in any position")
    elif strip_color == "yellow":
        print("Release when the countdown timer has a 5 in any position")
    else:
        print("Release when the countdown timer has a 1 in any position")

if __name__ == "__main__":
    run_module(main)
