#Simple Wires

import os

def main():
    numberWires = int(input("Number of wires: "))
    if numberWires == 3:
        wires_3()
    elif numberWires == 4:
        wires_4()
    elif numberWires == 5:
        wires_5()
    elif numberWires == 6:
        wires_6()

def wires_3():
    if str(input("Are there red wires? (Y/N): ")).strip().upper() == "N":
        print("Cut the second wire")
    elif str(input("Is the last wire white? (Y/N): ")).strip().upper() == "Y":
        print("Cut the last wire")
    elif int(input("Number of blue wires: ")) > 1:
        print("Cut the last blue wire")
    else:
        print("Cut the last wire")

def wires_4():
    redWires = int(input("Number of red wires:"))
    if redWires > 1 and int(input("Last digit of serial number:")) % 2 == 1:
        print("Cut the last red wire")
    elif redWires == 0 and str(input("Is the last wire yellow? (Y/N): ")).strip().upper() == "Y":
        print("Cut the first wire")
    elif int(input("Number of blue wires: ")) == 1:
        print("Cut the first wire")
    elif int(input("Number of yellow wires: ")) > 1:
        print("Cut the last wire")
    else:
        print("Cut the second wire")

def wires_5():
    if str(input("Is the last wire black? (Y/N): ")).strip().upper() == "Y" and int(input("Last digit of serial Number: ")) % 2 == 1:
        print("Cut the fourth wire")
    elif int(input("Number of red wires: ")) == 1 and int(input("Number of yellow wires:")) > 1:
        print("Cut the second wire")
    elif str(input("Are there black wires? (Y/N): ")).strip().upper() == "N":
        print("Cut the second wire")
    else:
        print("Cut the first wire")

def wires_6():
    yellowWires = int(input("How many yellow wires are there:"))
    if yellowWires == 0 and int(input("Last digit of serial number: ")) % 2 == 1:
        print("Cut the third wire")
    elif yellowWires == 1 and int(input("Number of white wires: ")) > 1:
        print("Cut the fourth wire")
    elif int(input("Number of red wires: ")) == 0:
        print("Cut the last wire")
    else:
        print("Cut the fourth wire")

while True:
    main()
    print("----------------------------------")
    if input("Repeat the program? (Y/N): ").strip().upper() != 'Y':
        break
    os.system('cls' if os.name == 'nt' else 'clear')