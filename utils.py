"""
Shared utilities for Keep Talking and Nobody Explodes solver modules.
"""
import os

def clear_screen():
    """Clear the terminal screen in a cross-platform way."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_yes_no_input(prompt, default=None):
    """
    Get a yes/no input from the user.
    
    Args:
        prompt (str): The prompt to display to the user
        default (str, optional): Default value ('Y' or 'N')
    
    Returns:
        bool: True for 'Y', False for 'N'
    """
    default_text = ""
    if default == "Y":
        default_text = " [Y/n]"
    elif default == "N":
        default_text = " [y/N]"
    else:
        default_text = " (Y/N)"
        
    while True:
        response = input(f"{prompt}{default_text}: ").strip().upper()
        
        if response == "" and default:
            return default == "Y"
        
        if response in ["Y", "YES"]:
            return True
        elif response in ["N", "NO"]:
            return False
        else:
            print("Please enter 'Y' or 'N'.")

def get_int_input(prompt, min_val=None, max_val=None):
    """
    Get an integer input from the user within optional bounds.
    
    Args:
        prompt (str): The prompt to display to the user
        min_val (int, optional): Minimum acceptable value
        max_val (int, optional): Maximum acceptable value
    
    Returns:
        int: The validated integer input
    """
    while True:
        try:
            value = int(input(prompt))
            
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}.")
                continue
                
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}.")
                continue
                
            return value
        except ValueError:
            print("Please enter a valid number.")

def repeat_program():
    """
    Ask if the user wants to repeat the program and clear screen if yes.
    
    Returns:
        bool: True if the program should repeat, False otherwise
    """
    repeat = get_yes_no_input("Repeat the program?", "N")
    if repeat:
        clear_screen()
    return repeat

def run_module(main_function):
    """
    Run a module's main function in a loop until the user chooses to exit.
    
    Args:
        main_function (callable): The main function to run
    """
    while True:
        main_function()
        print("----------------------------------")
        if not repeat_program():
            break