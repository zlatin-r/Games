import random

computer_choice = random.randint(1, 100)

while True:
    player_choice = input("Enter your guess: ")

    if not player_choice.isdigit():
        print("Your guess is not a number. Try again...")
        continue

    if int(player_choice) > computer_choice:
        print("Your guess is higher than the computer's number")
    elif int(player_choice) < computer_choice:
        print("Your guess is lower than the computer's number")
    else:
        break

print(f"{computer_choice} is correct!")
