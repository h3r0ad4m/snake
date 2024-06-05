#pgzero
import pgzero
import pgzrun
import random
import time

grid_x = 20
grid_y = 20
cell_size = 40

mode = 'game'

food_eaten = 0

my_map = [
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
]

def map_draw():
    for i in range(len(my_map)): 
        for j in range(len(my_map[0])): 
            if my_map[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_map[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()

WIDTH = grid_x * cell_size
HEIGHT = grid_y * cell_size

global timer

def start():
    screen.clear()

timer = 0
starting_turn = True
life = 1
snake_segments = [
    {'x': 0, 'y': 10},
    {'x': 1, 'y': 10},
    {'x': 2, 'y': 10}
]

cell = Actor('cell')
cell1 = Actor('cell1')

score = 3

def snake_collision():
    for i in range(snake_segments):
        if snake_segments[i]['x']['y'] == snake_segments['x']['y']:
            game_lost()

food_position = {
    'x' : random.randint(0, grid_x - 1),
    'y' : random.randint(0, grid_y - 1)
}


def game_won():
    screen.clear()
    screen.fill(68, 220, 76)
    screen.draw.text('You Won!')

def game_lost():
    global WIDTH
    global HEIGHT
    global score
    screen.clear()
    screen.fill((168, 220, 76))
    screen.draw.text(f'you lost with score of {score}', center = (WIDTH/2, HEIGHT/2), color = (0, 0, 0), fontsize =40)


def draw():
    global mode
    global WIDTH
    global HEIGHT
    global life
    global snake_segments
    global grid_x
    global grid_y
    global cell_size

    if life == 1 and mode == 'game':

        map_draw()


        for segment in snake_segments:
            screen.draw.filled_rect(
                Rect(
                    segment['x'] * cell_size, segment['y'] * cell_size,
                    cell_size, cell_size
                ),
                color=(66, 135, 245)
            )

        screen.draw.filled_rect(
            Rect(
                food_position['x'] * cell_size, food_position['y'] * cell_size,
                cell_size, cell_size
            ),
            color = (255, 76, 76)
        )   
        if life == 0:
            game_lost()

        screen.draw.text(str(score), topleft = (0, 0), fontsize = 70, color = (0, 0, 0))
    elif life < 1:
        game_lost()

        
#    for direction_index, direction in enumerate(direction_queue):
#        screen.draw.text(
#            'direction_queue[' + str(direction_index) + ']: ' + direction,
#            (15, 15 + 15 * direction_index))

def add_segment():
    global food_eaten
    global snake_segments
    food_eaten = 0
    snake_segments.append(
        {'x': -10000, 'y': -10000}
    )

def update(dt):
    global snake_segments
    global life
    global score
    global grid_x
    global grid_y
    global timer
    global food_position
    global food_eaten

    if life >= 1:

        score = (len(snake_segments) -3)

        timer += dt
        if timer >= 0.2:
            timer = 0

            if len(direction_queue) > 3:
                direction_queue.pop(len(direction_queue) - 1)

            if len(direction_queue) > 1:
                direction_queue.pop(0)

                next_x_position = snake_segments[0]['x']
                next_y_position = snake_segments[0]['y']

                if direction_queue[0] == 'right':
                    next_x_position += 1
                    if next_x_position >= grid_x:
                        life -= 1

                elif direction_queue[0] == 'left':
                    next_x_position -= 1
                    if next_x_position < 0:
                        life -= 1

                elif direction_queue[0] == 'down':
                    next_y_position += 1
                    if next_y_position >= grid_y:
                        life -= 1

                elif direction_queue[0] == 'up':
                    next_y_position -= 1
                    if next_y_position < 0:
                        life -= 1
                    
                snake_segments.insert(0, {'x': next_x_position, 'y': next_y_position})
                snake_segments.pop()

        if len(snake_segments) +3 == grid_x * grid_y:
            game_won()




        if (snake_segments[0]['x'] == food_position['x']
        and snake_segments[0]['y'] == food_position['y']):
            food_position = {
                'x' : random.randint(0, grid_x - 1),
                'y' : random.randint(0, grid_y - 1)
            }
            food_eaten = 1

        if food_eaten == 1:
            add_segment()

        if life == 0:
            start()
        

direction_queue = ['right']

def right():
    direction_queue.append('right')
def left():
    direction_queue.append('left')
def down():
    direction_queue.append('down')
def up():
    direction_queue.append('up')

def on_key_down(key):
    global starting_turn

    if (keyboard.D
        and starting_turn == True):
            clock.schedule_interval(right, 0.2)    
            starting_turn = False

    elif (keyboard.D
        and direction_queue[0] != 'right'
        and direction_queue[0] != 'left'):
            clock.schedule_interval(right, 0.2)
            clock.unschedule(left)
            clock.unschedule(up)
            clock.unschedule(down)

    elif (keyboard.A
        and direction_queue[-1] != 'left'
        and direction_queue[-1] != 'right'):
            clock.schedule_interval(left, 0.2)
            clock.unschedule(right)
            clock.unschedule(up)
            clock.unschedule(down)

    elif (keyboard.S
        and direction_queue[0] != 'down'
        and direction_queue[0] != 'up'):
            clock.schedule_interval(down, 0.2)
            clock.unschedule(right)
            clock.unschedule(left)
            clock.unschedule(up)

    elif (keyboard.W
        and direction_queue[-1] != 'up'
        and direction_queue[-1] != 'down'):
            clock.schedule_interval(up, 0.2)
            clock.unschedule(right)
            clock.unschedule(left)
            clock.unschedule(down)

pgzrun.go()