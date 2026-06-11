from graphics import Canvas
import math
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_cloud(canvas, 140, 10, 'salmon')
    # TODO: draw two more clouds, and three trees
    draw_cloud(canvas, 20, 50, 'pink')
    draw_cloud(canvas, 265, 30, 'purple')
    draw_trunk(canvas, 150, 200, 'brown')
    draw_trunk(canvas, 60, 200, 'brown')
    draw_trunk(canvas, 300, 200, 'brown')
    draw_leaves(canvas, 130, 170, 'red')
    draw_leaves(canvas, 40, 170, 'green')
    draw_leaves(canvas, 280, 170, 'orange')

def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in 
    different values of x and y (the location of the cloud) and
    color (the color of the cloud). 
    """
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH
    # Bottom two puffs
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )

# TODO: You should define a function like draw_cloud

# for trees, as well as for any extra elements in the scene.

def draw_trunk(canvas, x, y, color):
    end_x = x + TRUNK_WIDTH
    end_y = y + TRUNK_HEIGHT
    canvas.create_rectangle(
        x,
        y,
        end_x,
        end_y,
        color
    )

def draw_leaves(canvas, x, y, color):
    end_x = x + LEAVES_SIZE
    end_y = y + LEAVES_SIZE
    canvas.create_oval(
        x,
        y,
        end_x,
        end_y,
        color
    )

if __name__ == '__main__':
    main()