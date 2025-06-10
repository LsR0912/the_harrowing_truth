from npc import NPC
from item import Item
from utils.print_helper import slow_print, Color as cp

class Room:
    def __init__(self,id,name,description,items=None,exits=None,npcs=None,requires_key=None):
        self.id = id
        self.name = name
        self.description = description
        self.items = items if items is not None else []
        self.exits = exits if exits is not None else {}
        self.npcs = npcs if npcs is not None else []
        self.requires_key = requires_key

    # This method prints the room's name and description using the slow_print function with color formatting.
    def show_room(self):
        slow_print(f"You're in the {cp.YELLOW}{self.name}{cp.RESET}, {self.description}")

    # This method returns the dictionary of rooms.
    def get_rooms():
        return rooms
    
    # This method prints the items in the room, with color formatting used to indicate different types of items.
    def show_items(self):
        slow_print(f"The room contains following items: ")
        if self.id == "3":
            for item in self.items: slow_print(f"\t- {cp.RED}{item.name}{cp.RESET}")
        else:
            for item in self.items: slow_print(f"\t- {cp.GREEN}{item.name}{cp.RESET}")

items = Item.get_items()
npcs = NPC.get_npcs()

rooms = {
"1" : Room("1","Main Hall","A dark and cold hall, a torch spends a dim light",[items["2"]], {"north" : "2","south" : "3"},[]),
"2" : Room("2","Kitchen","The smell of old iron is overwhelming, and a cleaver lies embedded in the table, surrounded by the chilling evidence of a brutal, final act.",[items["1"]], {"west" : "4","south" : "1"},[]),
"3" : Room("3","Workshed","A dark chamber, with a chainsaw on a workbench",[items["6"],items["3"]], {"north" : "1"},[],"Workshed_Key"),
"4" : Room("4","Library","A huge room, with an enormous amount of books",[items["5"],items["4"]], {"east" : "2"},[npcs["1"]]),
}