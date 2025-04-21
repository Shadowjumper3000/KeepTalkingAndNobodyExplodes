"""
Main launcher for Keep Talking and Nobody Explodes module solvers.
"""

import os
import importlib.util
import glob
import sys
from utils import clear_screen, get_int_input, get_yes_no_input


def get_available_modules():
    """Find all KTANE modules in the current directory."""
    module_files = glob.glob("KTANE-*.py")
    modules = []

    for file in module_files:
        # Remove .py extension and keep the full filename for import
        module_name = file[6:-3]  # Just for display
        import_name = file[:-3]  # Keep KTANE- prefix for proper importing

        modules.append({"name": module_name, "file": file, "import_name": import_name})

    return modules


def display_menu(modules, bomb_info):
    """Display the main menu with all available modules and bomb information."""
    clear_screen()
    print("=" * 50)
    print("Keep Talking and Nobody Explodes - Module Solver".center(50))
    print("=" * 50)

    # Display bomb information
    print("\nCurrent Bomb Information:")
    print(f"Batteries: {bomb_info['batteries']}")
    print(
        f"Serial Number: {bomb_info['serial_number'] if bomb_info['serial_number'] else 'Unknown'}"
    )

    # Display indicators
    lit_indicators = [ind for ind, is_lit in bomb_info["indicators"].items() if is_lit]
    unlit_indicators = [
        ind for ind, is_lit in bomb_info["indicators"].items() if not is_lit
    ]

    if lit_indicators:
        print(f"Lit Indicators: {', '.join(lit_indicators)}")
    if unlit_indicators:
        print(f"Unlit Indicators: {', '.join(unlit_indicators)}")

    print("=" * 50)

    print("\nSelect a module to solve:\n")

    for i, module in enumerate(modules, 1):
        print(f"{i}. {module['name']}")

    print("\n-1. Start New Bomb")
    print("0. Exit")
    print("-" * 50)


def collect_bomb_information():
    """Collect general bomb information needed by multiple modules."""
    print("=" * 50)
    print("Bomb Information Setup".center(50))
    print("=" * 50)
    print("\nPlease provide the following information about the bomb:")

    batteries = get_int_input("Number of Batteries: ", min_val=0)

    serial_number = input("Serial Number (leave blank if unknown): ").strip().upper()

    # Collect indicators information
    indicators = {}

    # For backward compatibility, ensure CAR and FRK are still available
    indicators["CAR"] = get_yes_no_input("Is there a lit CAR indicator?", "N")
    indicators["FRK"] = get_yes_no_input("Is there a lit FRK indicator?", "N")

    # Ask if there are any additional indicators to enter
    if get_yes_no_input("Do you want to enter additional indicators?", "N"):
        print("\nEnter indicator information (empty label to finish):")
        print("Indicators are 3-letter labels with an LED that can be ON or OFF")

        while True:
            indicator_label = (
                input("Enter indicator label (3 letters, or empty to finish): ")
                .strip()
                .upper()
            )
            if not indicator_label:
                break

            if len(indicator_label) != 3:
                print(
                    "Warning: Indicator labels should be 3 letters. Please try again."
                )
                continue

            is_lit = get_yes_no_input(
                f"Is the {indicator_label} indicator lit (ON)?", "N"
            )
            indicators[indicator_label] = is_lit
            print(f"Added {indicator_label} indicator: {'LIT' if is_lit else 'UNLIT'}")

    return {
        "batteries": batteries,
        "serial_number": serial_number,
        "indicators": indicators,
    }


def main():
    """Main program loop."""
    modules = get_available_modules()

    clear_screen()
    print("Welcome to the KTANE Module Solver!")
    print("\nFirst, let's collect some information about the bomb.")
    bomb_info = collect_bomb_information()

    while True:
        display_menu(modules, bomb_info)

        choice = get_int_input(
            "\nEnter your choice: ", min_val=-1, max_val=len(modules)
        )

        if choice == 0:
            print("\nThank you for using the KTANE Module Solver!")
            break

        if choice == -1:
            print("\nStarting a new bomb setup...")
            bomb_info = collect_bomb_information()
            continue

        selected_module = modules[choice - 1]

        try:
            # Load the module directly from the file path
            module_path = os.path.abspath(selected_module["file"])
            module_name = selected_module["import_name"]

            # Use importlib.util for more direct module loading
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)

            clear_screen()
            print(f"Running {selected_module['name']} Module Solver...\n")

            # Run the main function with bomb information
            if hasattr(module, "main"):
                # Check if the main function can accept bomb_info parameter
                import inspect

                sig = inspect.signature(module.main)
                if len(sig.parameters) > 0:
                    module.main(bomb_info)
                else:
                    # For backwards compatibility with modules that don't accept bomb_info
                    module.main()

            input("\nPress Enter to return to the main menu...")

        except ImportError as e:
            print(f"Error importing module: {e}")
            input("\nPress Enter to continue...")
        except Exception as e:
            print(f"Error running module: {e}")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
