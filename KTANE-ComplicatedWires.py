#Solve Complicated Wires based on information given

import os

def main():
    star = str(input("Is there a Star Symbol? (Y/N): ")).strip().upper()
    led = str(input("Is the LED on? (Y/N): ")).strip().upper()
    colorRed = str(input("Is the Wire Red? (Y/N): ")).strip().upper()
    colorBlue = str(input("Is the Wire Blue? (Y/N): ")).strip().upper()
    print("-------------------------------------------")
    if colorBlue == "N" and colorRed == "N" and star == "N" and led == "N":
        print("Cut the Wire")
    elif colorBlue == "Y" and colorRed == "N" and star == "N" and led == "N":
        serialNumber()
    elif colorBlue == "N" and colorRed == "Y" and star == "N" and led == "N":
        serialNumber()
    elif colorBlue == "Y" and colorRed == "Y" and star == "N" and led == "N":
        serialNumber()
    elif colorBlue == "N" and colorRed == "N" and star == "Y" and led == "N":
        print("Cut the wire")
    elif colorBlue == "N" and colorRed == "N" and star == "N" and led == "Y":
        print("Do not cut the wire")
    elif colorBlue == "N" and colorRed == "N" and star == "Y" and led == "Y":
        batteries()
    elif colorBlue == "N" and colorRed == "Y" and star == "Y" and led == "N":
        print("Cut the wire")
    elif colorBlue == "Y" and colorRed == "N" and star == "N" and led == "Y":
        parallelPort()
    elif colorBlue == "Y" and colorRed == "N" and star == "Y" and led == "N":
        print("Do not cut the wire")
    elif colorBlue == "N" and colorRed == "Y" and star == "N" and led == "Y":
        batteries()
    elif colorBlue == "Y" and colorRed == "Y" and star == "Y" and led == "N":
        parallelPort()
    elif colorBlue == "Y" and colorRed == "Y" and star == "N" and led == "Y":
        serialNumber()
    elif colorBlue == "Y" and colorRed == "N" and star == "Y" and led == "Y":
        parallelPort()
    elif colorBlue == "N" and colorRed == "Y" and star == "Y" and led == "Y":
        batteries()
    elif colorBlue == "Y" and colorRed == "Y" and star == "Y" and led == "Y":
        print("Do not cut the wire")

def batteries():
    if int(input("Number of Batteries: ")) >= 2:
        print("Cut the wire ")
    else:
        print("Do not cut the wire")

def parallelPort():
    if str(input("Does the bomb have a parallel port? (Y/N): ")).strip().upper() != "Y":
        print("Do not cut the wire")
    else:
        print("Cut the Wire")

def serialNumber():
    print("----------------------------------")
    if int(input("Last digit of the serial number: ")) % 2 == 0:
        print("Cut the wire")
    else:
        print("Do not cut the Wire")

while True:
    main()
    print("----------------------------------")
    if input("Repeat the program? (Y/N): ").strip().upper() != 'Y':
        break
    os.system('cls' if os.name == 'nt' else 'clear')