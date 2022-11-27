#Take Input Number and give Number or ask for further Input


#Stage 1
def stage_1():
    print("Stage 1")
    number.append(str(input("Number: ")))
    if number[0] == "1": 
        print("Select Position 2")
        position.append("2")
    elif number[0] == "2":
        print("Select Position 2")
        position.append("2")
    elif number[0] == "3":
        print("Select Position 3")
        position.append("3")
    elif number[0] == "4":
        print("Select Position 4")
        position.append("4")
    else:
        raise ValueError("Given Number not in acceptable range")
    selected.append(str(input("Selected Number: ")))
    print("------------------------------")

#Stage 2
def stage_2():
    print("Stage 2")
    number.append(str(input("Number: ")))
    if number[1] == "1": 
        print("Select Number 4")
        selected.append("4")
        position.append(str(input("Position of Selected Number: ")))
    elif number[1] == "2":
        print("Select Position " + position[0])
        position.append("2")
    elif number[1] == "3":
        print("Select Position 1")
        position.append("1")
        selected.append(str(input("Selected Number: ")))
    elif number[1] == "4":
        print("Select Position " + position[0])
        position.append("4")
    else:
        raise ValueError("Given Number not in acceptable range")
    print("------------------------------")

#Stage 3
def stage_3():
    print("Stage 3")
    number.append(str(input("Number: ")))
    if number[2] == "1": 
        print("Select Number " + selected[1])
        selected.append(selected[1])
        position.append(str(input("Position of Selected Number: ")))
    elif number[2] == "2":
        print("Select Number " + selected[0])
        selected.append(selected[0])
        position.append(str(input("Position of Selected Number: ")))
    elif number[2] == "3":
        print("Select Position 3")
        position.append("3")
        selected.append(str(input("Selected Number: ")))
    elif number[2] == "4":
        print("Select Number 4")
        selected.append("4")
        position.append(str(input("Position of Selected Number: ")))
    else:
        raise ValueError("Given Number not in acceptable range")
    print("------------------------------")

#Stage 4
def stage_4():
    print("Stage 4")
    number.append(str(input("Number: ")))
    if number[3] == "1": 
        print("Select Position " + position[0])
        position.append(position[0])
        selected.append(str(input("Selected Number: ")))
    elif number[3] == "2":
        print("Select Position 1")
        position.append("1")
        selected.append(str(input("Selected Number: ")))
    elif number[3] == "3":
        print("Select Position " + position[1])
        position.append(position[1])
        selected.append(str(input("Selected Number: ")))
    elif number[3] == "4":
        print("Select Position " + position[1])
        position.append(position[1])
        selected.append(str(input("Selected Number: ")))
    else:
        raise ValueError("Given Number not in acceptable range")
    print("------------------------------")

#Stage 5
def stage_5():
    print("Stage 5")
    number.append(str(input("Number: ")))
    if number[4] == "1": 
        print("Select Number " + selected[0])
        selected.append(selected[0])
        position.append(str(input("Position of Selected Number: ")))
    elif number[4] == "2":
        print("Select Number " + selected[1])
        selected.append(selected[1])
        position.append(str(input("Position of Selected Number: ")))
    elif number[4] == "3":
        print("Select Number " + selected[3])
        selected.append(selected[3])
        position.append(str(input("Position of Selected Number: ")))
    elif number[4] == "4":
        print("Select Number " + selected[2])
        selected.append(selected[2])
        position.append(str(input("Position of Selected Number: ")))
    else:
        raise ValueError("Given Number not in acceptable range")
    print("------------------------------")

number = []
position = []
selected = []


stage_1()
stage_2()
stage_3()
stage_4()
stage_5()


print(number)
print(position)
print(selected)