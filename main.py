from game.cpu import *
from colorama import Fore, Back
import os, sys, time

Ai = """
 █████╗ ██╗██╗██╗██╗██╗
██╔══██╗██║██║██║██║██║
███████║██║██║██║██║██║
██╔══██║██║╚═╝╚═╝╚═╝╚═╝
██║  ██║██║██╗██╗██╗██╗
╚═╝  ╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝
"""

Player = """
██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗ ██╗██╗██╗██╗
██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██║██║██║██║
██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝██║██║██║██║
██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗╚═╝╚═╝╚═╝╚═╝
██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║██╗██╗██╗██╗
╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝╚═╝╚═╝
"""
LOGO1 = """
        ██████╗  ██████╗  ██████╗██╗  ██╗       ██████╗  █████╗ ██████╗ ███████╗██████╗        ███████╗ ██████╗██╗███████╗███████╗ ██████╗ ██████╗ ███████╗
        ██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝       ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗       ██╔════╝██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
        ██████╔╝██║   ██║██║     █████╔╝        ██████╔╝███████║██████╔╝█████╗  ██████╔╝       ███████╗██║     ██║███████╗███████╗██║   ██║██████╔╝███████╗
        ██╔══██╗██║   ██║██║     ██╔═██╗        ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗       ╚════██║██║     ██║╚════██║╚════██║██║   ██║██╔══██╗╚════██║
        ██║  ██║╚██████╔╝╚██████╗██║  ██╗▄█╗    ██║     ██║  ██║██║     ███████╗██║  ██║▄█╗    ███████║╚██████╗██║███████║███████║╚██████╔╝██║  ██║███████║
        ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝    ╚══════╝ ╚═════╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                                                                                                                               
"""

os.system("clear")
print(Fore.RED +  "Warning: Needs a big window of the terminal to read the logo" + Fore.RESET + Back.RESET)

time.sleep(2)
os.system("clear")
print(Fore.BLUE + LOGO1 + Fore.YELLOW)

time.sleep(0.5)

def main():
    try:
        choice = input("What will you shoot? (Rock, Paper, Scissors):  ")
    except KeyboardInterrupt:
        print("Goodbye")
        os.system("clear")
        sys.exit()

    import pyfiglet 
    
    os.system("clear")
    print(pyfiglet.figlet_format("Rock", font="alligator"))
    time.sleep(1)
    os.system("clear")
    
    print(pyfiglet.figlet_format("Paper", font="alligator"))
    time.sleep(1)
    os.system("clear")
    
    print(pyfiglet.figlet_format("Scissor", font="alligator"))
    time.sleep(1)
    os.system("clear")
    
    print(Fore.RED + """
███████ ██   ██  ██████   ██████  ████████ ██ 
██      ██   ██ ██    ██ ██    ██    ██    ██ 
███████ ███████ ██    ██ ██    ██    ██    ██ 
     ██ ██   ██ ██    ██ ██    ██    ██       
███████ ██   ██  ██████   ██████     ██    ██                                              
""" + Fore.RESET)
    time.sleep(1)
    os.system("clear")
    
    if choice.lower() == "rock":
        print("You picked:")
        os.system("cat ascii/rock.txt")
    elif choice.lower() == "paper":
        print("You picked:")
        os.system("cat ascii/paper.txt")
    elif choice.lower() == "scissors":
        print("You picked:")
        os.system("cat ascii/scissors.txt")
    
    time.sleep(1 )
    os.system("clear")
    
    time.sleep(1.5)
    
    if cpu_choice.lower() == "rock":
        print("The AI picked:")
        os.system("cat ascii/rock.txt")
    elif cpu_choice.lower() == "paper":
        print("The AI picked:")
        os.system("cat ascii/paper.txt")
    elif cpu_choice.lower() == "scissors":
        print("The AI picked:")
        os.system("cat ascii/scissors.txt")
        
    
    time.sleep(1)
    os.system("clear")
    
    print("The winner is...")
    if choice.lower() == "rock" and cpu_choice.lower() == "scissors":
        print(Fore.BLUE + Player)
    if choice.lower() == "rock" and cpu_choice.lower() == "paper":
        print(Fore.BLUE + Ai)
    if choice.lower() == "paper" and cpu_choice.lower() == "scissor":
        print(Fore.BLUE + Ai)
    if choice.lower() == "scissors" and cpu_choice.lower() == "paper":
        print(Fore.BLUE + Player)
    if choice.lower() == "paper" and cpu_choice.lower() == "rock":
        print(Fore.BLUE + Player)
    if choice.lower() == "paper" and cpu_choice.lower() == "scissors":
        print(Fore.BLUE + Ai)
    if choice.lower() == cpu_choice.lower():
        print(Fore.BLUE + """
████████╗██╗███████╗██╗██╗██╗██╗
╚══██╔══╝██║██╔════╝██║██║██║██║
   ██║   ██║█████╗  ██║██║██║██║
   ██║   ██║██╔══╝  ╚═╝╚═╝╚═╝╚═╝
   ██║   ██║███████╗██╗██╗██╗██╗
   ╚═╝   ╚═╝╚══════╝╚═╝╚═╝╚═╝╚═╝
                                """)
        
    time.sleep(1)
    os.system("clear")
    sys.exit()

main()
