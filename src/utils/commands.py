from utils.print_helper import slow_print

valid_commands = ["go","look","take","examine","help","inventory","stats","talk","quit"]

def command_function(game, command):
    command = command.lower().strip()
    command_parts = command.split()
    if not command_parts:
        slow_print("Please enter a command.")
        return

    cmd = command_parts[0]
    args = command_parts[1:]

    # Step 1: Validate the command
    if cmd not in valid_commands:
        slow_print(f"Invalid command: '{cmd}'. Use 'help' for a list of valid commands.")
        return

    # Step 2: Execute the command based on its type
    if cmd == "go":
        if len(args) != 1:
            slow_print("Usage: go <direction>")
        else:
            game.handle_go_command(args[0])
    elif cmd == "look":
        game.look()
    elif cmd == "inventory":
        game.player.show_inventory()
    elif cmd == "help":
        show_help(game)
    elif cmd == "stats":
        game.player.show_stats()
    elif cmd == "quit":
        game.quit_game()
    elif cmd == "examine":
        item = next((item for item in game.player.inventory if item.name.lower() == args[0].lower()),None)
        item.examine_item()
    elif cmd == "talk":
        game.talk()
    elif cmd == "take":
        if len(args) != 1:
            slow_print("Usage: take <item>")
        else:
            game.take_item(args[0])

def show_help(game):
    slow_print("Here are the available commands:")
    slow_print("- go [direction]: Move in the specified direction (e.g., 'go north').")
    slow_print("- look: Look around the current room and see its description.")
    slow_print("- inventory: Shows the contents of your inventory.")
    slow_print("- stats: Shows the current statistics of your character.")
    slow_print("- talk: Talk with persons in the current room.")
    slow_print("- take: Take an item from the current room.")
    slow_print("- examine [item]: Examine an item in the room or your inventory.")
    slow_print("- help: Show this help message.")
    slow_print("- quit: Exit the game.")  
    game.show_status()  
    
    