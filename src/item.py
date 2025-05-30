from utils.print_helper import slow_print

class Item:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def get_items():
        return items
    
    def examine_item(self):
        slow_print(f"You examine the {self.name}\n{self.description}")        

items = {
    "1": Item("1", "Workshed_Key", "A small key that looks like it could open a door."),
    "2": Item("2", "Map", "A map of the area, showing various locations. Main Hall, Kitchen, Library, Workshed."),
    "3": Item("3", "Chainsaw", "In case you miss a hand, feel free to replace it with the chainsaw."),
    "4": Item("4", "Note", "A note that says 'Only fools can read this!'."),
    "5": Item("5", "Book", "The cover of this book says: 'Clean Code'"),
    "6": Item("6", "Necromonicon", "A book of the dead, it is said to contain dark magic.")
}  
