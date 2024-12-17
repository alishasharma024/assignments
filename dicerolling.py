import random

# Define the dice faces
dice_faces = {
    1: ["[-----]", "[     ]", "[ 0 ]", "[     ]", "[-----]"],
    2: ["[-----]", "[ 0   ]", "[     ]", "[   0 ]", "[-----]"],
    3: ["[-----]", "[     ]", "[0 0 0]", "[     ]", "[-----]"],
    4: ["[-----]", "[0 0 ]", "[     ]", "[0 0 ]", "[-----]"],
    5: ["[-----]", "[0 0 ]", "[ 0 ]", "[0 0 ]", "[-----]"],
    6: ["[-----]", "[0 0 0]", "[     ]", "[0 0 0]", "[-----]"]
}

def roll_dice():
    # Generates a random number between 1 and 6 (inclusive)
    return random.randint(1, 6)

def print_dice(face):
    # Print the dice face
    for line in dice_faces[face]:
        print(line)

def main():
    x = "y"
    while x.lower() == "y":
        face = roll_dice()
        print_dice(face)
        x = input("Press 'y' to roll again and 'n' to exit: ")
        print("\n")

if __name__ == "__main__":
    main()
