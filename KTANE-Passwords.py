"""Password Module Solver for Keep Talking and Nobody Explodes."""

from utils import run_module, clear_screen

# Passwords of Identification Code 241
PASSWORDS = [
    "about",
    "after",
    "again",
    "below",
    "could",
    "every",
    "first",
    "found",
    "great",
    "house",
    "large",
    "learn",
    "never",
    "other",
    "place",
    "plant",
    "point",
    "right",
    "small",
    "sound",
    "spell",
    "still",
    "study",
    "their",
    "there",
    "these",
    "thing",
    "think",
    "three",
    "water",
    "where",
    "which",
    "world",
    "would",
    "write",
]


def filter_passwords(columns):
    """Filter passwords based on entered columns."""
    possible_passwords = []
    for p in PASSWORDS:
        valid = True
        for col_idx in range(len(columns)):
            if col_idx < len(p) and p[col_idx] not in columns[col_idx]:
                valid = False
                break
        if valid:
            possible_passwords.append(p)
    return possible_passwords


def main():
    """Take input of column letters and find possible passwords."""
    letters = 6
    columns = []
    possible_passwords = PASSWORDS.copy()

    # Take input of individual columns as lists
    for c in range(5):
        columns.append([])
        print(f"Enter all letters of column {c+1} (one at a time):")

        for letter_idx in range(letters):
            letter = input(f"Letter {letter_idx+1}: ").strip().lower()
            columns[-1].append(letter)

            # Show the current state after each entry
            clear_screen()
            print(f"Column {c+1}: {', '.join(columns[-1])}")

        # Check if we can determine the password after this column
        possible_passwords = filter_passwords(columns)
        clear_screen()
        print("Columns entered:")
        for i, col in enumerate(columns, 1):
            print(f"Column {i}: {', '.join(col)}")
        print(f"\nPossible passwords ({len(possible_passwords)}):")

        if possible_passwords:
            for p in possible_passwords:
                print(f"- {p}")

            # If only one possibility found, no need to enter more columns
            if len(possible_passwords) == 1:
                print(f"\nSolution found: {possible_passwords[0]}")
                return
        else:
            print("No matching passwords found. Please check your inputs.")
            return

        # If we still have columns to go, ask if user wants to continue
        if c < 4:
            print("\nContinue with next column? (y/n)")
            if input().lower() != "y":
                return


if __name__ == "__main__":
    run_module(main)
