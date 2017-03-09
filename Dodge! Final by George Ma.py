#Import functions
from pygame import *
from random import *
from math import *

init()

#Colours
RED = (255, 0, 0)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
TONE = (100, 100, 100)
GREEN = (100, 255, 100)
YELLOW = (255,255,0)
BLUE = (0, 0, 255)
PURPLE = (76,0,153)
GREY = TONE
# Game States
MENUSTATE = 0
QUITSTATE = 1
PLAYSTATE = 2
INSTRUCTIONSTATE = 3

info = display.Info()
width = 1024
height = 512
midx = width/2
midy = height/2
SIZE = (width, height)
screen = display.set_mode(SIZE)
display.set_caption('Dodge!')
myClock = time.Clock()

#######################################################################
########                 MENU FUNCTIONS                   #############
#######################################################################
menuBackground = image.load("./backgrounds/stormMorning.png")
menuBackground = transform.scale(menuBackground,(width,height))

instructionBackground = image.load("./misc/instruction.png")

# button is clicked in MENUSTATE, see where and what should happen
def checkButtonMenu(button, mouseX, mouseY):
  if button == 1:
    if checkPlayMenu(mouseX, mouseY):
        return PLAYSTATE
    elif checkQuitMenu(mouseX, mouseY):
        return QUITSTATE
    elif checkInstructionMenu(mouseX, mouseY):
        return INSTRUCTIONSTATE

def checkButtonInstruction(button,mouseX,mouseY):
    if button == 1:
        if checkBackButton(mouseX, mouseY):
            return MENUSTATE

# check if mouse is within the play menu box
def checkPlayMenu(mouseX, mouseY):
  playMenuLeft = width/4 #Variables needed for the button's/box's location
  playMenuWidth = width/2
  playMenuTop = height/4
  playMenuHeight = height/5

  #Determines whether the mouse location is within the menu box
  if mouseX >= playMenuLeft and mouseX <= playMenuLeft + playMenuWidth and mouseY >= playMenuTop and mouseY <= playMenuTop + playMenuHeight:
    return True
  return False

#check if mouse is within the quit menu box
def checkQuitMenu(mouseX, mouseY):
    playMenuLeft = width/4
    playMenuWidth = width/2
    playMenuTop = height/2
    playMenuHeight = height/5

    #Determines whether the mouse location is within the Quit box
    if mouseX >= playMenuLeft and mouseX <= playMenuLeft + playMenuWidth and mouseY >= playMenuTop and mouseY <= playMenuTop + playMenuHeight:
        return True
    return False

# check if mouse is within the instruction box for the MENU
def checkInstructionMenu(mouseX, mouseY):
    playMenuLeft = width/4
    playMenuWidth = width/2
    playMenuTop = 3*(height/4)
    playMenuHeight = height/5

    #Determines whether the mouse location is within the instruction box
    if mouseX >= playMenuLeft and mouseX <= playMenuLeft + playMenuWidth and mouseY >= playMenuTop and mouseY <= playMenuTop + playMenuHeight:
        return True
    return False

def checkBackButton(mouseX,mouseY): #Check if the mouse is within the BACK button in the INSTRUCTION
    playMenuLeft = 75
    playMenuWidth = width/4
    playMenuTop = 3*(height/4)
    playMenuHeight = height/5

    #Determines whether the mouse location is within the back button
    if mouseX >= playMenuLeft and mouseX <= playMenuLeft + playMenuWidth and mouseY >= playMenuTop and mouseY <= playMenuTop + playMenuHeight:
        return True
    return False

def paintInstruction(mouseX,mouseY):#Function for the instruction state
    #Initializes text to be used
    fontInstruction = font.SysFont("Arial",width//15)
    textInstruction = fontInstruction.render("Back",1, RED)
    sizeInstruction = fontInstruction.size("Back")

    instrucCol = TONE #Sets the box colour to TONE (grey)
    if checkBackButton(mouseX, mouseY):
        instrucCol = PURPLE

    screen.blit(instructionBackground,Rect(0,0,width,height)) #Draws the instruction image

    draw.rect(screen, instrucCol, (75, 3*(height/4), width/4, height/5)) #Draws the Instruction Box
    screen.blit(textInstruction, (140, 3*(height/4) + height/10 - sizeInstruction[1]/2, sizeInstruction[0], sizeInstruction[1]))

# paint the menu screen
def paintMenu(mouseX, mouseY):
    # title fonts
    fontTitle = font.SysFont("Times New Roman",width//12)
    titleText = fontTitle.render("Dodge!", 1, RED)
    titleSize = fontTitle.size("Test")

    #Fonts needed for the menu
    fontMenu = font.SysFont("Arial",width//12)
    menuText1 = fontMenu.render("Play Game:", 1, RED)
    menuText2 = fontMenu.render("Quit Game:", 1, RED)
    menuText3 = fontMenu.render("Instructions", 1, RED)
    text1Size = fontMenu.size("Play Game:")
    text2Size = fontMenu.size("Quit Game:")
    text3Size = fontMenu.size("Instructions")

  # determine the colour of the menu options background
    colMenu1 = TONE
    colMenu2 = TONE
    colMenu3 = TONE
    if checkPlayMenu(mouseX, mouseY):
        colMenu1 = GREEN
    if checkQuitMenu(mouseX, mouseY):
        colMenu2 = BLUE
    if checkInstructionMenu(mouseX, mouseY):
        colMenu3 = YELLOW

    # draw the menu options
    screen.blit(menuBackground,Rect(0,0,width,height)) #Draws the backround image for the menu

    screen.blit(titleText, (width/2 - titleSize[0]/1, height/10 - titleSize[1]/2, titleSize[0], titleSize[1])) #Draws the title

    draw.rect(screen, colMenu1, (width/4, height/4, width/2, height/5)) #Draws the Play Menu Box
    screen.blit(menuText1, (width/2 - text1Size[0]/2, height/4 + height/10 - text1Size[1]/2, text1Size[0], text1Size[1]))

    draw.rect(screen, colMenu2, (width/4, height/2, width/2, height/5)) #Draws the Quit Box
    screen.blit(menuText2, (width/2 - text2Size[0]/2, height/2 + height/10 - text2Size[1]/2, text1Size[0], text1Size[1]))

    draw.rect(screen, colMenu3, (width/4, 3*(height/4), width/2, height/5)) #Draws the Instruction Box
    screen.blit(menuText3, (width/2 - text3Size[0]/2, 3*(height/4) + height/10 - text3Size[1]/2, text1Size[0], text1Size[1]))

    paintHighScore() #Runs the highscore function

###########################################################
########             GAME VARIABLES           #############
###########################################################
#Virus Initialization
virusX = 50 #Initial X and Y co-ordinates for each virus
virusY = 50

#Virus Settings
#Red Virus Settings
redVirusSize= 25
redVirusSpeedX= 4
redVirusSpeedY = 4

blueVirusSize = 45
blueVirusSpeedX = 3
blueVirusSpeedY = 3

purpleVirusSize = 15
purpleVirusSpeedX = 2
purpleVirusSpeedY = 2

#Player Settings
playerSize = 30
playerX = midx
playerY = midy
playerSpeedX = 10
playerSpeedY = 10

Viruses = []
score = 0
coinSpawned = False

#IMAGES
earthPic = image.load("./player/earth.png")
earthPic = transform.scale(earthPic,(playerSize*2,playerSize*2))
gameBackground = image.load("./backgrounds/stormAfternoon.png")

border = 0

#Loads images of viruses
redVirus = image.load("./enemy/redVirus.png")
blueVirus = image.load("./enemy/blueVirus.png")
purpleVirus = image.load("./enemy/purpleVirus.png")

#KEY STATES
KEY_RIGHT = False
KEY_LEFT = False
KEY_UP = False
KEY_DOWN = False

###########################################################
########             GAME FUNCTIONS           #############
###########################################################

def paintGame(pX,pY,pSize): #Function for Drawing the Game
    screen.blit(gameBackground,Rect(0,0,width,height-border)) #Draws the game background
    draw.line(screen, RED,(0,height-border),(width,height-border),3)

    screen.blit(earthPic, Rect(int(pX-pSize),int(pY-pSize),pSize,pSize))#Draws the earth
    draw.circle(screen, BLACK, (int(pX), int(pY)), pSize+2,3)

#x,y,radius,speedX,speedY,virusType
def paintRedVirus(): #Function for Drawing the Normal Red Virus & also updates the location
    screen.blit(redVirus, Rect(virus[0]-virus[2],virus[1]-virus[2],virus[2],virus[2]))
    virus[0] += virus[3]
    virus[1] += virus[4]

def paintBlueVirus(): #Function for drawing the blue virus & also updates the location
    screen.blit(blueVirus, Rect(virus[0]-virus[2],virus[1]-virus[2],virus[2],virus[2]))
    virus[0] -= virus[3]
    virus[1] -= virus[4]

def paintPurpleVirus(): #Function for the purple virus which follows the player
    screen.blit(purpleVirus, Rect(virus[0]-virus[2],virus[1]-virus[2],virus[2],virus[2]))
    if playerX+playerSize > virus[0]+virus[2]:
        virus[0] += virus[3]
    if playerX+playerSize < virus[0]+virus[2]:
        virus[0] -= virus[3]

    if playerY+playerSize > virus[1]+virus[2]:
        virus[1] += virus[4]
    if playerY+playerSize < virus[1]+virus[2]:
        virus[1] -= virus[4]

def createCoin():#Function which creates the coin and returns the value into the main loop
    return [randint(30,width-10),randint(30,height-border-10)]
def coin(location):
    draw.circle(screen,YELLOW,(location[0],location[1]),10)

def checkCollision(playerX,playerY,playerSize,virusX,virusY,virusSize): #Function which checks collision between Player and Virus
    distance = ((playerX - virusX)**2)+((playerY - virusY)**2)
    distance = sqrt(distance)
    if distance < playerSize+virusSize:
        return True
    else:
        return False

def checkCollisionCoin(circle1x,circle1y, circle2, radius1, radius2):
    #Distance formula for collision
    distance = (circle1x - circle2[0])**2 + (circle1y - circle2[1])**2
    distance = sqrt(distance)
    if distance < radius1 + radius2:
        return True
    else:
        return False

def paintScore(): #Function for drawing the score
    scoreFont = font.SysFont("Arial",width//25)
    scoreText = scoreFont.render("Score:%i" %score, 1, RED)
    scoreSize = scoreFont.size("Score:%i")
    screen.blit(scoreText, (width/15 - scoreSize[0]/2, height-45 , scoreSize[0], scoreSize[1]))

def paintHighScore(): #Function for drawing the High Score
    #Variables needed to draw the current high score (number)
    scoreFont = font.SysFont("Arial",width//12)
    scoreText = scoreFont.render("%i" %highScore, 1, PURPLE)
    scoreSize = scoreFont.size("%i")

    #Variables needed to draw the text "HighScore"
    hScoreFont = font.SysFont("Arial",width//50)
    highScoreText = hScoreFont.render("HighScore:",5, PURPLE)
    highScoreSize = hScoreFont.size("HighScore:")

    #Draws the box and the highscore
    draw.rect(screen, GREY, (3*(width/4)+50, height/2, 160, height/5))
    screen.blit(scoreText, (width-165 - scoreSize[0]/2, height/2+15 , scoreSize[0], scoreSize[1]))
    screen.blit(highScoreText, (width-160 - highScoreSize[0]/2, height/2+5 , highScoreSize[0], highScoreSize[1]))

def findHighScore(): #Function for reading the current highscore from the .dat file
    # Tries to read the high score from a file
    try:
        highScoreFile = open("./misc/highscore.dat", "r")
        highScore = int(highScoreFile.read())
        highScoreFile.close()
    except ValueError:
        highScore = 0
    return highScore

def saveHighScore(newHighScore): #Function for saving a new high-score
    highScoreFile = open("highscore.dat", "w")
    highScoreFile.write(str(newHighScore))
    highScoreFile.close()

def displayGameOver(score,highScore): #Prints the text for when the game is over into the console window
    print ("Thank you for playing Dodge!")
    print ("")
    print ("You Scored",score,"Point(s) this Round!")
    if score < highScore:
        print ("Not quite good enough.")
        print ("The highscore is still",str(highScore)+".")
        print ("Try Again!!!")
    elif score > highScore:
        print ("You beat the highscore!!!")
        print ("The new highscore is now",str(score)+"!!!")
    else:
        print ("You tied the highscore!!!")
        print ("The highscore is still",str(highScore)+"!")

#######################################################################
########              MAIN GAME LOOP                      #############
#######################################################################

# defining local variables to the main game loop
running = True         # if running is False, game will quit
gameState = MENUSTATE  # menuState
mx = my = 0 #Sets the mouse coordinates initially to 0
button = 0 #For checking what button the player is pressing
counter = 599 #Counter for starting at 599

# The game loop depending on variable running
while running:
    highScore = findHighScore() #Finds the current HIGHSCORE
  # check the game states and display accordingly
    if gameState == MENUSTATE:
        paintMenu(mx, my)# draw the main menu
    elif gameState == INSTRUCTIONSTATE:
        paintInstruction(mx,my) #draws the instruction
    elif gameState == QUITSTATE:
        running = False# quit the game
    elif gameState == PLAYSTATE:
        paintGame(playerX, playerY, playerSize)# draw the game screen
        paintScore() #Displays the player's current score

    for evnt in event.get():          # check for events
        if evnt.type == QUIT: #Checks if evnt.type is quit, means the program needs to be closd
            running = False

        if evnt.type == MOUSEMOTION: #Checks for mouse position
            mx, my = evnt.pos

        if evnt.type == MOUSEBUTTONDOWN:
            button = evnt.button #Checks which button
            mx, my = evnt.pos #Checks for co-ordinates for where the button is being pressed down
          # button has been clicked, check for what happens
            if gameState == MENUSTATE:
                gameState = checkButtonMenu(button, mx, my)
            elif gameState == INSTRUCTIONSTATE:
                gameState = checkButtonInstruction(button, mx, my)

        if evnt.type == KEYDOWN: #Checks if the event is a keydown
            if evnt.key == K_LEFT:
                KEY_LEFT = True
            if evnt.key == K_RIGHT:
                KEY_RIGHT = True
            if evnt.key == K_UP:
                KEY_UP = True
            if evnt.key == K_DOWN:
                KEY_DOWN= True

        if evnt.type == KEYUP: #if the event is a Key being released
            if evnt.key == K_LEFT:
                KEY_LEFT = False
            if evnt.key == K_RIGHT:
                KEY_RIGHT = False
            if evnt.key == K_UP:
                KEY_UP = False
            if evnt.key == K_DOWN:
                KEY_DOWN = False

    #Code for moving the player
    if KEY_LEFT:
        playerX -= playerSpeedX
    if KEY_RIGHT:
        playerX += playerSpeedX
    if KEY_UP:
        playerY -= playerSpeedY
    if KEY_DOWN:
        playerY += playerSpeedY

    #Code for checking collision of the player on a wall
    if playerX+playerSize >= width:
        playerX -= playerSpeedX
    if playerX-playerSize <= 0:
        playerX += playerSpeedX
    if playerY+playerSize >= height-border:
        playerY -= playerSpeedY
    if playerY-playerSize <= 0:
        playerY += playerSpeedY

    if gameState == PLAYSTATE: #Checks if gamestate is in PLAYSTATE
        counter += 1
        if counter == 600:
            virusRand = randint(1,100) #Finds a random number between 1,7
            if 1 <= virusRand <= 40: #if random number is 5,6 or (33.66%) chance, spawns a purple virus
                virus = [virusX,virusY,purpleVirusSize,purpleVirusSpeedX,purpleVirusSpeedY,3]
                Viruses.append(virus)
            elif 41 <= virusRand <= 71: #if random number is 7 (16.66%) chance, spawns a blue virus
                virus = [virusX,virusY,blueVirusSize,blueVirusSpeedX,blueVirusSpeedY,2]
                Viruses.append(virus)
            else: #Else (50%) chance, spawns a red virus
                virus = [virusX,virusY,redVirusSize,redVirusSpeedX,redVirusSpeedY,1]
                Viruses.append(virus)
            counter = 0

    for virus in Viruses:
        if virus[5] == 1:
            paintRedVirus() #Draws the red virus
        elif virus[5] == 2:
            paintBlueVirus() #Draws the red virus
        elif virus[5] == 3:
            paintPurpleVirus()#Draws the purple virus

        #Checks for a collision between the virus and the wall (#x,y,radius,speedX,speedY,virusType)
        if virus[0]+virus[2] >= width:
            virus[3] *= -1
        if virus[0]-virus[2] <= 0:
            virus[3] *= -1
        if virus[1]+virus[2] >= height-border:
            virus[4] *= -1
        if virus[1]-virus[2] <= 0:
            virus[4] *= -1

        if checkCollision(playerX,playerY,playerSize+2,virus[0],virus[1],virus[2]) == True:
            displayGameOver(score,highScore)
            if score > highScore:
                saveHighScore(score)
            running = False

        if coinSpawned == False:
            coinLocation=createCoin()
            coin(coinLocation)
            coinSpawned = True
        else:
            coin(coinLocation)
            if checkCollisionCoin(playerX,playerY, coinLocation, playerSize, 10):
                score += 1
                coinSpawned = False

    display.flip()
    myClock.tick(60)

quit()
