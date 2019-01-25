import time
import pygame
import random
import sys

def spinner():
    global timesleep, angle
    img5 = pygame.image.load('clicker_copy.png')

    for z in range(0, e):
        u = 0
        while u <= e:
            u += 1
            timesleep += 0.0015
            time.sleep(timesleep)
            angle = angle + 45
            angle = angle % 360
            display = pygame.display.set_mode((800, 800))
            display.fill(white)
            center = (400, 400)
            img1 = pygame.transform.rotate(img, angle)
            size = img1.get_size()
            hSize = [n / 2 for n in size]
            pos = (center[0] - hSize[0], center[1] - hSize[1])
            img5 = pygame.transform.scale(img5,(20,100))
            display.blit(img1, pos)
            display.blit(img5, (425,0))
            pygame.display.update()
        print(angle)
        time.sleep(3)
        pygame.display.quit()
        pygame.quit()
        break



e = 8
timesleep = 0.001
angle = 0
white = (255, 255, 255)
img = pygame.image.load('tototo.png')

sciencewords = ['microbiology', ' paleontology', 'aerodynamics', 'aerostatics', 'chemistry', 'embryo', 'kinetic', 'gyroscope', 'Hydrocarbons', 'redshift']
mathwords = ['algebra', 'amplitude', 'calculus', 'circumference', 'equation', 'exponent', 'finite', 'trigonometry', 'polynomial', 'logarithm']


for f in range(0,10):

    spinner()

    if angle == 45 or angle == 225:
        sciencewords1 = []
        chosen_word = random.choice(sciencewords)
        sciencewords.remove(chosen_word)
        letter = len(chosen_word)
        guessed_word = []
        print("you landed on orange! you category is science words")
        sciencewords1.append(chosen_word)


    if angle == 180 or angle == 0:
        print("pink")

    if angle == 135 or angle == 315:
        print("green")

    if angle == 90 or angle == 270:
       print("blue")

word = ['hey','hi', 'hello', 'heyo']
y = random.choice(word)
x = list(y)
ho = []
hhh = []


for j in range(0, len(y)):
    hhh.append('e')
    x[j] = "_"



#input stuff

print(x)


g = True

while g == True:
    input4 = input("guess")
    try:
        indices = [i for i, p in enumerate(y) if p == input4]
        for index in indices:
            x[index] = input4
        print(x)
        if index in indices:
            del hhh[0]
    except:
        print("im sorry, that is an invald input")

    if hhh == None:
        print("yes")
        g = False




