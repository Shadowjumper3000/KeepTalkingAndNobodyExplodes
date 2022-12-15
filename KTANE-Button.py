#Button Module
import os

#Take button inputs and determine further action
def main():
    buttonColor = str(input("Color of Button: ")).strip().lower()
    lable = str(input("Lable on Button: ")).strip().lower()
    if buttonColor == "blue" and lable == "abort":
        holdButton()
    elif lable == "detonate" and int(input("Number of Batteries: ")) > 1:
        print("Press and immediately release the button")
    elif buttonColor == "white" and str(input("Is there a lit CAR Indicator? (Y/N): ")).strip().upper() == "Y":
        holdButton()
    elif int(input("Number of Batteries: ")) > 2 and str(input("Is there a lit FRK Indicator? (Y/N): ")).strip().upper() == "Y":
        print("Press and immediately release the button")
    elif buttonColor == "yellow":
        holdButton()
    elif buttonColor == "red" and lable == "hold":
        print("Press and immediately release the button")
    else:
        holdButton()

#Take Strip color and output correct release time
def holdButton():
    stripColor = str(input("Hold button and check strip color: ")).strip().lower()
    if stripColor == "blue":
        print("Release when the countdown timer has a 4 in any position")
    elif stripColor == "yellow":
        print("Release when the countdown timer has a 5 in any position")
    else:
        print("Release when the countdown timer has a 1 in any position")

#Execute main and repeat functions
while True:
    main()
    print("----------------------------------")
    if input("Repeat the program? (Y/N): ").strip().upper() != 'Y':
        break
    os.system('cls' if os.name == 'nt' else 'clear')
    
