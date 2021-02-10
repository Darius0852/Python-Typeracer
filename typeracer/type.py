import pygame as pyg
import threading
import sys
import time
import random


pyg.init()
screen = pyg.display.set_mode((640, 480))
COLOR_INACTIVE = pyg.Color('lightskyblue1')
COLOR_ACTIVE = pyg.Color('dodgerblue1')
FONT = pyg.font.Font(None, 32)
testTexts = (
    "an ant hugs a grain of sand on the beach",
    "an asteroid was discovered rocketing past us",
    "my local city has the best bars in the country",
    )

startButton = False

#HEADING AND LOGO

I = 700
J = 400
surf = (255,255,255)
displaySurf = pyg.display.set_mode((I,J))
pyg.display.set_caption('Python Typeracer')
img = pyg.image.load('race.png')



class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pyg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        global TIMER
        if event.type == pyg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pyg.KEYDOWN:
            if self.active:
                if event.key == pyg.K_RETURN:
                    print(self.text)
                    self.text = ''
                    print("YOU TOOK " + str(yourTime))
                    TIMER = yourTime
                    return TIMER
                elif event.key == pyg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    counting_thread = threading.Thread(target = stopwatch)
                    counting_thread.start()
                    #Check if spacing divides axactly by 10, if so then start new line
                    textLength = len(self.text)
                    print("LENGTH = ",textLength)
                    if textLength % 50 == 0:
                        print("newline")
                        self.text = self.text[0]
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pyg.draw.rect(screen, self.color, self.rect, 2)
    
    def checkwords(self, displayWords):
        global yesCount
        # Check if words types are equal to textboox
        words = self.text.split()
        savedWords = testTexts[0].split()

        print(savedWords)
        #split text into words
        yesCount = 0
        limit = len(savedWords)
        for index, word in zip(range(limit), words):
            accuracy = 0
            print(words)
            if words[index] == savedWords[index]:
                print("YES")
                yesCount += 1
                print(yesCount)
            elif words[index] != savedWords[index]:
                print("NOPE")
            else:
                break
            accuracy = '%.2f' % ((float(yesCount) / float(limit)) * 100)
            print("Limit" + str(limit))
            print("Yes count" + str(yesCount))
            print("ACCURACY = " + str(accuracy) + "%")
            print("INDEX" + str(index))
            if index+1 == limit:
                print("SENTENCE FINISHED")
                break
        return yesCount


def stopwatch():
    global yourTime
    seconds = 10
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print "loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed) 
        time.sleep(1)   
        yourTime = elapsed
    return yourTime       


def main():
    sentenceCount = 0
    clock = pyg.time.Clock()
    input_box1 = InputBox(100, 100, 500, 50)
    input_boxes = [input_box1]
    displaySurf.fill(surf)
    # stores the width of the 
    # screen into a variable 
    width = screen.get_width() 
    
    # stores the height of the 
    # screen into a variable 
    height = screen.get_height()
    pyg.draw.rect(screen,COLOR_ACTIVE,[width/2,height/2,140,40])
    done = False
    
    myfont = pyg.font.SysFont('Ariel', 34)
    textsurface = myfont.render(testTexts[0], False, (20, 200, 100))

    


    while not done:
        global TIMERR
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                done = True
            for box in input_boxes:
                TIME = box.handle_event(event)
                print("TEST2 TIME" + str(TIME))
                if TIME > 0:
                    THETIME = TIME
                    print("TESTINGTIME" + str(THETIME))

                

            if event.type == pyg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                if button.collidepoint(mouse_pos):
                        # prints current location of mouse
                        print('button was pressed at {0}'.format(mouse_pos))
                        sentenceCount += 1
                        if sentenceCount == 0:
                            textsurface = myfont.render(testTexts[0], False, (20, 200, 100))
                        elif sentenceCount == 1:
                            textsurface = myfont.render(testTexts[1], False, (20, 200, 100))
                        elif sentenceCount == 2:
                            textsurface = myfont.render(testTexts[2], False, (20, 200, 100))
                        elif sentenceCount == 3:
                            textsurface = myfont.render(testTexts[0], False, (20, 200, 100))
                            sentenceCount = 0



        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)
        
        for word in input_boxes:
            WORDS = box.checkwords(word)
            if WORDS > 0:
                THEWORDS = WORDS
                print("TESTINGWORDS" + str(THEWORDS))
                

        screen.blit(textsurface,(100,50))

        print("TEST WORDS" + str(WORDS))
        print("TEST TIME" + str(TIME))

        try:
            wpm = (float(THEWORDS)/THETIME) * 60
            theWPM = int(wpm)
            print("wpm")
            print("%.2f" % wpm)
            playerTime = myfont.render(str(theWPM), False, (20, 200, 100))
            screen.blit(playerTime, (330, 300))
        except:
            print("An exception occurred")

        #Draw Logo
        screen.blit(img, (20, 20))

        #Draw button
        button = pyg.Rect(265, 250, 140, 50)
        pyg.draw.rect(screen, [150, 30, 10], button)


        pyg.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
    pyg.quit()