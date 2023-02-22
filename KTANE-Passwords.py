#Password Module
import os

#Passwords of Identification Code 241
passwords = ["about", "after", "again", "below", "could", 
"every", "first", "found", "great", "house",
"large", "learn", "never", "other", "place", 
"plant", "point", "right", "small", "sound", 
"spell", "still", "study", "their", "there", 
"these", "thing", "think", "three", "water", 
"where", "which", "world", "would", "write"]

def main():
    #Take Input of individual columns as lists
    letters = 6
    columns = []
    for c in range(5):
        columns.append([])
        for l in range(letters):
            columns[-1].append(input("Enter all Letters of " + str(c+1) + " column: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            print(columns)

    #Go through each Word of password and check if containing letters
    for p in passwords:
        for l in range(len(p)):
            if p[l] in columns[l]:
                if l == 4:
                    print(p)
            else:
                break

#Execute main and repeat functions
while True:
    main()
    print("----------------------------------")
    if input("Repeat the program? (Y/N): ").strip().upper() != 'Y':
        break
    os.system('cls' if os.name == 'nt' else 'clear')
    

