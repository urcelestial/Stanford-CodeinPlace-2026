from graphics import Canvas

import time
    
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

"""
SUMMARY:

This is a mini analysis app to discover women's makeup style
based of their facial features. All users need to do is choose
the facial features they have and the algorithm will decide 
which makeup style fits them the best!

MILESTONE 1:
1. Create a menu screen with background.
2. Create title
3. Create a button to start the analysis

MILESTONE 2:
1. Clear the menu screen
2. Start a new screen that provides questions about the facial features:
    Questions: 
    1. Eyes
    2. Eyebrows
    3. Nose
    4. Lips
    5. Face shape
    6. Skin color
3. Upload 3 images as choices for each questions, and users can click
whatever facial features fits them most
4. All 5 answers will be stored

MILESTONE 3:
1. Clear the questions screen
2. Create a transition screen (such as '3..2..1' or 'analysing...')

MILESTONE 4:
1. Clear the transtion screen
2. Use the if statements to determine the results
3. Upload pictures of makeup styles that will fit users the best.
4. Make a button to go back to menu screen
"""

"""
MILESTONE 1
"""

### MENU SCREEN ###
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    menu(canvas)

def menu(canvas):
    canvas.create_image(0,0,"menu.PNG")
    canvas.create_rectangle(
        100,
        200,
        700,
        300,
        'white',
        'pink'
    )

    canvas.create_text(
        400,
        250,
        font_size = 45,
        font= "Copperplate",
        color= '#FAACE9',
        text= 'Find Your Makeup Style!',
        anchor= 'center'
    )

    canvas.create_oval(
        200,
        350,
        600,
        450,
        'white'
    )
    canvas.create_text(
        400,
        400,
        font_size = 35,
        font= "Copperplate",
        color= '#FAACE9',
        text= 'Click here to start',
        anchor= 'center'
    )

    # Start a loop for when the player clicks the start button
    while True:

        # catch the mouse click 
        clicks = canvas.get_new_mouse_clicks()

        if len(clicks) > 0:
            click = clicks[0]

            if click is not None:

                if 200 <= click[0] <= 600 and 350 <= click[1] <= 450:
                    canvas.clear()
                    questions(canvas)
                    break

"""
MILESTONE 2
"""
### QUESTIONS SCREEN ###

MAKEUP_QUESTIONS = [
    # QUESTION 1 / EYES

    {
        "question": "EYE SHAPE?",
        "image": [
            "eye1.PNG",
            "eye2.PNG",
            "eye3.PNG"
        ],
        "labels": ["Doe Eyes", "Almond Eyes", "Disturned Eyes"],
        
        # Rectangle coordinates for labels
        "box_coordinates": [
            (50,450,250,500), 
            (300,450,500,500),
            (550,450,750,500)
        ]
    },

    # QUESTION 2 / EYEBROWS

    {
        "question": "EYEBROWS?",
        "image": [
            "eyebrow1.PNG",
            "eyebrow2.PNG",
            "eyebrow3.PNG"
        ],
        "labels": ["Thick Eyebrows", "Thin Eyebrows", "Normal Eyebrows"],
        
        # Rectangle coordinates for labels
        "box_coordinates": [
            (50,450,250,500), 
            (300,450,500,500),
            (550,450,750,500)
        ]
    },

    # QUESTIONS 3 / NOSE

    {
        "question": "NOSE SHAPE?",
        "image": [
            "nose1.PNG",
            "nose2.PNG",
            "nose3.PNG"
        ],
        "labels": ["High Bridge", "Straight Nose", "Low Bridge"],
        
        # Rectangle coordinates for labels
        "box_coordinates": [
            (50,450,250,500), 
            (300,450,500,500),
            (550,450,750,500)
        ]
    },

    # QUESTION 4 / LIPS

    {
        "question": "LIPS?",
        "image": [
            "lips1.PNG",
            "lips2.PNG",
            "lips3.PNG"
        ],
        "labels": ["Thick Lips", "Thin Lips", "Normal Lips"],
        
        # Rectangle coordinates for labels
        "box_coordinates": [
            (50,450,250,500), 
            (300,450,500,500),
            (550,450,750,500)
        ]
    },

    # QUESTION 5 / FACE SHAPE

    {
        "question": "FACE SHAPE?",
        "image": [
            "shape1.PNG",
            "shape2.PNG",
            "shape3.PNG"
        ],
        "labels": ["Sharp", "Oval", "Round"],
        
        # Rectangle coordinates for labels
        "box_coordinates": [
            (50,450,250,500), 
            (300,450,500,500),
            (550,450,750,500)
        ]
    },

    # QUESTION 6 / SKIN COLOR

    {
        "question": "SKIN COLOR?",
        "image": [
            "color1.PNG",
            "color2.PNG",
            "color3.PNG"
        ],
        "labels": ["Light", "Medium", "Dark"],
        
        # Rectangle coordinates for labels
        "box_coordinates": [
            (50,450,250,500), 
            (300,450,500,500),
            (550,450,750,500)
        ]
    }
]

def questions(canvas):

    user_selection = []
    current_question = 0

    while current_question < len(MAKEUP_QUESTIONS):
        # Screen will refresh everytime with a new question
        canvas.clear()
        
        canvas.create_image(0,0,'transition.PNG')
        canvas.create_text(
            400,
            80,
            font_size= 45,
            font= "Copperplate",
            text= 'What is your...',
            color= 'black',
            anchor= 'center'
        )

        canvas.create_text(
            400,
            550,
            font_size= 20,
            font= "Copperplate",
            text= 'Click the labels, NOT the pictures!!',
            color= 'black',
            anchor= 'center'
        )



        # Value of the questions choices
        data = MAKEUP_QUESTIONS[current_question]

        canvas.create_text(
            400,
            150,
            font_size= 60,
            font= "Copperplate",
            text= data["question"],
            color= 'black',
            anchor= 'center'
        )

        for i in range(3):
            # Placing 3 pictures side by side 
            image_x = 50 + (250 * i)
            canvas.create_image(
                image_x,
                200,
                data["image"][i]
            )

            # Placing the labels with text inside
            coordinates = data["box_coordinates"][i]
            canvas.create_rectangle(
                coordinates[0], 
                coordinates[1], 
                coordinates[2], 
                coordinates[3], 
                'white'
            )
            canvas.create_text(
                (coordinates[0]+coordinates[2])/2, 
                (coordinates[1]+coordinates[3])/2, 
                font_size= 20, 
                font= 'Copperplate', 
                text= data["labels"][i], 
                color= 'black',
                anchor= 'center'
            )
        
        while True:
            clicks = canvas.get_new_mouse_clicks()
            if len(clicks) > 0 and clicks[0] is not None:
                click = clicks[0]
                    
                clicked_index = -1
                for i in range(3):
                    coordinates = data["box_coordinates"][i]
                    if coordinates[0] <= click[0] <= coordinates[2] and coordinates[1] <= click[1] <= coordinates[3]:
                        clicked_index = i
                            
                if clicked_index != -1:
                    # Store user's answer choice (0, 1, or 2)
                    user_selection.append(clicked_index)

                    # Move to the next question
                    current_question += 1 
                    break
    
    if user_selection.count(0) > 2:
        analyzing(canvas)
        korean_makeup(canvas)
    elif user_selection.count(1) > 2:
        analyzing(canvas)
        western_makeup(canvas)
    elif user_selection.count(2) > 2 and user_selection[5] == 2:
        analyzing(canvas)
        pakistani_makeup(canvas)
    elif (user_selection.count(2) > 2 and user_selection[5] == 1) or (user_selection.count(2) > 2 and user_selection[5] == 0):
            analyzing(canvas)
            mediterannian_makeup(canvas)
    else:
        analyzing(canvas)
        western_makeup(canvas)


# MILESTONE 3

### ANALYZING SCREEN ###

def analyzing(canvas):
    canvas.clear()

    # Counting down
    i = 3
    while i >= 1:
        canvas.create_image(0,0,'transition.PNG')
        canvas.create_text(
            400,
            250,
            font= 'Copperplate',
            font_size= 30,
            text= 'Analyzing...',
            color= 'white',
            anchor= 'center'
        )

        canvas.create_text(
            400,
            310,
            font= 'Georgia',
            font_size= 100,
            text= str(i),
            color= 'white',
            anchor= 'center'
        )
        
        time.sleep (1.2)

        i = i - 1

    canvas.clear()

        
def korean_makeup(canvas):
    canvas.create_image(0,0, "korean_makeup.PNG")

    canvas.create_oval(
        200,
        200,
        600,
        400,
        'white'
    )
    canvas.create_text(
        400,
        280,
        font_size = 25,
        font= "Copperplate",
        color= '#FAACE9',
        text= 'Your Style is...',
        anchor= 'center'
    )
    canvas.create_text(
        400,
        310,
        font_size = 35,
        font= "Copperplate",
        color= '#FAACE9',
        text= 'Korean Makeup!',
        anchor= 'center'
    )

    back_to_menu(canvas)

def western_makeup(canvas):
    canvas.create_image(0,0, "western_makeup.PNG")

    canvas.create_oval(
        200,
        200,
        600,
        400,
        'white'
    )
    canvas.create_text(
        400,
        280,
        font_size = 25,
        font= "Copperplate",
        color= '#FAACE9',
        text= 'Your Style is...',
        anchor= 'center'
    )
    canvas.create_text(
        400,
        310,
        font_size = 35,
        font= "Copperplate",
        color= '#FAACE9',
        text= 'Western Makeup!',
        anchor= 'center'
    )

    back_to_menu(canvas)

def pakistani_makeup(canvas):
    canvas.create_image(0,0, "pakistani_makeup.PNG")

    canvas.create_oval(
        200,
        200,
        600,
        400,
        'white'
    )
    canvas.create_text(
        400,
        280,
        font_size = 25,
        font= "Copperplate",
        color= '#FAACE9',
        text= 'Your Style is...',
        anchor= 'center'
    )
    canvas.create_text(
        400,
        310,
        font_size = 35,
        font= "Copperplate",
        color= '#FAACE9',
        text= 'Pakistani Makeup!',
        anchor= 'center'
    )

    back_to_menu(canvas)

def mediterannian_makeup(canvas):
    canvas.create_image(0,0, "mediterannian_makeup.PNG")

    canvas.create_oval(
        200,
        200,
        600,
        400,
        'white'
    )
    canvas.create_text(
        400,
        280,
        font_size = 25,
        font= "Copperplate",
        color= '#FAACE9',
        text= 'Your Style is...',
        anchor= 'center'
    )
    canvas.create_text(
        400,
        310,
        font_size = 35,
        font= "Copperplate",
        color= '#FAACE9',
        text= 'Mediterannian Makeup!',
        anchor= 'center'
    )

    back_to_menu(canvas)


# MILESTONE 4 #
# Configure a 'back to menu' 

def back_to_menu(canvas):
    canvas.create_rectangle(
        550,
        500,
        750,
        550,
        'white'
    )

    canvas.create_text(
        650,
        525,
        font= 'Copperplate',
        font_size= 25,
        text= 'Back to Menu',
        color= '#FAACE9',
        anchor= 'center'
    )

    # Start a loop for when the player clicks the start button
    while True:

        # catch the mouse click 
        clicks = canvas.get_new_mouse_clicks()

        if len(clicks) > 0:
            click = clicks[0]

            if click is not None:

                if 550 <= click[0] <= 750 and 500 <= click[1] <= 550:
                    canvas.clear()
                    menu(canvas)
                    break

    

if __name__ == '__main__':
    main()