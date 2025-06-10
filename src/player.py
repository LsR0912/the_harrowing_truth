from utils.print_helper import slow_print
from rich.console import Console
from rich.table import Table
from item import Item
import json

class Player:
    def __init__(self):
        self.name = ""
        self.level = 1
        self.xp = 0
        self.inventory = []
        self.xp_to_next_level = 100

    # This method prints the player's stats, including the player's name, current level, and current experience points.
    def show_stats(self):
         slow_print(f"Name: {self.name}\nLevel: {self.level}\nXP: {self.xp}")

    # This method adds a specified amount of experience points to the player's total.
    # It also checks if the player has gained enough experience to level up.
    def add_xp(self, amount):
            self.xp += amount
            slow_print(f"You gained {amount} XP!")
            while self.xp >= self.xp_to_next_level:
                self.xp -= self.xp_to_next_level
                self.level_up()

    # This method increases the player's level and adjusts the amount of experience required to reach the next level.
    def level_up(self):
        self.level += 1
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5)  # Increase XP needed for next level
        slow_print(f"Congratulations! {self.name} reached level {self.level}!")    
        
    # This method prints the player's inventory. If the player has an inventory, 
    # it is displayed in a formatted table using the Table class from the rich library.
    # If the player's inventory is empty, it prints a message indicating that the inventory is empty.
    def show_inventory(self):
        if len(self.inventory) > 0:
            table = Table(title="Inventory")

            table.add_column("Item name", justify="right", style="green", no_wrap=True)
            table.add_column("Description", justify="center" ,style="cyan")

            for item in self.inventory:
                table.add_row(item.name,item.description)

            console = Console()
            console.print(table)
        else:
             slow_print("Your inventory is empty.")

    # This method saves the player's data to a JSON file.
    def save_player(self, filename="data/players.json"):
        player_data = {
            "name": self.name,
            "level": self.level,
            "xp": self.xp,
            "inventory": [item.name for item in self.inventory],
            "xp_to_next_level": self.xp_to_next_level
        }
        with open(filename, 'w') as f:
            json.dump(player_data, f, indent=4)
        slow_print(f"Player data saved to {filename}")

    # This method loads a player's data from a JSON file.
    def load_player(self, filename="data/players.json"):
        try:
            with open(filename, 'r') as f:
                player_data = json.load(f)
                self.name = player_data.get("name", self.name)
                self.level = player_data.get("level", self.level)
                self.xp = player_data.get("xp", self.xp)
                self.xp_to_next_level = player_data.get("xp_to_next_level", self.xp_to_next_level)
                self.inventory = [Item.get_item_by_name(item_name) for item_name in player_data.get("inventory", [])]
                return self
        except FileNotFoundError:
            slow_print(f"No saved player data found in {filename}. Starting a new game.")
         