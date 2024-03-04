import pyautogui as py
import time


time.sleep(2)

py.hotkey('winleft')
py.write('Google Chrome', interval=0.1)
py.press('enter')
time.sleep(2)

py.click(x=400, y=300)
time.sleep(2)

py.hotkey('winleft')
py.write('Bloco de Notas', interval=0.1)
py.press('enter')

py.write('dadani nego, tome cuidado', interval=0.1)
