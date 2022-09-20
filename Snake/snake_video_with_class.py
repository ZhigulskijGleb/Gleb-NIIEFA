import os
import random as ran
from pytimedinput import timedInput
import copy
import time
import keyboard as keyb

class field:
    "determine field size and cell array"

    def __init__(self, hieght_field, width_field, cell):
        self.hieght_field = hieght_field
        self.width_field = width_field
        self.cell = cell
    def cell_array(self):
        
def main():
    name_dict = {}
    HIEGHT_FIELD = 16
    WIDTH_FIELD = 20
    CELL = [(x,y) for y in range (HIEGHT_FIELD) for x in range (WIDTH_FIELD)]
    # moving cpmand
    COMAND = {'left':(-1,0), 'right':(1,0), 'up':(0, -1), 'down':(0, 1)}
    comand = COMAND ['up']

    #snake_position
    snake_position = [(WIDTH_FIELD // 2, 10),
                      (WIDTH_FIELD // 2, 11),
                      (WIDTH_FIELD // 2, 12)]
    #variable
    eat = (ran.randrange(1,WIDTH_FIELD-1),
           ran.randrange(1,HIEGHT_FIELD-1))
    score = 0
    name = input('Input your name:').lower()
    cwd = os.getcwd()
    os.system('cls')

    
    def print_field():
        for cell in CELL:
            if cell in snake_position:
                print ('o', end = '')
            elif cell == eat:
                print ('a', end = '')
            elif cell[0] in (0, WIDTH_FIELD - 1) or cell[1] in (0, HIEGHT_FIELD - 1):
                print ('#', end = '')
            else:
                print (' ', end = '')
            if cell[0] == WIDTH_FIELD - 1:
                print ('')
                
    def move_snake():
##        nonlocal last_cell
        new_coor = (snake_position[0][0] + comand[0],
                    snake_position[0][1] + comand[1])
        snake_position.insert(0, new_coor)
        last_cell = snake_position.pop(-1)
        return last_cell
    def rise_snake():
        snake_position.append(last_cell)

    def generate_eat():
        nonlocal eat
        eat = (ran.randrange(1,WIDTH_FIELD-1),
               ran.randrange(1,HIEGHT_FIELD-1))
    def count_score():
        print ('Your current score:',score)
        if name in name_dict:
            if score > name_dict[name]:  
                name_dict [name] = score
                print (f'Congretulation! {score} it\'s your new record')
            else:
                print ('Your maximum score:', name_dict[name])
        else:
            print ("You haven't have game history yet")
            name_dict[name] = score
            
    

    while True:
        #reload field
        print_field()

        #input with waiting
        in_com,_ = timedInput('',timeout = 0.3)
        
        
        #commands and move snake
        #check warning with reversed moving (if press "s" than "w" will not the next one)

        if in_com == 'w' and comand != COMAND['down']:
            comand = COMAND ['up']
        elif in_com == 's' and comand != COMAND['up']:
            comand = COMAND['down']
        elif in_com == 'd' and comand != COMAND['left']:
            comand = COMAND ['right']
        elif in_com == 'a' and comand != COMAND['right']:
            comand = COMAND ['left']
        elif in_com == 'q':
            break
        
        #new coord of snake
        snake_copy = copy.deepcopy(snake_position)
##        move_snake()
        last_cell = move_snake()

        #eating
        if snake_position[0] == eat:
            rise_snake()
            generate_eat()
            score += 1
        
        #boundary comditions
        if snake_position[0] in snake_copy or snake_position[0][0] in (0, WIDTH_FIELD - 1) or snake_position[0][1] in (0, HIEGHT_FIELD - 1):
            print ('DEFEAT')
            break
        #clear 
        os.system('cls')
        #count score
        
    #delete game window
    os.system('cls')

    #pause between game and score count
    time.sleep(1)
    #creat file if it not found
    with open(f'{cwd}\\snake_score.txt', 'a') as score_file:
        score_file.write('g,0')    
    #score count and print maximum score
    with open(f'{cwd}\snake_score.txt', 'r') as score_file:
        name_dict = {line.split(',')[0]: int(line.split(',')[1])
                     for line in score_file}
    ##    for line in score_file:
    ##        key,value = line.lower().split(',')
    ##        name_dict[key] = int(value)
    with open(f'{cwd}\snake_score.txt', 'w') as score_file:
        count_score()
        for key, value in name_dict.items():
            score_file.write(f'{key},{value}\n')
    #show current working directory
#start game
while True:
    main()
    print('Press "enter" to restart\nPress any other key to end the game')
    event = keyb.read_event()
    if event.event_type == keyb.KEY_DOWN and event.name == 'enter':
        continue
    break



    #python "D:\Python projects\Education\snake_video.py"
    #python "C:\Users\idtfs\Downloads\snake_video.py"
#C:\Users\idtfs\OneDrive\Рабочий стол\Gleb\

    


    
