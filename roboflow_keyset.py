import pyautogui as py
import keyboard as key
x, y = 0, 0
import time
while 1:
    time.sleep(0.01)
    x, y = py.position()
    
    if key.is_pressed('esc'):
        print('프로그램 종료')
        break

    if key.is_pressed('space'):
        py.click(1040, 140)
        py.moveTo(x, y)
        print("다음 사진")
        
    if key.is_pressed('q'):
        py.press('d')
        print("선택도구")
        
    if key.is_pressed('w'):
        py.press('b')
        print("사각형도구")
        
    if key.is_pressed('e'):
        py.press('p')
        print("폴리곤도구")
        
    if key.is_pressed('tab'):
        py.click(460,330)
        py.moveTo(x, y)
        print("class지우기")
        
    if key.is_pressed('1'):
        py.click(500, 390)
        py.moveTo(x, y)
        print("class1")
        
    if key.is_pressed('2'):
        py.click(500, 420)
        py.moveTo(x, y)
        print("class2")
        
    if key.is_pressed('3'):
        py.click(500, 450)
        py.moveTo(x, y)
        print("class3")
