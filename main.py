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
        return
    return
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
    listCurPos[0] += 45
    listCurPos[1] -= 40
    pyautogui.click(listCurPos)
    return

def performCloseCurTab():
    pyautogui.hotkey('ctrl', 'w')
    return



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

while True:
    findAndClick('./reactionsTds/love.PNG')
    timeOfSroll = 0
    time.sleep(3)
    while (isFound('./fbBut/like.PNG') == False and timeOfSroll <= 20):
        pyautogui.scroll(-100);
        time.sleep(.5)
        timeOfSroll += 1
    findAndMouseMove('./fbBut/like.PNG')
    time.sleep(1)

    # if (timeOfSroll > 10):
    #     timeOfSroll = 0
    #     while (isFound('./fbBut/likePic.PNG') == False and timeOfSroll <= 40):
    #         pyautogui.scroll(-150);
    #         time.sleep(.1)
    #         timeOfSroll += 1
    #     findAndMouseMove('./fbBut/likePic.PNG')
    #     time.sleep(1)

    if (timeOfSroll > 10):
        pyautogui.press('home')
        timeOfSroll = 0
        while (isFound('./fbBut/likeVideo.PNG') == False and timeOfSroll <= 20):
            pyautogui.scroll(-150);
            time.sleep(.1)
            timeOfSroll += 1
        findAndMouseMove('./fbBut/likeVideo.PNG')
        time.sleep(1)

    performLoveAction()
    performCloseCurTab()
    time.sleep(1)
    findAndClick('./reactionsTds/nhanTien.PNG')
    print('Da nhan tien thanh cong.')
    time.sleep(2)

# tds 80%
# fb 90%