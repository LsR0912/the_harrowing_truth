from utils.print_helper import slow_print, clear_console, Color as cp  # color printer
from utils.commands import command_function
from player import Player
from room import Room

class Game:
    """Main game class for The Harrowing Truth."""

    def __init__(self):
        self.player = Player()
        self.rooms = Room.get_rooms()
        self.location = self.rooms.get("1")
        self.isRunning = True
        if not self.location:
            raise ValueError("Starting room '1' not found.")

    # This method starts the game and sets up the initial environment. It clears the console, initializes the game, and prints the welcome message.
    def start_game(self):
        """Starts the game and main loop."""
        clear_console()
        self.init_game()
        slow_print(f"Welcome to {cp.RED}The Harrowing Truth{cp.RESET}, a dark and {cp.RED}bloody{cp.RESET} text adventure!")
        slow_print(f"Welcome, {self.player.name}!")
        self.show_status()
        self.main_loop()

    def show_exits(self):
        slow_print("Available exits:")
        for exit in self.location.exits:
            slow_print(f"\t- {cp.CYAN}{exit}{cp.RESET}")

    def show_npcs(self):
        if self.location.npcs:
            slow_print("Persons in this room:")
            for npc in self.location.npcs:
                slow_print(f"\t- {cp.BLUE}{npc.name}{cp.RESET}")

    # This method prints the current status of the game, including the player's name, the current room, 
    # available exits, NPCs, and any items in the room.
    def show_status(self):
        slow_print("Type 'help' to see the available commands")
        slow_print(f"You are now in the {cp.YELLOW}{self.location.name}{cp.RESET}")
        self.show_exits()
        self.show_npcs()
        if self.location.items:
            self.location.show_items()
        slow_print("What do you want to do?")

    # This method handles the player's command to move to a new room. 
    # It checks if the specified direction is valid and, if so, updates the player's location to the next room. 
    # If the next room requires a key that the player doesn't have, it prompts the player to use the key or re-enter the direction.
    def handle_go_command(self, direction):
        if direction not in self.location.exits:
            slow_print("You can't go that way.")
            return

        nextRoom = self.rooms[self.location.exits[direction]]
        if getattr(nextRoom, 'requires_key', None):
            required_key = nextRoom.requires_key
            key_item = next((item for item in self.player.inventory if item.name.lower() == required_key.lower()), None)
            if not key_item:
                slow_print(f"You need the {required_key} to enter this room.")
                return
            slow_print(f"You open the door to the {nextRoom.name} with the {required_key}!")
            self.player.inventory.remove(key_item)
            nextRoom.requires_key = None

        self.location = nextRoom
        slow_print(f"You go {direction}")
        self.show_status()

    # This method allows the player to look around the current room and view the exits and any items in the room.
    def look(self):
        self.location.show_room()
        self.show_exits()
        if self.location.items:
            self.location.show_items()

    # This method allows the player to take an item from the current room. 
    # If the item exists, it is added to the player's inventory, removed from the room, and the player's experience points are increased. 
    # The player's inventory and current experience points are then displayed.
    def take_item(self, args):
        item_taken = next((room_item for room_item in self.location.items if room_item.name.lower() == args.lower()), None)
        if item_taken:
            self.player.inventory.append(item_taken)
            self.location.items.remove(item_taken)
            slow_print(f"You took the {item_taken.name}")
            self.player.add_xp(50)
            self.player.show_inventory()
        else:
            slow_print(f"There is no item named '{args}' here.")

    # This method allows the player to interact with NPCs in the current room. It prompts the player to choose an NPC to talk to and handles the conversation.
    def talk(self):
        if not self.location.npcs:
            slow_print("There is no one here to talk to.")
            return

        slow_print("Who do you want to talk to?")
        for idx, npc in enumerate(self.location.npcs, 1):
            slow_print(f"{idx}. {npc.name}")

        try:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(self.location.npcs):
                npc = self.location.npcs[choice]
                # npc.describe()
                dialogue, answers = npc.talk()
                while True:
                    slow_print(dialogue)
                    if not answers:
                        slow_print("The conversation ends.")
                        break
                    slow_print("How do you respond?")
                    for i, ans in enumerate(answers, 1):
                        slow_print(f"{i}. {ans}")
                    slow_print(f"{len(answers)+1}. End conversation")
                    try:
                        ans_choice = int(input("> ")) - 1
                        if 0 <= ans_choice < len(answers):
                            response = answers[ans_choice]
                            npc.respond(response)
                            dialogue, answers = npc.talk()
                        elif ans_choice == len(answers):
                            slow_print("You end the conversation.")
                            break
                        else:
                            slow_print("Invalid answer choice.")
                    except ValueError:
                        slow_print("Please enter a valid number.")
            else:
                slow_print("Invalid choice.")
        except ValueError:
            slow_print("Please enter a valid number.")

    def quit_game(self):
        slow_print(f"Thanks for playing {self.player.name}, till next time!")
        self.isRunning = False

    def main_loop(self):
        """Main game loop."""
        while self.isRunning:
            command = input("> ").strip()
            clear_console()
            command_function(self, command)

    def init_player(self):
        self.player.name = input("Please enter your name: ")
        self.player.save_player()

    def init_game(self):
        """Initializes and returns a new Player object."""
        loaded_player = self.player.load_player()
        if loaded_player:
            self.player = loaded_player
        else:
            self.init_player()