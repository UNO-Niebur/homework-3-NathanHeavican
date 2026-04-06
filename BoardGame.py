# Homework 3 - Board Game System
# Name: Nathan Heavican
# Date: 4/5/2026

def loadGameData(filename):
    """Reads game data and organizes it into a dictionary."""
    
    game = {
        "turn": "",
        "players": {},
        "events": {}
    }
    
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("Turn:"):
                game["turn"] = line.split(": ")[1]
            else:
                position, value = line.split(": ")
                position = int(position)
                if value.startswith("Player"):
                    game["players"][value] = position
                else:
                    game["events"][position] = value
    return game


def displayGame(data):
    """Displays the current game state."""
    print("\nCurrent Game State:")

    # turn
    print(f"Turn: {data['turn']}")

    # players
    print("\nPlayers:")
    for player, position in data["players"].items():
        print(f"{player} is at position {position}")

    # events
    print("\nEvents:")
    for position, event in data["events"].items():
        print(f"Space {position}: {event}")

def movePlayer(data):
    """Moves the current player forward."""
    player = data["turn"]
    print(f"\nIt is {player}'s turn.")

    move = int(input("Enter number of spaces to move: "))

    data["players"][player] = data["players"][player] + move
    new_position = data["players"][player]
    print(f"{player} moved to position {new_position}")
    if new_position in data["events"]:
        event = data["events"][new_position]
        print(f"{player} landed on {event}!")
    
    players = list(data["players"].keys())
    current_index = players.index(player)
    next_index = (current_index + 1) % len(players)
    data["turn"] = players[next_index]

    print(f"Next turn: {data['turn']}")


def main():
    filename = "events.txt"   # Students can rename if needed

    gameData = loadGameData(filename)
    displayGame(gameData)

    # Example interaction
    choice = input("\nMove player? (y/n): ")
    if choice.lower() == "y":
        movePlayer(gameData)
        displayGame(gameData)


if __name__ == "__main__":
    main()
