import keyboard as keyb
import copy
from time import sleep
import msvcrt


n = int(input('n:')) 
m = int(input('m:'))
snake_coor = [[int(n/2), m-4],
              [int(n/2), m-3],
              [int(n/2), m-2]]
field = []
for j in range(m):
    field.append([])
    if j == 0 or j == m-1: 
        field[j] = ( ['#' for i in range(n)] ) 
    else: 
        for i in range(n): 
            if i == 0 or i == n-1: 
                field[j].append('#') 
            else: 
                field[j].append(' ')
def print_snake(copy_field):
    print('\n')
    [print(copy_field[j]) for j in range(m)]

def move_up(pos,direct):
    copy_field = copy.deepcopy(field)
    snake_coor_c = copy.deepcopy(snake_coor)
    snake_coor[2] = snake_coor[1]
    snake_coor[1] = snake_coor_c[0]
    snake_coor[0][pos] += direct
    key = 'w'
##    keyb.write('w')
    for i,j in snake_coor:
        copy_field [j][i] = 'o'
    return print_snake(copy_field)


def move_down():
    copy_field = copy.deepcopy(field)
    snake_coor_c = copy.deepcopy(snake_coor)
    snake_coor[2] = snake_coor[1]
    snake_coor[1] = snake_coor_c[0]
    snake_coor[0][1] += 1
    key = 's'
    for i,j in snake_coor:
        copy_field [j][i] = 'o'
    return print_snake(copy_field)

def move_right():
    copy_field = copy.deepcopy(field)
    snake_coor_c = copy.deepcopy(snake_coor)
    snake_coor[2] = snake_coor[1]
    snake_coor[1] = snake_coor_c[0]
    snake_coor[0][0] += 1
    key = 'd'
    for i,j in snake_coor:
        copy_field [j][i] = 'o'
    return print_snake(copy_field)

def move_left():
    copy_field = copy.deepcopy(field)
    snake_coor_c = copy.deepcopy(snake_coor)
    snake_coor[2] = snake_coor[1]
    snake_coor[1] = snake_coor_c[0]
    snake_coor[0][0] -= 1
    key = 'a'
    for i,j in snake_coor:
        copy_field [j][i] = 'o'
    return print_snake(copy_field)

def releaseall():
    keyb.release('w')  
##def press():
##    global key
##    keyb.add_hotkey(key, move_up)
##    snake_coor = move_up()[0]
##def start(field):
##    while snake_coor[0][0] < m and snake_coor[0][0] > 0 and snake_coor[0][1] < n and snake_coor[0][0] > 0:
##        for i,j in snake_coor:
##            field [j][i] = 'o'
##        print_snake()
##        keyb.send(key)
##        sleep(2)
##        press()
##        key = press()
key = 'w'
print('\nДля старта нажмите ПРОБЕЛ')
keyb.wait('space')
keyb.add_hotkey('space',print_snake(field))
while True:
    print (key)
    event1 = keyb.read_event()
    sleep (2)
    event = keyb.read_event()
    if event.name != event1.name:
        if event.event_type == keyb.KEY_DOWN and event.name == 'w':
            move_up(1, -1)
            key == 'w'
    else
##    elif event.event_type == keyb.KEY_DOWN and event.name == 's':
##        move_down()
##    elif event.event_type == keyb.KEY_DOWN and event.name == 'd':
##        move_right()
##    elif event.event_type == keyb.KEY_DOWN and event.name == 'a':
##        move_left()


##wait('s')
##keyb.add_hotkey('s',move_down)
##keyb.add_hotkey('a',move_left)
##keyb.add_hotkey('d',move_right)
