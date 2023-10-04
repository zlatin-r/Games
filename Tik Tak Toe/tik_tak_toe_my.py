def tictaktoe():
    display = [["*", "*", "*"],
               ["*", "*", "*"],
               ["*", "*", "*"]]
    print(" ".join(display[0]))
    print(" ".join(display[1]))
    print(" ".join(display[2]))
    for i in range(9):
        if i % 2 == 0:
            position_index = input("Enter row and colum: ").split(" ")
            row = int(position_index[0]) - 1
            col = int(position_index[1]) - 1
            display[row][col] = "X"
            print(" ".join(display[0]))
            print(" ".join(display[1]))
            print(" ".join(display[2]))
        else:
            position_index = input("Enter row and colum: ").split(" ")
            row = int(position_index[0]) - 1
            col = int(position_index[1]) - 1
            display[row][col] = "O"
            print(" ".join(display[0]))
            print(" ".join(display[1]))
            print(" ".join(display[2]))

        if display[0] == ["X", "X", "X"] or display[1] == ["X", "X", "X"] or display[2] == ["X", "X", "X"]:
            return "Winner X"
        elif display[0] == ["O", "O", "O"] or display[1] == ["O", "O", "O"] or display[2] == ["O", "O", "O"]:
            return "Winner O"

        elif display[0][0] + display[1][0] + display[2][0] == "XXX":
            return "Winner X"
        elif display[0][1] + display[1][1] + display[2][1] == "XXX":
            return "Winner X"
        elif display[0][2] + display[1][2] + display[2][2] == "XXX":
            return "Winner X"

        elif display[0][0] + display[1][1] + display[2][2] == "XXX":
            return "Winner X"
        elif display[0][2] + display[1][1] + display[2][0] == "XXX":
            return "Winner X"

        elif display[0][0] + display[1][0] + display[2][0] == "OOO":
            return "Winner O"
        elif display[0][1] + display[1][1] + display[2][1] == "OOO":
            return "Winner O"
        elif display[0][2] + display[1][2] + display[2][2] == "OOO":
            return "Winner O"

        elif display[0][0] + display[1][1] + display[2][2] == "OOO":
            return "Winner O"
        elif display[0][2] + display[1][1] + display[2][0] == "OOO":
            return "Winner O"
    else:
        return "No Winner"


print(tictaktoe())
