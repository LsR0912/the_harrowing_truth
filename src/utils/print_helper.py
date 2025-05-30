import time
import os

@staticmethod
def slow_print(text,delay=0.02):
    for char in text:
        print(char,end='',flush=True)
        time.sleep(delay)
    print()

@staticmethod    
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m' 