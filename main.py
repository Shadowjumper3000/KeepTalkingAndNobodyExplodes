"""
Main launcher for Keep Talking and Nobody Explodes module solvers.
"""
import os
import importlib.util
import glob
import sys
from utils import clear_screen, get_int_input

def get_available_modules():
    """Find all KTANE modules in the current directory."""
    module_files = glob.glob("KTANE-*.py")
    modules = []
    
    for file in module_files:
        # Remove .py extension and keep the full filename for import
        module_name = file[6:-3]  # Just for display
        import_name = file[:-3]  # Keep KTANE- prefix for proper importing
        
        modules.append({
            "name": module_name,
            "file": file,
            "import_name": import_name
        })
    
    return modules

def display_menu(modules):
    """Display the main menu with all available modules."""
    clear_screen()
    print("=" * 50)
    print("Keep Talking and Nobody Explodes - Module Solver".center(50))
    print("=" * 50)
    print("\nSelect a module to solve:\n")
    
    for i, module in enumerate(modules, 1):
        print(f"{i}. {module['name']}")
    
    print("\n0. Exit")
    print("-" * 50)

def main():
    """Main program loop."""
    modules = get_available_modules()
    
    while True:
        display_menu(modules)
        
        choice = get_int_input("\nEnter your choice: ", min_val=0, max_val=len(modules))
        
        if choice == 0:
            print("\nThank you for using the KTANE Module Solver!")
            break
        
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
            
            # Run the main function
            if hasattr(module, "main"):
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