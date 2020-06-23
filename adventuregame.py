import time
import random

def print_pause(text):
    print(text)
    time.sleep(2)

def intro(item, option):
    print_pause("You find yourself standing in a forest filled with birch trees and purple wildflowers.\n")
    print_pause("Rumor has it that a " + option + " is somewhere around here, and has been terrifying the nearby village.\n")
    print_pause("Curious, you approach the village to see what is going on. You see a fork in the road - right takes you to the big mansion on the hill, the left takes you to the village's well.\n")
    print_pause("In your hand, you hold your trusty pocket knife (always good for clipping thread and cutting fruit).")


def well(item, option):
    if "weapon" in item:
        print_pause("\nYou peer cautiously into the well.")
        print_pause("\nYou've been here before, and the fairy is gone."
                    " It's just a dry well now.")
        print_pause("\nYou walk back to the forest.\n")
    else:
        print_pause("\nYou see the well is boarded up.")
        print_pause("\nPrying the boards away, you hear a faint music in the depths.")
        print_pause("\nSuddenly, a magic fairy flies out and hovers before you!")
        print_pause("\nShe thanks you for freeing her and gives you a shiny sword and large shield as repayment")
        print_pause("\nYou pocket your trusty pocket knife and take the shiny sword and large shield with you.")
        print_pause("\nYou go back to the forest.\n")
        item.append("weapon")
    forest(item, option)

def mansion(item, option):
    print_pause("\nYou approach the courtyard of the mansion.")
    print_pause("\nYou are about to reach the door when "
                "you hear a loud noise and the " + option + " appears.")
    print_pause("Oh no! This is where the " + option + " has been hiding!")
    print_pause("\nThe " + option + " attacks you!\n")
    if "weapon" not in item:
        print_pause("You suddenly feel that this might not go well for you, "
                    "what with only having your normally trusty pocket knife.\n")
    while True:
        choice2 = input("Would you like to 1 - fight or 2 - "
                        "run away?")
        if choice2 == "1":
            if "weapon" in item:
                print_pause("\nAs the " + option + " moves to attack, "
                            "you grab hold of your new shiny sword and large shield.\n")
                print_pause("Your sword glints in the sun "
                            "as you brace yourself for the attack.")
                print_pause("\nThe " + option + " lunges towards you, but you slash your sword and quickly and defeat the creature!")
                print_pause("\nYou have rid the town of the " + option +
                            ". You are victorious!\n")
            else:
                print_pause("\nYou do your best...")
                print_pause("but your trusty pocket knife is no match for the "
                            + option + ".")
                print_pause("\nYou have been defeated!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run back into the forest. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            forest(item, option)
            break

def forest(item, option):
    print_pause("Enter 1 to go and see the mansion.")
    print_pause("Enter 2 to see the well.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            mansion(item, option)
            break
        elif choice1 == "2":
            well(item, option)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! Come again.\n\n\n")
    else:
        play_again()

def play_game():
    item = []
    option = random.choice(["dragon", "ogre", "wraith", "gorn", "godzilla", "cyclops"])
    intro(item, option)
    forest(item, option)


play_game()
