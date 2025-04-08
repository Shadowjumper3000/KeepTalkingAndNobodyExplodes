"""Password Module Solver for Keep Talking and Nobody Explodes."""
from utils import run_module, clear_screen

# Passwords of Identification Code 241
PASSWORDS = [
    "about", "after", "again", "below", "could", 
    "every", "first", "found", "great", "house",
    "large", "learn", "never", "other", "place", 
    "plant", "point", "right", "small", "sound", 
    "spell", "still", "study", "their", "there", 
    "these", "thing", "think", "three", "water", 
    "where", "which", "world", "would", "write"
]

def main():
    """Take input of column letters and find possible passwords."""
    letters = 6
    columns = []
    
    # Take input of individual columns as lists
    for c in range(5):
        columns.append([])
        print(f"Enter all letters of column {c+1} (one at a time):")
        
        for l in range(letters):
            letter = input(f"Letter {l+1}: ").strip().lower()
            columns[-1].append(letter)
            
            # Show the current state after each entry
            clear_screen()
            print(f"Column {c+1}: {', '.join(columns[-1])}")
    
    clear_screen()
    print("Columns entered:")
    for i, col in enumerate(columns, 1):
        print(f"Column {i}: {', '.join(col)}")
    print("\nPossible passwords:")
    
    # Check each password against the column letters
    possible_passwords = []
    for p in PASSWORDS:
        valid = True
        for l in range(len(p)):
            if p[l] not in columns[l]:
                valid = False
                break
        if valid:
            possible_passwords.append(p)
    
    # Display the results
    if possible_passwords:
        for p in possible_passwords:
            print(f"- {p}")
    else:
        print("No matching passwords found. Please check your inputs.")

if __name__ == "__main__":
    run_module(main)


