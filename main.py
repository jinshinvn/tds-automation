import pyautogui
import cv2
import matplotlib.pyplot as plt
import numpy as np

def takeScreenshot(directory):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(directory)
    return 

def openChrome():
    takeScreenshot(r'screenShot.png')
    chromeIcon = cv2.imread('./chromeIcon.PNG')
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
    # cv2.imwrite('result.png', chromeIcon)
    return

def openChrome2():
    takeScreenshot(r'screenShot.png')
    chromeIcon = cv2.imread('./chromeIcon.PNG')
    screen = cv2.imread(r'screenShot.png')

    heat_map = cv2.matchTemplate(chromeIcon, screen, cv2.TM_CCOEFF_NORMED)
    h, w, _ = screen.shape
    y, x = np.unravel_index(np.argmax(heat_map), heat_map.shape)
    pyautogui.click(x, y)
    print(cv2.rectangle(chromeIcon, (x,y), (x+w, y+h), (0,0,255), 5))
    print(type(cv2.rectangle(chromeIcon, (x,y), (x+w, y+h), (0,0,255), 5)))
    plt.imshow(cv2.cvtColor(chromeIcon, cv2.COLOR_BGR2RGB))

    
    return


openChrome2()
