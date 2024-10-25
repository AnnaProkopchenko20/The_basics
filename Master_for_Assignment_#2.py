from os import system
from time import sleep
import random
from random import randint

ROWS = COLUMNS = 4
EASY_SET = ("#", "$", "%", "&", "*", "@", "/", "Ø")
HARD_SET = ("<", ">", "^", ":", ";", "-", "_", "~")
ALL_COORDS = ("A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4",)


def level_valid(l_v) :
    l_v = l_v.strip()
    l_v = l_v.upper()
    while l_v != "E" and l_v != "H":
        l_v = input(f'Sorry, try again, its "E" or "H" but {l_v})\n: ')
    return l_v


def fill_board(l_f_b) :
    if l_f_b == "E" :
        l_f_b = [i for i in EASY_SET]
    else :
        l_f_b = [i for i in HARD_SET]
    l_f_b = l_f_b + l_f_b
    b = []
    while len(l_f_b) > 0 :
        ind = random.randint(0, len(l_f_b) - 1)
        b.append(l_f_b[ind])
        l_f_b.pop(ind)
    return list(zip(ALL_COORDS, b))


def countdown(time = 5, prompt = "") :
    print(prompt)
    for i in range(time, 0, -1):
        print(f"{i}")
        sleep(1)
    system("cls")


def valid_coords(coord, guessed, check_previous = False, previous = None ) :
    coord = coord.strip()
    while True :
        switch = True
        if " " in coord :
            coord = coord.split()
            coord = "".join(coord)
        if len(coord) > 1 :
            if coord[0].isalpha() and coord[1].isdigit():
                coord = coord[0].upper() + coord[1]
            elif coord[1].isalpha() and coord[0].isdigit() :
                coord = coord[1].upper() + coord[0]
        if check_previous and coord != None:
            if coord == previous :
                switch = False
        if coord not in ALL_COORDS or coord in guessed:
            switch = False
        if switch :
            return coord
        else :
            coord = input(f'''Please, try again\n: ''')


def valid_option(v_o) :
    while True :
        v_o = v_o.strip()
        v_o = v_o.upper()
        if v_o == "YES" or v_o == "NO" :
            return v_o


def output_board(already_guessed, end_cycle = True, coord_1 = None, coord_2 = None) :
    index = 0
    values_coords = []
    hint = 0
    print("  1 2 3 4")
    for i in range(ROWS):
        print("ABCD"[i], end=" ")
        for j in range(COLUMNS):
            if board[index][0] == coord_1 or board[index][0] == coord_2:
                print(board[index][1], end=" ")
                values_coords.append(board[index][1])
            elif board[index][0] in already_guessed:
                print(board[index][1], end=" ")
            else:
                hint += 1
                print("X", end=" ")
                end_cycle = False
            index += 1
        print()
    if hint == 2 and coord_2 == None :
        print('''Remember that closed cards are shown as "X"''')
    if coord_2 != None:
        return values_coords, end_cycle


def play_game() :
    count = 0
    already_guessed = []
    while True:
        end_cycle = True
        count += 1
        output_board(already_guessed = already_guessed, end_cycle=end_cycle)
        coord_1 = valid_coords(coord=input(f'''Please enter first coordinate\n: '''), guessed = already_guessed)
        output_board(already_guessed = already_guessed, end_cycle=end_cycle, coord_1 = coord_1)
        coord_2 = valid_coords(coord=input('''Please enter second coordinate\n: '''), guessed = already_guessed, check_previous=True, previous =  coord_1)
        a = output_board(already_guessed = already_guessed, coord_1= coord_1, coord_2=coord_2)
        values_coords = a[0]
        end_cycle = a[1]
        if values_coords[0] == values_coords[1]:
            already_guessed.append(coord_1)
            already_guessed.append(coord_2)
            countdown(prompt = "Correct!")
        elif not count % 10 and 50 >= count >= 20:
            option = valid_option(v_o=input('''It seems this game won't be useful for you...\nMaybe you should read strategies online...
Do you want to continue this game?\n(You can enter "Yes" or "No")\n: '''))
            if option == "NO":
                return count, True
        elif count > 50:
            return count, True
        else:
            countdown(prompt = "Incorrect!")
        if end_cycle :
            return count, False


def outro (result) :
    if not result[1]:
        print(f"The end! In total it took you {result[0]} tries Thanks for playing ;)")
        print('''
˚∧＿∧  　+        —̳͟͞͞💗
(  •‿• )つ  —̳͟͞͞ 💗         —̳͟͞͞💗 +
(つ　 <                —̳͟͞͞💗
｜　 _つ      +  —̳͟͞͞💗         —̳͟͞͞💗 ˚
`し´
''')
    else:
        print("Just read the rules again")
        print('''
∧__∧
(｀•ω• )づ__∧
  つ　 /( •ω•。)
しーＪ (nnノ) pat pat
''')


def intro() :
    print('''Hello, player! I am glad you chose to improve your short memory today :)
What you need to do is to enter two coordinats for this board :''')
    print("  1 2 3 4")
    for i in range(ROWS) :
        print("ABCD"[i], end = " ")
        for j in range(COLUMNS) :
            print("X", end = " ")
        print()
    sleep(6)


intro()
print("Do you want an easy or hard level?")
print(f"Easy : ",*EASY_SET)
print(f"Hard : ",*HARD_SET)
level = level_valid(l_v = input(f'For easy input - "E", for hard - "H")\n: '))
board = fill_board(l_f_b = level)
countdown(prompt = "We are starting in : ")
c = play_game()
outro(result=c)
print(f'''
I have used Google Translate to help me name some variables
https://www.messletters.com/en/text-art/
The code has been altered according to Artem Korotenko's suggestions''')
sleep(20)