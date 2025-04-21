"""Button Module Solver for Keep Talking and Nobody Explodes."""

from utils import get_yes_no_input, get_int_input, run_module


def main(bomb_info=None):
    """Take button inputs and determine further action."""
    button_color = input("Color of Button: ").strip().lower()
    label = input("Label on Button: ").strip().lower()

    # Get battery count from passed bomb info or ask if not available
    batteries = bomb_info.get("batteries") if bomb_info else None
    if batteries is None:
        batteries = get_int_input("Number of Batteries: ", min_val=0)

    # Get indicator info from passed bomb info or ask if not available
    # We'll handle both the standard CAR/FRK as well as any other indicators
    indicators = bomb_info.get("indicators", {}) if bomb_info else {}

    # Check for CAR indicator
    has_car = indicators.get("CAR")
    if has_car is None:
        has_car = get_yes_no_input("Is there a lit CAR indicator?")

    # Check for FRK indicator
    has_frk = indicators.get("FRK")
    if has_frk is None:
        has_frk = get_yes_no_input("Is there a lit FRK indicator?")

    if button_color == "blue" and label == "abort":
        hold_button()
    elif label == "detonate" and batteries > 1:
        print("Press and immediately release the button")
    elif button_color == "white" and has_car:
        hold_button()
    elif batteries > 2 and has_frk:
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
