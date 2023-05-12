import timeit
from ursina import *
import random as r

app = Ursina()  # https://www.youtube.com/watch?v=OUhSnXamVK0
window.color = color.white  # Creates the window colour

korok = Animation('assets/korok',
                  collider='box',
                  x=-7)  # creates the player for the game, photo taken from https://www.etsy.com/listing/1258493574

grass1 = Entity(
    model='quad',
    texture='assets/grass',
    scale=(50, 2, 1),
    y=-1.9,
    z=1)  # Grass photo https://pngtree.com/freepng/flat-green-cartoon-grassland_7052364.html
grass2 = duplicate(grass1, x=50)
pair = [grass1, grass2]  # The grass in the game

mushroom_1 = Entity(model='quad',
                    texture='assets/mushroom_1',
                    x=10,
                    y=-0.4,
                    collider='box')  # Different obsticles in the game
mushroom_2 = Entity(model='quad',
                    texture='assets/mushroom_2',
                    x=10,
                    y=-0.4,
                    collider='box')  # Mushroom photos https://dribbble.com/shots/3398486-Mushrooms
mushroom_3 = Entity(model='quad',
                    texture='assets/mushroom_3',
                    x=10,
                    y=-0.4,
                    collider='box')
fungi = []
mushrooms = [mushroom_1, mushroom_2, mushroom_3]  # A list of the different obsticles

label = Text(text=f'Your score: {0}',
             color=color.black,
             position=(0.5, 0.4))  # A game score label
score = 0


def Mushrooms():  # Randomly generates mushroom obsticles random distances apart
    chosen = random.choice(mushrooms)
    repeatmushroom = duplicate(chosen, x=10 + r.randint(0, 4))
    fungi.append(repeatmushroom)
    invoke(Mushrooms, delay=2)  # Execute it


Mushrooms()


def update():
    for grass in pair:
        grass.x -= 6 * time.dt  # Makes the grace repeat
        if grass.x < -35:
            grass.x += 100
    for f in fungi:
        f.x -= 6 * time.dt
    if korok.intersects().hit:  # This is the endgame screen for when the player hits a mushroom
        korok.texture = 'assets/hit'
        application.pause()
        Text('Game over',
             origin=(0, -3),
             color=color.red,
             scale=3)
        label.text = ''  # Removes origional score tracker
        Text(f'Score: {score}',
             origin=(0, -2.5),
             color=color.black,
             scale=2)
        Text('Refresh to try again!',
             origin=(0, -2),
             color=color.black,
             scale=1)


def input(jump):
    global score
    if jump == 'space':
        if korok.y <= 0.01:
            korok.animate_y(2,
                            duration=0.4,
                            curve=curve.out_sine)  # Jumping animation up
            korok.animate_y(0,
                            duration=0.4,
                            delay=0.4,
                            curve=curve.in_sine)
            score += 1
            label.text = f'Score: {score}'  # Adds one to the score for every jump


camera.orthographic = True
camera.fov = 10

app.run()

# Changes: Korok (zelda) themed, updated variable names, multiple types of
# obstacles (example had one), coordinates, and a different scoring system.