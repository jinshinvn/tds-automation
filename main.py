import pyautogui
import time
import cv2
import matplotlib.pyplot as plt
import numpy as np



def takeScreenshot(directory):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(directory)
    return 

def isFound(directory):
    takeScreenshot(r'screenShot.png')
    chromeIcon = cv2.imread(directory)
    screen = cv2.imread(r'screenShot.png')
    w, h = screen.shape[:-1]
    res = cv2.matchTemplate(chromeIcon, screen, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  
        cv2.rectangle(chromeIcon, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        return True
    return False
    
def findAndClick(directory):
    takeScreenshot(r'screenShot.png')
    chromeIcon = cv2.imread(directory)
    screen = cv2.imread(r'screenShot.png')

    # heat_map = cv2.matchTemplate(chromeIcon, screen, cv2.TM_CCOEFF_NORMED)
    # h, w, _ = screen.shape
    # y, x = np.unravel_index(np.argmax(heat_map), heat_map.shape)
    # cv2.rectangle(chromeIcon, (x,y), (x+w, y+h), (0,0,255), 5)
    # plt.imshow(cv2.cvtColor(chromeIcon, cv2.COLOR_BGR2RGB))

    w, h = screen.shape[:-1]
    res = cv2.matchTemplate(chromeIcon, screen, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  
        cv2.rectangle(chromeIcon, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        pyautogui.click(pt)
        return True
    return False
    # cv2.imwrite('result.png', chromeIcon)

def findAndMouseMove(directory):
    takeScreenshot(r'screenShot.png')
    chromeIcon = cv2.imread(directory)
    screen = cv2.imread(r'screenShot.png')

    # heat_map = cv2.matchTemplate(chromeIcon, screen, cv2.TM_CCOEFF_NORMED)
    # h, w, _ = screen.shape
    # y, x = np.unravel_index(np.argmax(heat_map), heat_map.shape)
    # cv2.rectangle(chromeIcon, (x,y), (x+w, y+h), (0,0,255), 5)
    # plt.imshow(cv2.cvtColor(chromeIcon, cv2.COLOR_BGR2RGB))

    w, h = screen.shape[:-1]
    res = cv2.matchTemplate(chromeIcon, screen, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  
        cv2.rectangle(chromeIcon, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        pyautogui.moveTo(pt)
        return
    return
    # cv2.imwrite('result.png', chromeIcon)

def findAndClick2(directory):
    takeScreenshot(r'screenShot.png')
    chromeIcon = cv2.imread(directory)
    screen = cv2.imread(r'screenShot.png')
    heat_map = cv2.matchTemplate(chromeIcon, screen, cv2.TM_CCOEFF_NORMED)
    y, x = np.unravel_index(np.argmax(heat_map), heat_map.shape)
    pyautogui.click(x+3, y+3)
    return

def performLoveAction():
    listCurPos = [pyautogui.position().x, pyautogui.position().y]
    listCurPos[0] += 42.5
    listCurPos[1] -= 40
    pyautogui.click(listCurPos)
    return

def performHahaAction():
    listCurPos = [pyautogui.position().x, pyautogui.position().y]
    listCurPos[0] += 42.5 + 125
    listCurPos[1] -= 40
    pyautogui.click(listCurPos)
    return

def performCloseCurTab():
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')
    return

def isNotFound():
    if (isFound('./404.PNG')):
        pyautogui.hotkey('ctrl', 'w')
        return True
    else:
        return False




    
findAndClick('./chromeIcon.PNG')
time.sleep(1)

# pyautogui.hotkey('ctrl', 'n')
# time.sleep(1)
# pyautogui.click(532, 71)
# time.sleep(1)
# pyautogui.press(['t','r','a','o','d','o','i','s','u','b','.','c','o','m','\n'])
# time.sleep(1)
# findAndClick('./loginTds.PNG')
# time.sleep(1)
# findAndClick('./kiemXu.PNG')
# time.sleep(1)
# findAndClick('./camXucCheo.PNG')


noMoreLove = False
noMoreHaha = False

while (not noMoreHaha):

    noMoreHaha = not findAndClick('./reactionsTds/haha.PNG')
    if (noMoreHaha):
        break
    time.sleep(1)
    if (isNotFound()):
        continue
    timeOfSroll = 0
    time.sleep(3)
    while (isFound('./fbBut/like.PNG') == False and timeOfSroll <= 20):
        pyautogui.scroll(-100);
        time.sleep(.5)
        timeOfSroll += 1
    findAndMouseMove('./fbBut/like.PNG')
    time.sleep(1)

    if (timeOfSroll > 20):
        timeOfSroll = 0
        while (isFound('./fbBut/likePic.PNG') == False and timeOfSroll <= 10):
            pyautogui.scroll(-150);
            time.sleep(.1)
            timeOfSroll += 1
        findAndMouseMove('./fbBut/likePic.PNG')
        time.sleep(1)

    if (timeOfSroll > 10):
        pyautogui.press('home')
        timeOfSroll = 0
        while (isFound('./fbBut/likeVid.PNG') == False and timeOfSroll <= 10):
            pyautogui.scroll(-150);
            time.sleep(.1)
            timeOfSroll += 1
        findAndMouseMove('./fbBut/likeVid.PNG')
        time.sleep(1)

    if (timeOfSroll > 10):
        pyautogui.press('home')
        timeOfSroll = 0
        while (isFound('./fbBut/likeVidWatch.PNG') == False and timeOfSroll <= 10):
            pyautogui.scroll(-150);
            time.sleep(.1)
            timeOfSroll += 1
        findAndMouseMove('./fbBut/likeVidWatch.PNG')
        time.sleep(1)

    performHahaAction()
    performCloseCurTab()
    time.sleep(1)
    findAndClick('./reactionsTds/nhanTien.PNG')
    time.sleep(2)

while (not noMoreLove):

    noMoreLove = not findAndClick('./reactionsTds/love.PNG')
    if (noMoreLove):
        break
    if (isNotFound()):
        continue
    timeOfSroll = 0
    time.sleep(3)
    while (isFound('./fbBut/like.PNG') == False and timeOfSroll <= 20):
        pyautogui.scroll(-100);
        time.sleep(.5)
        timeOfSroll += 1
    findAndMouseMove('./fbBut/like.PNG')
    time.sleep(1)

    if (timeOfSroll > 20):
        timeOfSroll = 0
        while (isFound('./fbBut/likePic.PNG') == False and timeOfSroll <= 20):
            pyautogui.scroll(-150);
            time.sleep(.1)
            timeOfSroll += 1
        findAndMouseMove('./fbBut/likePic.PNG')
        time.sleep(1)

    if (timeOfSroll > 20):
        pyautogui.press('home')
        timeOfSroll = 0
        while (isFound('./fbBut/likeVid.PNG') == False and timeOfSroll <= 10):
            pyautogui.scroll(-150);
            time.sleep(.1)
            timeOfSroll += 1
        findAndMouseMove('./fbBut/likeVid.PNG')
        time.sleep(1)

    if (timeOfSroll > 10):
        pyautogui.press('home')
        timeOfSroll = 0
        while (isFound('./fbBut/likeVidWatch.PNG') == False and timeOfSroll <= 10):
            pyautogui.scroll(-150);
            time.sleep(.1)
            timeOfSroll += 1
        findAndMouseMove('./fbBut/likeVidWatch.PNG')
        time.sleep(1)

    performLoveAction()
    performCloseCurTab()
    time.sleep(1)
    findAndClick('./reactionsTds/nhanTien.PNG')
    time.sleep(2)
    

# tds 80%
# fb 90%