"""Complicated Wires Module Solver for Keep Talking and Nobody Explodes."""
from utils import get_yes_no_input, get_int_input, run_module

def main():
    """Solve Complicated Wires based on information given."""
    star = get_yes_no_input("Is there a Star Symbol?")
    led = get_yes_no_input("Is the LED on?")
    color_red = get_yes_no_input("Is the Wire Red?")
    color_blue = get_yes_no_input("Is the Wire Blue?")
    
    print("-------------------------------------------")
    
    # Simple binary encoding of the 4 conditions for cleaner logic
    code = (1 if color_blue else 0) + (2 if color_red else 0) + (4 if star else 0) + (8 if led else 0)
    
    # Decision tree based on the code
    if code in [0, 4, 8]:
        print("Cut the Wire")
    elif code in [1, 2, 3, 6]:
        serial_number()
    elif code in [5, 9, 12]:
        batteries()
    elif code in [7, 10, 13]:
        parallel_port()
    elif code in [11, 14, 15]:
        print("Do not cut the wire")

def batteries():
    """Check if bomb has 2 or more batteries."""
    if get_int_input("Number of Batteries: ", min_val=0) >= 2:
        print("Cut the wire")
    else:
        print("Do not cut the wire")

def parallel_port():
    """Check if bomb has a parallel port."""
    if get_yes_no_input("Does the bomb have a parallel port?"):
        print("Cut the Wire")
    else:
        print("Do not cut the wire")

def serial_number():
    """Check if last digit of serial number is even."""
    print("----------------------------------")
    if get_int_input("Last digit of the serial number: ", min_val=0, max_val=9) % 2 == 0:
        print("Cut the wire")
    else:
        print("Do not cut the Wire")

if __name__ == "__main__":
    run_module(main)