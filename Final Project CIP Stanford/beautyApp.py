from graphics import Canvas

import time
    
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    menu(canvas)

def menu(canvas):
    # APP TITLE
    canvas.create_image(0,0, 'menu.PNG')

    canvas.create_text(
        400,
        100,
        color= 'black',
        font_size= 100,
        font="Copperplate",
        text="BeDazzel",
        anchor= 'Center'
    )
    canvas.create_text(
        400,
        150,
        color= 'black',
        font_size= 35,
        font="Copperplate",
        text="~Make your life more interesting~",
        anchor= 'Center'
    )

    canvas.create_oval(
        250,
        200,
        550,
        260,
        'white'
    )
    canvas.create_text(
        400,
        230,
        color= 'black',
        font_size= 30,
        font="Times New Roman",
        text="Choose to Start",
        anchor= 'Center'
    )

    # Feminine Energy Option
    canvas.create_rectangle(
        80,
        280,
        380,
        580,
        'white',
        'black'
    )
    canvas.create_image(80,280, 'feminine_option.PNG')

    # Masculine Energy Option
    canvas.create_rectangle(
        420,
        280,
        720,
        580,
        'white',
        'black'
    )
    canvas.create_image(420,280,'masculine_option.PNG')

    # Start a loop for when the player clicks the Feminine Option
    while True:

        # catch the mouse click 
        clicks = canvas.get_new_mouse_clicks()

        if len(clicks) > 0:
            click = clicks[0]

            if click is not None:

                if 80 <= click[0] <= 380 and 300 <= click[1] <= 550:
                    canvas.clear()
                    feminine(canvas)
                    break

                elif 420 <= click[0] <= 720 and 300 <= click[1] <= 550:
                    canvas.clear()
                    masculine(canvas)
                    break





#############################################################################
                        # FEMININE ENERGY #
#############################################################################
def feminine(canvas):
    canvas.create_image(0,0,"feminine.PNG")

    # Feminine Title
    canvas.create_rectangle(
        80,
        120,
        720,
        180,
        'pink'
    )
    canvas.create_text(
        400,
        150,
        font="Copperplate",
        text='Feminine Energy',
        color='White',
        anchor='center',
        font_size= 60
    )
    
    canvas.create_oval(
        150,
        200,
        650,
        270,
        'pink'
    )
    canvas.create_text(
        400,
        235,
        font="Copperplate",
        text='Choose Your Path',
        color='White',
        anchor='center',
        font_size= 45
    )


    # Option 1
    canvas.create_rectangle(
        200,
        280,
        600,
        330,
        'white',
        'black'
    )
    canvas.create_text(
        400,
        305,
        font="Times New Roman",
        text='Makeup',
        color='Black',
        anchor='center',
        font_size= 30
    )


    # Option 2
    canvas.create_rectangle(
        200,
        350,
        600,
        400,
        'white',
        'black'
    )
    canvas.create_text(
        400,
        375,
        font="Times New Roman",
        text='Hairstyle',
        color='Black',
        anchor='center',
        font_size= 30
    )


    # Option 3
    canvas.create_rectangle(
        200,
        420,
        600,
        470,
        'white',
        'black'
    )
    canvas.create_text(
        400,
        445,
        font="Times New Roman",
        text='Fashion',
        color='Black',
        anchor='center',
        font_size= 30
    )



 # Start a loop for when the player clicks one of the option
    while True:

        # catch the mouse click 
        clicks = canvas.get_new_mouse_clicks()

        if len(clicks) > 0:
            click = clicks[0]

            if click is not None:

                if 200 <= click[0] <= 600 and 280 <= click[1] <= 330:
                    canvas.clear()
                    feminine_makeup(canvas)
                    break

                elif 200 <= click[0] <= 600 and 350 <= click[1] <= 400:
                    canvas.clear()
                    feminine_hairstyle(canvas)
                    break

                elif 200 <= click[0] <= 600 and 420 <= click[1] <= 470:
                    canvas.clear()
                    feminine_fashion(canvas)
                    break


#############################################################################


### MAKEUP SCREEN ###

def feminine_makeup(canvas):
    canvas.create_image(0,0,"feminine.PNG")
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
                    questions_makeup(canvas)
                    break


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

def questions_makeup(canvas):

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

############################### ANALYZING SCREEN ############################################

def analyzing(canvas):
    canvas.clear()

    # Counting down
    i = 3
    while i >= 1:
        canvas.create_image(0,0,'menu.PNG')
        canvas.create_text(
            400,
            250,
            font= 'Copperplate',
            font_size= 30,
            text= 'Analyzing...',
            color= 'black',
            anchor= 'center'
        )

        canvas.create_text(
            400,
            310,
            font= 'Georgia',
            font_size= 100,
            text= str(i),
            color= 'black',
            anchor= 'center'
        )
        
        time.sleep (1.2)

        i = i - 1

    canvas.clear()

#############################################################################################

############################# MAKEUP ANSWERS ##################################
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

#############################################################################

############################# HAIRSTYLE SCREEN #############################

def feminine_hairstyle(canvas):
    canvas.create_image(0,0,"feminine.PNG")
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
        text= 'Find Your Hair Style!',
        anchor= 'center'
    )

    canvas.create_oval(
        400,
        150,
        750,
        220,
        'pink'
    )

    canvas.create_text(
        575,
        185,
        font_size = 30,
        font= "Copperplate",
        color= 'white',
        text= 'Bangs Edition',
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
                    questions_hairstyle_feminine(canvas)
                    break


def questions_hairstyle_feminine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_text(
        400,
        80,
        font_size= 40,
        text= 'What is your face shape?',
        color= 'black',
        font= 'Copperplate',
        anchor= 'center'
    )


    # OPTION 1
    girl_oval = canvas.create_rectangle(
        50,
        120,
        250,
        320,
        'black'
    )
    canvas.create_image(50,120,'oval_girl.PNG')

    # OPTION 2
    girl_round = canvas.create_rectangle(
        300,
        120,
        500,
        320,
        'black'
    )
    canvas.create_image(300,120,'round_girl.PNG')

    # OPTION 3
    girl_square = canvas.create_rectangle(
        550,
        120,
        750,
        320,
        'black'
    )
    canvas.create_image(550,120,'square_girl.PNG')

    # OPTION 4
    girl_heart = canvas.create_rectangle(
        150,
        350,
        350,
        550,
        'black'
    )
    canvas.create_image(150,350,'heart_girl.PNG')

    # OPTION 5
    girl_long = canvas.create_rectangle(
        450,
        350,
        650,
        550,
        'black'
    )
    canvas.create_image(450,350,'long_girl.PNG')


    # Start a loop for when the player clicks the Face Shape
    while True:

        # catch the mouse click 
        clicks = canvas.get_new_mouse_clicks()

        if len(clicks) > 0:
            click = clicks[0]

            if click is not None:

                if 50 <= click[0] <= 250 and 120 <= click[1] <= 320:
                    canvas.clear()
                    analyzing(canvas)
                    oval_shape_feminine(canvas)
                    back_to_menu(canvas)
                    break
                if 300 <= click[0] <= 500 and 120 <= click[1] <= 320:
                    canvas.clear()
                    analyzing(canvas)
                    round_shape_feminine(canvas)
                    back_to_menu(canvas)
                    break
                if 550 <= click[0] <= 750 and 120 <= click[1] <= 320:
                    canvas.clear()
                    analyzing(canvas)
                    square_shape_feminine(canvas)
                    back_to_menu(canvas)
                    break
                if 150 <= click[0] <= 350 and 350 <= click[1] <= 550:
                    canvas.clear()
                    analyzing(canvas)
                    heart_shape_feminine(canvas)
                    back_to_menu(canvas)
                    break
                if 450 <= click[0] <= 650 and 350 <= click[1] <= 550:
                    canvas.clear()
                    analyzing(canvas)
                    long_shape_feminine(canvas)
                    back_to_menu(canvas)
                    break

def oval_shape_feminine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_image(50,250,'oval_face1.PNG')

    canvas.create_text(
        400,
        200,
        text= 'Here is the best bangs for your face shape!',
        color= 'Black',
        font_size= 35,
        font= 'Copperplate',
        anchor= 'Center'

    )

def round_shape_feminine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_image(50,250,'round_face1.PNG')

    canvas.create_text(
        400,
        200,
        text= 'Here is the best bangs for your face shape!',
        color= 'Black',
        font_size= 35,
        font= 'Copperplate',
        anchor= 'Center'

    )

def square_shape_feminine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_image(50,250,'square_face1.PNG')

    canvas.create_text(
        400,
        200,
        text= 'Here is the best bangs for your face shape!',
        color= 'Black',
        font_size= 35,
        font= 'Copperplate',
        anchor= 'Center'

    )

def heart_shape_feminine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_image(50,250,'heart_face1.PNG')

    canvas.create_text(
        400,
        200,
        text= 'Here is the best bangs for your face shape!',
        color= 'Black',
        font_size= 35,
        font= 'Copperplate',
        anchor= 'Center'

    )

def long_shape_feminine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_image(50,250,'long_face1.PNG')

    canvas.create_text(
        400,
        200,
        text= 'Here is the best bangs for your face shape!',
        color= 'Black',
        font_size= 35,
        font= 'Copperplate',
        anchor= 'Center'
    )

#############################################################################

############################## FASHION SCREEN ###############################
def feminine_fashion(canvas):
    canvas.create_image(0,0,"feminine.PNG")
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
        text= 'Find Your Fashion Style!',
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
                    questions_fashion_feminine(canvas)
                    break


def questions_fashion_feminine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_text(
        400,
        70,
        font_size= 40,
        text= 'Select the Season',
        color= 'black',
        font= 'Copperplate',
        anchor= 'center'
    )


    # OPTION 1
    spring = canvas.create_rectangle(
        150,
        100,
        350,
        300,
        'black'
    )

    canvas.create_image(150,100, 'spring.PNG')

    # OPTION 2
    summer = canvas.create_rectangle(
        450,
        100,
        650,
        300,
        'black'
    )

    canvas.create_image(450,100, 'summer.PNG')


    # OPTION 3
    fall = canvas.create_rectangle(
        150,
        350,
        350,
        550,
        'black'
    )

    canvas.create_image(150,350, 'fall.PNG')

    # OPTION 4
    winter = canvas.create_rectangle(
        450,
        350,
        650,
        550,
        'black'
    )

    canvas.create_image(450,350, 'winter.PNG')



# Start a loop for when the player clicks the Face Shape
    while True:

        # catch the mouse click 
        clicks = canvas.get_new_mouse_clicks()

        if len(clicks) > 0:
            click = clicks[0]

            if click is not None:

                if 150 <= click[0] <= 350 and 100 <= click[1] <= 300:
                    canvas.clear()
                    analyzing(canvas)
                    spring_feminine(canvas)
                    back_to_menu(canvas)
                    break
                if 450 <= click[0] <= 650 and 100 <= click[1] <= 300:
                    canvas.clear()
                    analyzing(canvas)
                    summer_feminine(canvas)
                    back_to_menu(canvas)
                    break
                if 150 <= click[0] <= 350 and 350 <= click[1] <= 550:
                    canvas.clear()
                    analyzing(canvas)
                    fall_feminine(canvas)
                    back_to_menu(canvas)
                    break
                if 450 <= click[0] <= 650 and 350 <= click[1] <= 550:
                    canvas.clear()
                    analyzing(canvas)
                    winter_feminine(canvas)
                    back_to_menu(canvas)
                    break


def spring_feminine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_text(
        400,
        300,
        font_size= 30,
        text= 'OPPS! COME BACK LATER FOR THE RESULTS',
        color= 'black',
        font= 'Copperplate',
        anchor= 'center'
    )

def summer_feminine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_text(
        400,
        300,
        font_size= 30,
        text= 'OPPS! COME BACK LATER FOR THE RESULTS',
        color= 'black',
        font= 'Copperplate',
        anchor= 'center'
    )

def fall_feminine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_text(
        400,
        300,
        font_size= 30,
        text= 'OPPS! COME BACK LATER FOR THE RESULTS',
        color= 'black',
        font= 'Copperplate',
        anchor= 'center'
    )

def winter_feminine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_text(
        400,
        300,
        font_size= 30,
        text= 'OPPS! COME BACK LATER FOR THE RESULTS',
        color= 'black',
        font= 'Copperplate',
        anchor= 'center'
    )


#############################################################################







#############################################################################
                        # MASCULINE ENERGY #
#############################################################################

def masculine(canvas):
    canvas.create_image(0,0, 'masculine.PNG')

    # Masculine Title
    canvas.create_rectangle(
        80,
        120,
        720,
        180,
        '#7cb5fbff'
    )
    canvas.create_text(
        400,
        150,
        font="Copperplate",
        text='Masculine Energy',
        color='White',
        anchor='center',
        font_size= 60
    )
    
    canvas.create_oval(
        150,
        200,
        650,
        270,
        '#7cb5fbff'
    )
    canvas.create_text(
        400,
        235,
        font="Copperplate",
        text='Choose Your Path',
        color='White',
        anchor='center',
        font_size= 45
    )


    # Option 1
    canvas.create_rectangle(
        200,
        280,
        600,
        330,
        'white',
        'black'
    )
    canvas.create_text(
        400,
        305,
        font="Times New Roman",
        text='Hairstyle',
        color='Black',
        anchor='center',
        font_size= 30
    )


    # Option 2
    canvas.create_rectangle(
        200,
        350,
        600,
        400,
        'white',
        'black'
    )
    canvas.create_text(
        400,
        375,
        font="Times New Roman",
        text='Fashion',
        color='Black',
        anchor='center',
        font_size= 30
    )


    # Coming soon label
    canvas.create_rectangle(
        200,
        420,
        600,
        470,
        'grey',
        'black'
    )
    canvas.create_text(
        400,
        445,
        font="Times New Roman",
        text='More features coming soon',
        color='Black',
        anchor='center',
        font_size= 30
    )



 # Start a loop for when the player clicks one of the option
    while True:

        # catch the mouse click 
        clicks = canvas.get_new_mouse_clicks()

        if len(clicks) > 0:
            click = clicks[0]

            if click is not None:

                if 200 <= click[0] <= 600 and 280 <= click[1] <= 330:
                    canvas.clear()
                    masculine_hairstyle(canvas)
                    break

                elif 200 <= click[0] <= 600 and 350 <= click[1] <= 400:
                    canvas.clear()
                    masculine_fashion(canvas)
                    break
#############################################################################


########################### Masculine Hairstyle #############################

def masculine_hairstyle(canvas):
    canvas.create_image(0,0,"masculine.PNG")
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
        color= 'blue',
        text= 'Find Your Hair Style!',
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
        color= 'blue',
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
                    questions_hairstyle_masculine(canvas)
                    break


def questions_hairstyle_masculine(canvas):
    canvas.create_image(0,0, 'masculine.PNG')

    canvas.create_text(
        400,
        80,
        font_size= 40,
        text= 'What is your face shape?',
        color= 'black',
        font= 'Copperplate',
        anchor= 'center'
    )


    # OPTION 1
    boy_oval = canvas.create_rectangle(
        50,
        120,
        250,
        320,
        'black'
    )
    canvas.create_image(50,120,'oval_boy.PNG')

    # OPTION 2
    boy_round = canvas.create_rectangle(
        300,
        120,
        500,
        320,
        'black'
    )
    canvas.create_image(300,120,'round_boy.PNG')

    # OPTION 3
    boy_square = canvas.create_rectangle(
        550,
        120,
        750,
        320,
        'black'
    )
    canvas.create_image(550,120,'square_boy.PNG')

    # OPTION 4
    boy_heart = canvas.create_rectangle(
        150,
        350,
        350,
        550,
        'black'
    )
    canvas.create_image(150,350,'rectangle_boy.PNG')

    # OPTION 5
    boy_long = canvas.create_rectangle(
        450,
        350,
        650,
        550,
        'black'
    )
    canvas.create_image(450,350,'diamond_boy.PNG')


    # Start a loop for when the player clicks the Face Shape
    while True:

        # catch the mouse click 
        clicks = canvas.get_new_mouse_clicks()

        if len(clicks) > 0:
            click = clicks[0]

            if click is not None:

                if 50 <= click[0] <= 250 and 120 <= click[1] <= 320:
                    canvas.clear()
                    analyzing(canvas)
                    oval_shape_masculine(canvas)
                    back_to_menu(canvas)
                    break
                if 300 <= click[0] <= 500 and 120 <= click[1] <= 320:
                    canvas.clear()
                    analyzing(canvas)
                    round_shape_masculine(canvas)
                    back_to_menu(canvas)
                    break
                if 550 <= click[0] <= 750 and 120 <= click[1] <= 320:
                    canvas.clear()
                    analyzing(canvas)
                    square_shape_masculine(canvas)
                    back_to_menu(canvas)
                    break
                if 150 <= click[0] <= 350 and 350 <= click[1] <= 550:
                    canvas.clear()
                    analyzing(canvas)
                    rectangle_shape_masculine(canvas)
                    back_to_menu(canvas)
                    break
                if 450 <= click[0] <= 650 and 350 <= click[1] <= 550:
                    canvas.clear()
                    analyzing(canvas)
                    diamond_shape_masculine(canvas)
                    back_to_menu(canvas)
                    break

def oval_shape_masculine(canvas):
    canvas.create_image(0,0, 'masculine.PNG')

    canvas.create_image(50,250,'oval_face2.PNG')

    canvas.create_text(
        400,
        200,
        text= 'Here is the best hairstyle for your face shape!',
        color= 'white',
        font_size= 30,
        font= 'Copperplate',
        anchor= 'Center'

    )

def round_shape_masculine(canvas):
    canvas.create_image(0,0, 'masculine.PNG')

    canvas.create_image(50,250,'round_face2.PNG')

    canvas.create_text(
        400,
        200,
        text= 'Here is the best hairstyle for your face shape!',
        color= 'white',
        font_size= 30,
        font= 'Copperplate',
        anchor= 'Center'

    )

def square_shape_masculine(canvas):
    canvas.create_image(0,0, 'masculine.PNG')

    canvas.create_image(50,250,'square_face2.PNG')

    canvas.create_text(
        400,
        200,
        text= 'Here is the best hairstyle for your face shape!',
        color= 'white',
        font_size= 30,
        font= 'Copperplate',
        anchor= 'Center'

    )

def rectangle_shape_masculine(canvas):
    canvas.create_image(0,0, 'masculine.PNG')

    canvas.create_image(50,250,'rectangle_face.PNG')

    canvas.create_text(
        400,
        200,
        text= 'Here is the best hairstyle for your face shape!',
        color= 'white',
        font_size= 30,
        font= 'Copperplate',
        anchor= 'Center'

    )

def diamond_shape_masculine(canvas):
    canvas.create_image(0,0, 'masculine.PNG')

    canvas.create_image(50,250,'diamond_face.PNG')

    canvas.create_text(
        400,
        200,
        text= 'Here is the best hairstyle for your face shape!',
        color= 'white',
        font_size= 30,
        font= 'Copperplate',
        anchor= 'Center'
    )

#############################################################################################

################################# FASHION MASCULINE #########################################

def masculine_fashion(canvas):
    canvas.create_image(0,0,"masculine.PNG")
    canvas.create_rectangle(
        100,
        200,
        700,
        300,
        'white',
    )

    canvas.create_text(
        400,
        250,
        font_size = 45,
        font= "Copperplate",
        color= 'blue',
        text= 'Find Your Fashion Style!',
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
        color= 'blue',
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
                    questions_fashion_masculine(canvas)
                    break


def questions_fashion_masculine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_text(
        400,
        70,
        font_size= 40,
        text= 'Select the Season',
        color= 'black',
        font= 'Copperplate',
        anchor= 'center'
    )


    # OPTION 1
    spring = canvas.create_rectangle(
        150,
        100,
        350,
        300,
        'black'
    )

    canvas.create_image(150,100, 'spring.PNG')

    # OPTION 2
    summer = canvas.create_rectangle(
        450,
        100,
        650,
        300,
        'black'
    )

    canvas.create_image(450,100, 'summer.PNG')


    # OPTION 3
    fall = canvas.create_rectangle(
        150,
        350,
        350,
        550,
        'black'
    )

    canvas.create_image(150,350, 'fall.PNG')

    # OPTION 4
    winter = canvas.create_rectangle(
        450,
        350,
        650,
        550,
        'black'
    )

    canvas.create_image(450,350, 'winter.PNG')



# Start a loop for when the player clicks the Face Shape
    while True:

        # catch the mouse click 
        clicks = canvas.get_new_mouse_clicks()

        if len(clicks) > 0:
            click = clicks[0]

            if click is not None:

                if 150 <= click[0] <= 350 and 100 <= click[1] <= 300:
                    canvas.clear()
                    analyzing(canvas)
                    spring_masculine(canvas)
                    back_to_menu(canvas)
                    break
                if 450 <= click[0] <= 650 and 100 <= click[1] <= 300:
                    canvas.clear()
                    analyzing(canvas)
                    summer_masculine(canvas)
                    back_to_menu(canvas)
                    break
                if 150 <= click[0] <= 350 and 350 <= click[1] <= 550:
                    canvas.clear()
                    analyzing(canvas)
                    fall_masculine(canvas)
                    back_to_menu(canvas)
                    break
                if 450 <= click[0] <= 650 and 350 <= click[1] <= 550:
                    canvas.clear()
                    analyzing(canvas)
                    winter_masculine(canvas)
                    back_to_menu(canvas)
                    break


def spring_masculine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_text(
        400,
        300,
        font_size= 30,
        text= 'OPPS! COME BACK LATER FOR THE RESULTS',
        color= 'black',
        font= 'Copperplate',
        anchor= 'center'
    )

def summer_masculine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_text(
        400,
        300,
        font_size= 30,
        text= 'OPPS! COME BACK LATER FOR THE RESULTS',
        color= 'black',
        font= 'Copperplate',
        anchor= 'center'
    )

def fall_masculine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_text(
        400,
        300,
        font_size= 30,
        text= 'OPPS! COME BACK LATER FOR THE RESULTS',
        color= 'black',
        font= 'Copperplate',
        anchor= 'center'
    )

def winter_masculine(canvas):
    canvas.create_image(0,0, 'transition.PNG')

    canvas.create_text(
        400,
        300,
        font_size= 30,
        text= 'OPPS! COME BACK LATER FOR THE RESULTS',
        color= 'black',
        font= 'Copperplate',
        anchor= 'center'
    )


#############################################################################

# Configure a 'back to menu' #

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
        color= 'black',
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

#############################################################################   

if __name__ == '__main__':
    main()