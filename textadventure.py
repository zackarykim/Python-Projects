locations = {
    "start": {"description": "You're at the beginning of your journey.", "exits": {"north": "forest"}, "actions": {"examine": "Examine the strange rock"}},
    "forest": {"description": "A dense forest surrounds you.", "exits": {"south": "start"}, "actions": {"pick flowers": "Pick some wildflowers"}}
}

def examine_rock():
    print("You examine the rock and find a hidden key.")

def pick_flowers():
    print("You picked some wildflowers. They smell lovely.")

def game_loop():
    current_location = "start"

    while True:
        print(locations[current_location]["description"])

        exits = locations[current_location]["exits"]
        actions = locations[current_location]["actions"]

        print("Exits:", ", ".join(exits.keys()))
        print("Actions:")
        for action, description in actions.items():
            print(f"  {action}: {description}")

        choice = input("What do you want to do? ")

        if choice in exits:
            current_location = exits[choice]
        elif choice in actions:
            globals()[choice]()  # Call the function dynamically
        elif choice == "quit":
            break
        else:
            print("Invalid choice.")

game_loop()