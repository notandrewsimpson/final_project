import random
import os
import time
import pygame
import vlc


def spinner():  # function that runs the spinner
    global timesleep, angle, e
    pygame.init()
    img = pygame.image.load('tototo.png')
    img5 = pygame.image.load('clicker_copy.png')
    e = random.randint(50,100)
    for z in range(0, e):
        timesleep += 0.0015  # incrementaly slows down the speed of the spinner Bob
        time.sleep(timesleep)
        angle = angle + 45
        angle = angle % 360  # makes sure the angle value stays in 360 degrees
        display = pygame.display.set_mode((800, 800))
        display.fill(white)
        center = (400, 400)
        img1 = pygame.transform.rotate(img, angle)
        size = img1.get_size()
        hSize = [n / 2 for n in size]
        pos = (center[0] - hSize[0], center[1] - hSize[1])  # defines the center of the display
        img5 = pygame.transform.scale(img5,(20,100))
        display.blit(img1, pos)
        display.blit(img5, (425,0))
        pygame.display.update()
    pygame.display.quit()
    pygame.quit()


print("welcome lucky contestant too...")
sound1 = vlc.MediaPlayer("drumroll.mp3")  # opens drumroll file
sound1.play()  #plays drumroll file
time.sleep(4.46)  # time is set too 4.46 so right after the drum roll ends, lines 37 to 44 show up
print("               /$$                           /$$                  /$$$$$$         /$$$$$$                      /$$")
print("              | $$                          | $$                 /$$__  $$       /$$__  $$                    | $$")
print(" /$$  /$$  /$$| $$$$$$$   /$$$$$$   /$$$$$$ | $$        /$$$$$$ | $$  \__/      | $$  \__//$$$$$$   /$$$$$$  /$$$$$$   /$$   /$$ /$$$$$$$   /$$$$$$")
print("| $$ | $$ | $$| $$__  $$ /$$__  $$ /$$__  $$| $$       /$$__  $$| $$$$          | $$$$   /$$__  $$ /$$__  $$|_  $$_/  | $$  | $$| $$__  $$ /$$__  $$")
print("| $$ | $$ | $$| $$  \ $$| $$$$$$$$| $$$$$$$$| $$      | $$  \ $$| $$_/          | $$_/  | $$  \ $$| $$  \__/  | $$    | $$  | $$| $$  \ $$| $$$$$$$$")
print("| $$ | $$ | $$| $$  | $$| $$_____/| $$_____/| $$      | $$  | $$| $$            | $$    | $$  | $$| $$        | $$ /$$| $$  | $$| $$  | $$| $$_____/")
print("|  $$$$$/$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$/| $$            | $$    |  $$$$$$/| $$        |  $$$$/|  $$$$$$/| $$  | $$|  $$$$$$$")
print(" \_____/\___/ |__/  |__/ \_______/ \_______/|__/       \______/ |__/            |__/     \______/ |__/         \___/   \______/ |__/  |__/ \_______/")
print("Welcome welcome lucky contestant to wheel of fortune, where you spin to win!")
name = input("to start things off, can we get your name?")
name = name.lower()
os.chdir("..")
os.chdir("final_project")
q = open("saved_data.txt", "r")
line1 = q.readlines()
empty = []
money = 3000
empty.append(line1[0].strip())  # appends first line of saved_data.txt to a list so it can be printed
t = empty[0]
x = True
jk = True
while x == True:
    if name == t:  # if the users name is the same as the saved data name, it runs the code in the statement
        input1 = input("it looks like you have been on wheel of fortune before, would you like to resume your progress? (yes or no)")
        input1 = input1.lower()
        if input1 == "yes":
            q
            emptysaved = []
            line1
            line3 = len(line1)
            emptysaved.append(line1[0].strip())
            emptysaved.append(line1[1].strip())
            emptysaved.append(line1[2].strip())
            y = emptysaved[1]
            y = int(y)
            money = emptysaved[2]
            money = int(money)
            print("welcome back " + str(name) + ", you have $" + str(money))
            jk = False
            x = False
        elif input1 == "no":
            print("as you wish")
            y = 1
            jk = False
            x = False
        else:
            input1 = input("it looks like you have been on wheel of fortune before, would you like to resume your progress? (yes or no)")  #defensive coding so if yes or no isnt not inputted, it will prompt the user until so
    else:
        y = 1
        break

if jk == True:
    print("ok " + str(name) + ", how wheel of fortune works is you start with $ 3000 will spin the wheel and the wedge of the wheel and get a category")
    time.sleep(4)
    print("depending on the category you land on there will be a word you will have to fill in the blanks for")
    time.sleep(3)
    print("for each word you get right you will win money, if you dont guess the word, then you dont lose any money")
    time.sleep(3)
    print("you get 10 spins")
    time.sleep(1.5)
    print("you will use the $3000 to buy vowels for your word, and constants are free")
    time.sleep(2)
    print("you have 3 strikes, if you guess a letter that is not apart of the word, you lose a strike")
    time.sleep(2)
    print("also, at anytime if you want to save your data while playing, type 'save' and your data will be saved")

listx = [1,2,3,4,5,6,7,8,9,10]
sciencewords = ['microbiology', ' paleontology', 'aerodynamics', 'aerostatics', 'chemistry', 'embryo', 'kinetic', 'gyroscope', 'hydrocarbons', 'redshift']
mathwords = ['algebra', 'amplitude', 'calculus', 'circumference', 'equation', 'exponent', 'finite', 'trigonometry', 'polynomial', 'logarithm']
countries = ['afghanistan', 'bangladesh', 'cambodia', 'denmark', '	ethiopia', 'guatemala', 'honduras', 'indonesia', 'kazakhstan', 'netherlands']
torontoslang = ['bucktee', 'wasteyute', 'sweeterman', 'bare', 'ahlie', 'cyattie', 'deafaz', 'merked', 'wagwan', 'mandem']
if y > 1:
    for p in range(0, y):
        del listx[0]
    spinnum1 = listx[0]
""" lines 107 to 110 run if y is greater then 1, if it is, it takes y's value and deletes the first number in the list 
 how many times y is"""
for y in range(y,11):  # main game loop
    spinnum1 = listx[0]
    spinnum1 = str(spinnum1)
    listx.remove(min(listx))
    """ lines 113 to 115 take the first index of listx and convert it to a string so it can be printed, then the lowest value is removed from 
     listx so for the next iteration of the for loop, a new number can be printed """
    print("lets take spin number " + str(spinnum1))
    white = (255, 255, 255)
    angle = 0
    timesleep = 0.001
    time.sleep(2)
    spinner()
    g = True  # setting up the guessing loop
    vowels = ["a", "e", "i", "o", "u"]
    if angle == 45 or angle == 225:
        print("your category is science words!")
        print("your word is...")
        time.sleep(2)
        randsciword= random.choice(sciencewords)
        sciencewords.remove(randsciword)
        xx = list(randsciword)
        hhh = []
        for j in range(0, len(randsciword)):
            hhh.append('e')  # setting up correct guess of word *note used multiple times
            xx[j] = "_"  # empty word list * note used multiple times
        print(xx)
        ho = []  # guessed words list
        holder = 0  # lines 139 and 140 setting up for loop for checking if number of guesses exceeded
        strike = 3
        while g == True:
            for counter in range(holder, strike):
                input4 = str(input("pick a letter through a-z"))
                input4 = input4.lower()
                if len(input4) > 1:
                    if input4 == "save":
                        print("your information will be saved")
                        try:
                            saved = open("saved_data.txt", "x")
                        except:
                            saved = open("saved_data.txt","w")
                            saved.write('{}'.format(name) + '\n')
                            saved.write('{}'.format(y) + '\n')
                            saved.write('{}'.format(money) + '\n')
                        exit()
                        """ lines 151 to 154 save the iteration value, money, and name to the "saved_data.txt" file. the try and except statement is used so 
                         if the file "saved_data.txt already exists, the program wont error and the code under the except statement will run
                          * note used multiple times """

                    else:
                        print("that is more then one letter! Try again!")

                if input4 in ho:
                    print("you have already guessed that letter!")
                    continue

                if input4.isalpha():  # checks if input is a letter
                    if input4 in vowels:
                        input7 = input(str(input4) + " is a vowel, would you like to spend $300 to buy that vowel? you have $" + str(money) + "(yes/no")
                        input7 = input7.lower()
                        if input7 == "yes":
                            if money <= 300:
                                print("you dont have enough money for this vowel!")
                            if money >= 300:
                                ho.append(input4)
                                money = money - 300
                                indices = [i for i, p in enumerate(randsciword) if p == input4]  # checks if the vowel input is in the word * note used multiple times
                                if len(indices) > 0:  # if the letter is in the word, statement will run, if not, the else statement will run
                                    print("correct!")
                                    for index in indices:
                                        xx[index] = input4
                                        if index in indices:
                                            del hhh[0]
                                            continue
                                else:
                                    print("im sorry, that is not correct")

                        elif input7 == "no":
                            continue
                        else:
                            print("this is an invalid input! try again")
                            ho.remove([0])  # removes the input from the guesses letters list to give user another chance to enter the right input *used multiple times


                    else:
                        ho.append(input4)
                        indices = [i for i, p in enumerate(randsciword) if p == input4]  # checks if the constinant input is in the word
                        if len(indices) > 0:  # if letter is in the word, statement will run, if not, else statement will run
                            print("correct!")
                            for index in indices:
                                xx[index] = input4
                                if index in indices:
                                    del hhh[0]  # deletes a letter from the list which checks
                        else:
                            print("im sorry, that is not one of the letters!")
                            holder = holder + 1

                    print(xx)

                if not input4.isalpha():
                    print("im sorry, that is an invald input, try again!")  # defensive coding

                if len(hhh) == 0:
                    print("you guessed the word correctly!, for guessing that word correctly, you win $1500!")
                    money = money + 1500
                    g = False
                    break  # ends the loop
                if holder == strike:
                    print("im sorry, you did not guess the word, the word was " + str(randsciword))
                    g = False  # ends the loop



    if angle == 180 or angle == 0:
        print("your category is math words")
        print("your word is...")
        time.sleep(2)
        randmathword = random.choice(mathwords)
        mathwords.remove(randmathword)
        xx = list(randmathword)
        hhh = []
        for j in range(0, len(randmathword)):
            hhh.append('e')
            xx[j] = "_"
        print(xx)
        ho = []
        holder = 0
        strike = 3
        while g == True:
            for counter in range(holder,strike):
                input4 = str(input("pick a letter through a-z"))
                input4 = input4.lower()

                if len(input4) > 1:
                    if input4 == "save":
                        print("your information will be saved")
                        try:
                            saved = open("saved_data.txt", "x")
                        except:
                            saved = open("saved_data.txt","w")
                            saved.write('{}'.format(name) + '\n')
                            saved.write('{}'.format(y) + '\n')
                            saved.write('{}'.format(money) + '\n')
                        exit()
                    else:
                        print("that is more then one letter! Try again!")

                if input4 in ho:
                    print("you have already guessed that letter!")
                    continue

                if input4.isalpha():
                    if input4 in vowels:
                        input7 = input(str(input4) + " is a vowel, would you like to spend $300 to buy that vowel? you have $" + str(money) + "(yes/no")
                        input7 = input7.lower()
                        if input7 == "yes":
                            if money <= 300:
                                print("you dont have enough money for this vowel!")
                            if money >= 300:
                                ho.append(input4)
                                money = money - 300
                                indices = [i for i, p in enumerate(randmathword) if p == input4]
                                if len(indices)>0:
                                    print("correct!")
                                    for index in indices:
                                        xx[index] = input4
                                        if index in indices:
                                            del hhh[0]
                                            continue
                                else:
                                    print("im sorry, that is not correct")

                        elif input7 == "no":
                            continue
                        else:
                            print("this is an invalid input! try again")


                    else:
                        ho.append(input4)
                        indices = [i for i, p in enumerate(randmathword) if p == input4]
                        if len(indices) > 0:
                            print("correct!")
                            for index in indices:
                                xx[index] = input4
                                if index in indices:
                                    del hhh[0]
                        else:
                            print("im sorry, that is not one of the letters!")
                            holder = holder + 1
                    print(xx)

                if not input4.isalpha():
                    print("im sorry, that is an invald input, try again!")

                if len(hhh) == 0:
                    print("you guessed the word correctly!, for guessing that word correctly, you win $1500!")
                    money = money + 1500
                    g = False
                    break
                if holder == strike:
                    print("im sorry, you did not guess the word, the word was " + str(randmathword))
                    g = False

    if angle == 135 or angle == 315:
        print("your category is countries")
        print("your word is...")
        time.sleep(2)
        randcountry = random.choice(countries)
        countries.remove(randcountry)
        xx = list(randcountry)
        hhh = []
        for j in range(0, len(randcountry)):
            hhh.append('e')
            xx[j] = "_"
        print(xx)
        ho = []
        holder = 0
        strike = 3

        while g == True:
            for counter in range(holder,strike):
                input4 = str(input("pick a letter through a-z"))
                input4 = input4.lower()

                if len(input4) > 1:
                    if input4 == "save":
                        print("your information will be saved")
                        try:
                            saved = open("saved_data.txt", "x")
                        except:
                            saved = open("saved_data.txt","w")
                            saved.write('{}'.format(name) + '\n')
                            saved.write('{}'.format(y) + '\n')
                            saved.write('{}'.format(money) + '\n')
                        exit()
                    else:
                        print("that is more then one letter! Try again!")

                if input4 in ho:
                    print("you have already guessed that letter!")
                    continue

                if input4.isalpha():
                    if input4 in vowels:
                        input7 = input(str(input4) + " is a vowel, would you like to spend $300 to buy that vowel? you have $" + str(money) + "(yes/no")
                        input7 = input7.lower()
                        if input7 == "yes":
                            if money <= 300:
                                print("you dont have enough money for this vowel!")
                            if money >= 300:
                                ho.append(input4)
                                money = money - 300
                                indices = [i for i, p in enumerate(randcountry) if p == input4]
                                if len(indices)>0:
                                    print("correct!")
                                    for index in indices:
                                        xx[index] = input4
                                        if index in indices:
                                            del hhh[0]
                                            continue
                                else:
                                    print("im sorry, that is not correct")

                        elif input7 == "no":
                            continue
                        else:
                            print("this is an invalid input! try again")


                    else:
                        ho.append(input4)
                        indices = [i for i, p in enumerate(randcountry) if p == input4]
                        if len(indices) > 0:
                            print("correct!")
                            for index in indices:
                                xx[index] = input4
                                if index in indices:
                                    del hhh[0]
                        else:
                            print("im sorry, that is not one of the letters!")
                            holder = holder + 1

                    print(xx)

                if not input4.isalpha():
                    print("im sorry, that is an invald input, try again!")

                if len(hhh) == 0:
                    print("you guessed the word correctly!, for guessing that word correctly, you win $1500!")
                    money = money + 1500
                    g = False
                    break
                if holder == strike:
                    print("im sorry, you did not guess the word, the word was " + str(randcountry))
                    g = False


    if angle == 90 or angle == 270:
        print("your category is toronto slang words")
        print("your word is...")
        time.sleep(2)
        randtoslang= random.choice(torontoslang)
        torontoslang.remove(randtoslang)
        xx = list(randtoslang)
        hhh = []
        for j in range(0, len(randtoslang)):
            hhh.append('e')
            xx[j] = "_"
        print(xx)
        ho = []
        holder = 0
        strike = 3
        while g == True:
            for counter in range(holder, strike):
                input4 = str(input("pick a letter through a-z"))
                input4 = input4.lower()

                if len(input4) > 1:
                    if input4 == "save":
                        print("your information will be saved")
                        try:
                            saved = open("saved_data.txt", "x")
                        except:
                            saved = open("saved_data.txt","w")
                            saved.write('{}'.format(name) + '\n')
                            saved.write('{}'.format(y) + '\n')
                            saved.write('{}'.format(money) + '\n')
                        exit()
                    else:
                        print("that is more then one letter! Try again!")

                if input4 in ho:
                    print("you have already guessed that letter!")
                    continue

                if input4.isalpha():
                    if input4 in vowels:
                        input7 = input(str(
                            input4) + " is a vowel, would you like to spend $300 to buy that vowel? you have $" + str(
                            money) + "(yes/no")
                        input7 = input7.lower()
                        if input7 == "yes":
                            if money <= 300:
                                print("you dont have enough money for this vowel!")
                            if money >= 300:
                                ho.append(input4)
                                money = money - 300
                                indices = [i for i, p in enumerate(randtoslang) if p == input4]
                                if len(indices) > 0:
                                    print("correct!")
                                    for index in indices:
                                        xx[index] = input4
                                        if index in indices:
                                            del hhh[0]
                                            continue
                                else:
                                    print("im sorry, that is not correct")

                        elif input7 == "no":
                            continue
                        else:
                            print("this is an invalid input! try again")


                    else:
                        ho.append(input4)
                        indices = [i for i, p in enumerate(randtoslang) if p == input4]
                        if len(indices) > 0:
                            print("correct!")
                            for index in indices:
                                xx[index] = input4
                                if index in indices:
                                    del hhh[0]
                        else:
                            print("im sorry, that is not one of the letters!")
                            holder = holder + 1

                    print(xx)

                if not input4.isalpha():
                    print("im sorry, that is an invald input, try again!")

                if len(hhh) == 0:
                    print("you guessed the word correctly!, for guessing that word correctly, you win $1500!")
                    money = money + 1500
                    g = False
                    break
                if holder == strike:
                    print("im sorry, you did not guess the word, the word was " + str(randtoslang))
                    g = False
print("thanks for playing wheel for fortune! You finished with " + str(money))
time.sleep(1)
print("we hope to see you next time on wheel of fortune!")