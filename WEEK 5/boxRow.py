from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    middle_x = CANVAS_WIDTH / 2
    middle_y = CANVAS_HEIGHT / 2

    left_x = 0
    top_y = 120

    right_x = left_x + BOX_SIZE
    bottom_y = top_y + BOX_SIZE

    for i in range(N_BOXES):
        canvas.create_rectangle(
            left_x + (i * BOX_SIZE),
            top_y,
            left_x + (i * BOX_SIZE) + BOX_SIZE,
            bottom_y,
            "white",
            "black"
        )


        
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    