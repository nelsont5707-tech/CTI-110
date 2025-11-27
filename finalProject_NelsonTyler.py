# Tyler Nelson
# 11/27/2025
# Final Project
# This is a haunted house exploration game that allows you to walk through an old house trying to find the missing house deed before your courage or flashlight runs out.


import random
import time

def intro(player):
    print("You’re standing inside the Enfield House. It’s quiet, dusty, and way colder than it should be.")
    time.sleep(1)
    player["name"] = input("Before you look around… what's your name? ")
    print(f"\nAlright {player['name']}, your goal is simple: find the house deed and get out.\n")
    time.sleep(1)

def explore(player):
    print("\nYou push open the creaky door…")
    time.sleep(1)

    event = random.choice(["clue", "item", "cold_spot", "flashlight", "ghost", "deed", "nothing"])

    if event == "clue":
        clue = random.choice([
            "A note carved into the wall: 'Check the places no one likes.'",
            "A chalk arrow pointing upward… maybe the attic?",
            "Dust patterns suggest something was dragged toward the back room."
        ])
        player["clues"].append(clue)
        print(f"📄 You found a clue: {clue}")

    elif event == "item":
        item = random.choice(["Old Key", "Candle Stub", "Rusty Locket", "Broken Compass"])
        player["inventory"].append(item)
        print(f"🪄 You pick up a {item}. Not sure if it’s useful, but okay.")

    elif event == "cold_spot":
        loss = random.randint(5, 15)
        player["courage"] -= loss
        print(f"🥶 You walk through a cold spot. You lose {loss} courage.")

    elif event == "flashlight":
        drain = random.randint(5, 20)
        player["flashlight"] -= drain
        print(f"🔦 Your flashlight flickers hard. -{drain}% battery.")

    elif event == "ghost":
        print("👻 A ghost casjumps out and nudges past you.")
        if player["inventory"]:
            random.shuffle(player["inventory"])
            print("Your stuff is now in a different order. Great.")

    elif event == "deed":
        print("📜 You spot a folded paper under a loose floorboard… It's the house deed!")
        player["found_deed"] = True

    else:
        print("Nothing here but dust and old floorboards.")

    print(f"Stats → Courage: {player['courage']} | Flashlight: {player['flashlight']}% | Items: {player['inventory']} | Clues: {len(player['clues'])}")
    time.sleep(1)

def use_item(player):
    if not player["inventory"]:
        print("\nYou check your pockets… nothing useful in there.")
        return

    print("\nYour items:", player["inventory"])
    choice = input("Which item do you want to use? ").strip()

    if choice not in player["inventory"]:
        print("You don't have that item.")
        return
    
    if choice == "Candle Stub":
        print("🕯️ You light the candle. Its glow steadies your nerves. +10 courage.")
        player["courage"] += 10

    elif choice == "Rusty Locket":
        print("📿 You hold the locket. The familiar warmth calms you. +5 courage.")
        player["courage"] += 5

    elif choice == "Old Key":
        print("🔑 You jingle the old key. It doesn't unlock anything… but it feels important.")

    elif choice == "Broken Compass":
        print("🧭 The compass spins wildly. It does absolutely nothing.")

    player["inventory"].remove(choice)
    print(f"Updated Courage: {player['courage']}")
    time.sleep(1)

def main():
    player = {
        "name": "",
        "courage": 100,
        "flashlight": 60,
        "inventory": [],
        "clues": [],
        "found_deed": False
    }

    intro(player)

    while player["courage"] > 0 and player["flashlight"] > 0:
        if player["found_deed"]:
            print("\nYou tuck the deed into your pocket and head for the exit.")
            time.sleep(1)
            print("🏁 You’re out. House explored. Mission complete.")
            break

        print("\nWhat do you want to do?")
        print("1. Explore another room")
        print("2. Use an item")
        print("3. Leave the house")

        choice = input("Choose 1, 2, or 3: ").strip()

        if choice == "1":
            explore(player)
            player["flashlight"] -= 3  

        elif choice == "2":
            use_item(player)

        elif choice == "3":
            print("\nYou decide to head back toward the entrance.")
            break

        else:
            print("Invalid choice. Try again.")

    if player["courage"] <= 0:
        print("\nYou lose your nerve and run out of the house empty-handed.")
    elif player["flashlight"] <= 0:
        print("\nYour flashlight dies completely. You decide it's not worth tripping in the dark.")

    print("\nFinal Stats:", player)

main()
