#Guide to importing graphics/canvas: https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1238/references/graphics/

from graphics import Canvas

import random
    
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20000

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    shapes = ['circle', 'triangle', 'square', 'star']
    for i in range (N_CIRCLES):
        shape = random.choice(shapes)
        if shape == "circle":
            draw_circle(canvas)
        elif shape == "triangle":
            pass
        elif shape == "square":
            draw_square(canvas)
    
def draw_circle(canvas):
    circle_size = random.randint(0,100)
    left_x = random.randint(0,(CANVAS_WIDTH - circle_size))
    top_y = random.randint(0,(CANVAS_HEIGHT - circle_size))
    right_x = left_x + circle_size
    bottom_y = top_y + circle_size
    
    rect = canvas.create_oval(left_x, 
    top_y, 
    right_x, 
    bottom_y,
    random_color()
    )

def draw_square(canvas):
    square_size = random.randint(0,100)
    left_x = random.randint(0,(CANVAS_WIDTH - square_size))
    top_y = random.randint(0,(CANVAS_HEIGHT - square_size))
    right_x = left_x + square_size
    bottom_y = top_y + square_size
    
    rect = canvas.create_rectangle(left_x, 
    top_y, 
    right_x, 
    bottom_y,
    random_color()
    )

def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'red', 'yellow', 'green']
    return random.choice(colors)

if __name__ == '__main__':
    main()
