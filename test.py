from time import sleep
import pyautogui as auto




sleep(5)

x_position,y_position = auto.position()
print(x_position,y_position)