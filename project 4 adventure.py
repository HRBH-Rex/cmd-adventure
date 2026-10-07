import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
def main():
    class Room:
        def __init__(self, desc, item_1, item_2, puzzle):
            self.desc = desc
            self.item_1 = item_1
            self.item_2 = item_2
            self.puzzle = puzzle
    
    class Item:
        def __init__(self, name, desc):
            self.name = name
            self.desc = desc
            self.picked_up = False
#put second puzzel in room5 instance and change refereance in inspect using seperate if before regular inspect
    class Puzzle:
        def __init__(self, name, desc, reqItem, prompt, solution):
            self.name = name
            self.desc = desc
            self.reqItem = reqItem
            self.prompt = prompt
            self.solution = solution
            self.solved = False

        def solve(self):
            attempt = input(f"{Fore.CYAN}{self.prompt} do you want to try?: ")
            if attempt == "Yes" or attempt == "yes":
                self.solved = True
                print(f"{Fore.CYAN}{self.solution}")
            elif attempt == "No" or attempt == "no":
                print(f"{Fore.CYAN}you put the {self.reqItem} back in your inventory and move on")
            else:
                print(f"{Fore.CYAN}that doesnt seem to work, you move on.")
#items#
    #rooms1items#
    wooden_tray = Item("Wooden Tray", "A simple, pale ash wood tray with rounded edges. \nIt's used for carrying drinks or small decorative items, and the grain of the wood is smooth and refined, \nshowing off the natural beauty of the material.")
    wool_throw_blanket = Item("Wool Throw Blanket", "A soft, gray wool throw with a subtle geometric pattern. \nIt's lightweight yet warm, perfect for draping over the arm of the couch \nor wrapping around yourself for an added layer of coziness.")

    #rooms2items#
    leather_bound_journal = Item("Leather-Bound Journal", "thick, rich burgundy leather journal with gold-embossed edges. \nThe pages inside are creamy, and the texture of the leather cover is supple, \nhinting at both its age and its luxury.")
    candlestick_holder = Item("Candlestick Holder", "tall, ornate brass candlestick holder with intricate floral engravings. \nIt has a vintage, Gothic feel, with a slightly tarnished surface that adds to its charm. \nThe holder is made for long, tapered candles, casting flickering shadows across the room.")

    #rooms3items#
    cast_iron_skillet = Item("Cast Iron Skillet", "A well-seasoned, heavy-duty black cast iron skillet with a sturdy handle. \nIt has a rustic, timeless appeal, perfect for searing meat or baking cornbread, \nand feels substantial in the hand.")
    mason_jar_mug = Item("Mason Jar Mug", "A clear glass mason jar with a metal lid and a sturdy handle, \nfilled with fresh iced tea. The jar's vintage feel is matched with practicality, \nmaking it both charming and functional.")

    #rooms4items#
    cocktail_shaker = Item("Shaker", "A sleek, stainless steel cocktail shaker with a shiny chrome finish. \nIt's elegantly shaped, with smooth curves and a tight-fitting lid, \nused for mixing up classic drinks like martinis or old fashioneds.")
    crystal_decanter = Item("Decanter", "A beautifully cut crystal decanter with intricate diamond patterns etched into the glass. \nIt holds premium whiskey or scotch, and its heavy, faceted design reflects light in a dazzling way,\n adding a touch of opulence to the bar.")

    #rooms5items#
    meditation_mala_beads = Item("Meditation Mala Beads", "A string of 108 smooth, dark wood beads, with a tassel at the end. \nThe beads are used for meditation, helping the user focus as they move from bead to bead while chanting or breathing. \nEach bead feels cool and comforting in the hand.")
    singing_bowl = Item("Singing Bowl", "A small, metal singing bowl with intricate designs etched around the rim. \nWhen struck gently with a mallet, it produces a deep, \nresonating sound that fills the room with a calming vibration, \nhelping to clear the mind and induce relaxation.")

#Puzzles#
    #room1puzzle#
    tile_puzzle = Puzzle("Mosaic",
                        "There is a large mosaic on the left wall, it looks like a sliding puzzle.",
                        None,
                        "here is a large mosaic on the left wall, it looks like a sliding puzzle, attempt to solve it?.",
                        "the pieces of the mosaic slide into place quickly, forming the image of a golde key. You hear a rumbling and the room shakes for a second...")
    
    #room2puzzle#
    candle_puzzle = Puzzle("Candles",
                            "A table near the rooms centre with four candlesticks on it.",
                            candlestick_holder,
                            "An almost ring of candlesticks on a centre table, all unlit, your candlestick could complete the circle,",
                            "The Candles all catch alight and flare with tall, bright purple flames, then quickly stutter back to a more familier steady orange tougues.")
    
    #room3puzzle#
    bookcase_puzzle = Puzzle("Bookcase",
                            "A large white Bookcase with shelves full of books, there is a space left for a single book to slot into.",
                            leather_bound_journal,
                            "A large white Bookcase with shelves full of books, there is a space left for a book the size of the leatherbound journal you have to fit into,",
                            "The Book slots into place perfectly, and you can hear a series of quiet clicks coming from behind the bookcase.")
    
    #room4puzzle#
    drink_puzzle = Puzzle("Empty Bar",
                            "The bar is empty except for a lone glass that sits by one of the stools, like someone left it behind.",
                            cocktail_shaker,
                            "The bar is empty except for a lone glass that sits by one of the stools. You could pour youself drink from the cocktail shaker you have,",
                            "You get behind the bar and pour yourself a drink, but before you can grab it a figure appears on the stool on the other side of the bar. \nIt lifts the glass to you and toasts, before dissapearing along with the glass.")
    
    #room5puzzle#
    skillet_gong_puzzle1 = Puzzle("Small Hook",
                            "There is a small hook on the wall, it looks like something heavy could hang from it.",
                            cast_iron_skillet,
                            "There is a small hook on the wall, you realize you could hang te heavy cast iron skillet on it,",
                            "the burden of carrying around the iron skillet is gone, you feel much lighter.")
    
    skillet_gong_puzzle2 = Puzzle("Hanging Skillet",
                                "the iron skillet hangs from the wall.",
                                None,
                                "The iron skillet hangs from the wall, it is very remeniscenet of a gong.",
                                "The makeshift gong rings out loudly and echoes around the room, and you feel satisfied.\nAfter a while you snap back to reality and find yourself craving a nice drink.")
#Rooms#
    room1 = Room("Clean lines, light wood, neutral tones, and a focus on comfort and functionality. \nMinimalist yet cozy, with a touch of nature-inspired elements like plants and textiles.", 
                 wooden_tray, 
                 wool_throw_blanket,
                 tile_puzzle)

    room2 = Room("Dark, moody, and full of character.\nDark woods, deep reds, and rich purples create an intimate, dramatic atmosphere. \nThe room is filled with towering bookshelves and vintage décor.", 
                 leather_bound_journal, 
                 candlestick_holder,
                 candle_puzzle)

    room3 = Room("A blend of rustic and contemporary, complete with wood accents, a Large White Bookcase,\nand vintage-inspired touches. It feels warm and welcoming, \nperfect for family gatherings.", 
                 cast_iron_skillet, 
                 mason_jar_mug,
                 bookcase_puzzle)
    
    room4 = Room("Luxurious, with glossy surfaces,\n and a mix of rich metals and velvets. Fit with a bar in the corner and expenively furnished. The room has an elegant, high-end feel,\n channeling the glamour of the 1920s and 1930s.", 
                 cocktail_shaker, 
                 crystal_decanter,
                 drink_puzzle)

    room5 = Room("Calm, serene, and uncluttered, with natural materials like bamboo, stone, and soft textiles. \nThe space is designed to promote mindfulness and inner peace, \nwith a focus on simplicity.", 
                 meditation_mala_beads, 
                 singing_bowl,
                 skillet_gong_puzzle1)

    inventory = [None]
    cRoom = room1
    looped = True
    count = 0
    
    def pick_up():
        nonlocal inventory
        nonlocal cRoom
        while True:
            item = input(f"{Fore.YELLOW}Which item do you want to Pick Up?, {Fore.MAGENTA}{cRoom.item_1.name}{Fore.RESET}, {Fore.MAGENTA}{cRoom.item_2.name}{Fore.RESET}, or back?:")
            if item == cRoom.item_1.name:
                if cRoom.item_1.name in inventory:
                    print(f"{Fore.YELLOW}This item is in your inventory")
                elif cRoom.item_1.picked_up == True:
                    print(f"{Fore.YELLOW}this item has already been used")
                else:
                    inventory.append(cRoom.item_1.name)
                    print(f"{Fore.YELLOW}you picked up {Fore.MAGENTA}{cRoom.item_1.name}{Fore.YELLOW} and put it in your inventory.")
                    cRoom.item_1.picked_up = True
    
            elif item == cRoom.item_2.name:
                if cRoom.item_2.name in inventory:
                    print(f"{Fore.YELLOW}this item is already in your inventory.")
                elif cRoom.item_2.picked_up == True:
                    print(f"{Fore.YELLOW}this item has already been used")
                else:
                    inventory.append(cRoom.item_2.name)
                    print(f"{Fore.YELLOW}you picked up {Fore.MAGENTA}{cRoom.item_2.name}{Fore.YELLOW} and put it in your inventory.")
                    cRoom.item_2.picked_up = True
            elif item == "back":
                break
            else:
                print(f"{Fore.YELLOW}please enter one of the items ")

#mabye add looped counter for one time events
    def next_door():
        nonlocal cRoom, looped, count
        if cRoom == room1:
            cRoom = room2
            print (f"{Fore.BLUE}The second Room: \n{cRoom.desc}")
        elif cRoom == room2:
            cRoom = room3
            print (f"{Fore.BLUE}The third room: \n{cRoom.desc}")
        elif cRoom == room3:
            cRoom = room4
            print (f"{Fore.BLUE}The fourth room: \n{cRoom.desc}")
        elif cRoom == room4:
            cRoom = room5
            print (f"{Fore.BLUE}the fifth room: \n{cRoom.desc}")
        elif cRoom == room5:
            if looped == False:
                print(f"{Back.GREEN}as you open the door you realize your staring out into the world. freedom at last.")
                sys.exit()
            elif count == 0:
                print(f"{Back.RED}the door to the last room has lead you back into the first room, it a loop.")
                count + count + 1
                cRoom = room1
                print (f"{Fore.BLUE}The first room: \n{cRoom.desc}")
            else:
                count = count + 1
                cRoom = room1
                print (f"{Fore.BLUE}The first room: \n{cRoom.desc}")

    def prev_door():
        nonlocal cRoom, looped, count
        if cRoom == room1:
            if looped == False:
                print(f"{Back.GREEN}as you open the door you realize your staring out into the world. freedom at last.")
                sys.exit()
            elif count == 0:
                print(f"{Back.RED}the door you came in has led you to a room, its a loop.")
                cRoom = room5
                count = count + 1
                print (f"{Fore.BLUE}the fifth room: \n{cRoom.desc}")
            else:
                cRoom = room5
                count = count + 1
                print (f"{Fore.BLUE}the fifth room: \n{cRoom.desc}")
        elif cRoom == room2:
            cRoom = room1
            print (f"{Fore.BLUE}The first room: \n{cRoom.desc}")
        elif cRoom == room3:
            cRoom = room2
            print (f"{Fore.BLUE}The second Room: \n{cRoom.desc}")
        elif cRoom == room4:
            cRoom = room3
            print (f"{Fore.BLUE}The third room: \n{cRoom.desc}")
        elif cRoom == room5:
            cRoom = room4
            print (f"{Fore.BLUE}The fourth room: \n{cRoom.desc}")

            

    def open_inventory():
        nonlocal inventory
        print(f"{Fore.YELLOW}{inventory}")

    def inspect():
        nonlocal cRoom
        while True:
            item = input(f"Which do you want to inspect?({Fore.BLUE}Room{Fore.RESET}, {Fore.MAGENTA}{cRoom.item_1.name}{Fore.RESET}, {Fore.MAGENTA}{cRoom.item_2.name}{Fore.RESET}, {Fore.CYAN}{cRoom.puzzle.name}{Fore.RESET} or back?:")
            if item == "Room":
                print (f"{Fore.BLUE}{cRoom.desc}")
            elif item == cRoom.item_1.name:
                if cRoom.item_1.picked_up == True:
                    print("you've moved this item")
                else:
                    print (f"{Fore.MAGENTA}{cRoom.item_1.desc}")
            elif item == cRoom.item_2.name:
                if cRoom.item_2.picked_up == True:
                    print("you've moved this item")
                else:
                    print (f"{Fore.MAGENTA}{cRoom.item_2.desc}")
            elif item == cRoom.puzzle.name:
                if cRoom.puzzle.solved == False:
                    key = cRoom.puzzle.reqItem
                    if key == None:
                        cRoom.puzzle.solve()
                    elif key.name in inventory:
                        cRoom.puzzle.solve()
                        inventory.remove(key.name)
                    else:
                        print(f"{Fore.CYAN}{cRoom.puzzle.desc}")
                else:
                    print(f"{Fore.CYAN}{cRoom.puzzle.desc}")
                if skillet_gong_puzzle1.solved == True:
                    room5.puzzle = skillet_gong_puzzle2
            elif item == "back":
                break
            else:
                print("please enter one of the options")

    def start_game():
        print(f"{Fore.GREEN}You find yourself alone in the woods. \nYou wander for what feels like hours before finding yourself \nstanding before a house surrounded by trees."\
            "\nYou cant see any light from inside so you try to open the door, \nand find yourself wandering into a room that is...")
        print(f"{Fore.BLUE}{cRoom.desc}")

    def next_move():
        nonlocal looped
        while True:
            if tile_puzzle.solved == True and candle_puzzle.solved == True and bookcase_puzzle.solved == True and drink_puzzle.solved == True and skillet_gong_puzzle2.solved == True:
                    looped = False
                    print(f"{Fore.GREEN}you feel a breeze suddenly coming from the doorways, the loop has been broken.")
            command = input(f"what do you want to do next?(PickUp, PrevDoor, NextDoor, OpenInventory, Inspect, Quit):")
            if command == "PickUp":
                pick_up()
            elif command == "PrevDoor":
                prev_door()
            elif command == "NextDoor":
                next_door()
            elif command == "OpenInventory":
                open_inventory()
            elif command == "Inspect":
                inspect()
            elif command == "Quit":
                sys.exit()
            else:
                print("this is an invalid command")

    start_game()
    while True:
        next_move()
main()
