from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_random_circle(canvas)
    
def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

def draw_random_circle(canvas):
    for i in range (N_CIRCLES):

        left_x = random.randint(0, CANVAS_WIDTH)
        top_y = random.randint(0, CANVAS_HEIGHT)

        right_x = left_x + CIRCLE_SIZE
        bottom_y = top_y + CIRCLE_SIZE

        color = random_color()

        canvas.create_oval(
            left_x,
            top_y,
            right_x,
            bottom_y,
            color
        )


if __name__ == '__main__':
    main()